"""Resumable, quota-aware UN Comtrade HS6 extraction. Credentials never enter logs.

Indonesia is the reporter. Original HS editions are retained separately. Monthly
availability is discovered rather than inferred from annual data. Annual records
are supplementary and never disaggregated to months.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import gzip
import hashlib
import json
import time
import csv
import io
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'input/raw/un_comtrade_hs6_20261117'
BASE='https://comtradeapi.un.org/'
ISOS=['AUS','CHN','IND','JPN','KOR','MYS','SGP','THA','USA','VNM']
MAX_RECORDS=100000

def sha(blob):return hashlib.sha256(blob).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def atomic_json(path,obj):
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
    temp.replace(path)

class Download:
    def __init__(self,call_budget):
        RAW.mkdir(parents=True,exist_ok=True)
        key=''
        for line in (ROOT.parent/'.env.comtrade').read_text(encoding='utf-8-sig').splitlines():
            if line.strip().startswith('COMTRADE_API_KEY='):
                key=line.strip().split('=',1)[1].strip().strip('"').strip("'")
        if not key:raise RuntimeError('COMTRADE_API_KEY is not configured')
        self.secret=key.encode();self.calls=0;self.budget=call_budget;self.last=0
        self.rate_lock=threading.Lock();self.state_lock=threading.Lock()
        self.client=httpx.Client(headers={'Ocp-Apim-Subscription-Key':key},
            timeout=httpx.Timeout(150,connect=30),follow_redirects=False)
        self.path=RAW/'download_manifest.json'
        self.manifest=json.loads(self.path.read_text(encoding='utf-8')) if self.path.exists() else {
            'created_utc':utc(),'reporter':'IDN','reporter_code':360,'requested_start':2006,
            'classification_policy':'HS as originally reported; native edition retained',
            'monthly_missing_policy':'Never infer months from annual data or fill absent product rows',
            'files':{}}

    def fetch(self,name,route,params=None,check_limit=False):
        params=params or {};rec=self.manifest['files'].get(name);path=RAW/name
        if rec and path.exists() and rec['parameters']==params and rec['route']==route:
            if sha(path.read_bytes())!=rec['file_sha256']:raise RuntimeError('Cached file checksum mismatch: '+name)
            with gzip.open(path,'rb') as f:blob=f.read()
            return self.parse(blob,params)
        for attempt in range(4):
            with self.rate_lock:
                if self.calls>=self.budget:raise RuntimeError('Session call budget reached; rerun later to resume')
                time.sleep(max(0,1.2-(time.monotonic()-self.last)))
                self.last=time.monotonic();self.calls+=1
            start=time.monotonic()
            try:
                r=self.client.get(BASE+route,params=params)
            except httpx.RequestError as exc:
                self.log(name,0,attempt,type(exc).__name__)
                if attempt==3:raise RuntimeError('Network error for '+name) from None
                time.sleep(2**attempt);continue
            self.log(name,r.status_code,attempt)
            if r.status_code in [401,403]:raise RuntimeError('API access denied; status '+str(r.status_code))
            if r.status_code==429:
                try:delay=float(r.headers.get('Retry-After','5'))
                except ValueError:delay=5
                if delay>30:raise RuntimeError('API quota/rate wait exceeds 30 seconds; saved files remain resumable')
                if attempt==3:raise RuntimeError('Repeated API rate/quota limit; resume later')
                time.sleep(max(delay,3));continue
            if r.status_code>=500:
                if attempt==3:raise RuntimeError('Repeated server error for '+name)
                time.sleep(2**attempt);continue
            if r.status_code!=200:raise RuntimeError('API returned status '+str(r.status_code)+' for '+name)
            blob=r.content
            if self.secret in blob:raise RuntimeError('Credential reflected in response; not saved')
            try:data=self.parse(blob,params)
            except ValueError:raise RuntimeError('Non-JSON response for '+name) from None
            if data.get('error'):raise RuntimeError('API reports an application error for '+name)
            rows=data.get('data',data.get('results',[]))
            if not isinstance(rows,list):raise RuntimeError('Unexpected record container for '+name)
            if check_limit and len(rows)>=MAX_RECORDS:
                raise RuntimeError('Possible truncated response; refine request before saving '+name)
            temp=path.with_suffix(path.suffix+'.tmp')
            with gzip.open(temp,'wb') as f:f.write(blob)
            temp.replace(path)
            record={'route':route,'parameters':params,'retrieved_utc':utc(),'http_status':200,
                'records':len(rows),'response_bytes':len(blob),'response_sha256':sha(blob),
                'file_sha256':sha(path.read_bytes()),'elapsed_seconds':round(time.monotonic()-start,2),
                'row_cap_checked':bool(check_limit),'row_cap':MAX_RECORDS if check_limit else None}
            if rows and 'classificationCode' in rows[0]:
                record['native_classifications']=sorted({x['classificationCode'] for x in rows})
            with self.state_lock:
                self.manifest['files'][name]=record;self.manifest['updated_utc']=utc()
                atomic_json(self.path,self.manifest)
            return data
        raise RuntimeError('Unexpected retry exhaustion')

    def log(self,name,status,attempt,note=''):
        with self.state_lock:
            with (RAW/'request_log.jsonl').open('a',encoding='utf-8') as f:
                f.write(json.dumps({'utc':utc(),'file':name,'http_status':status,'attempt':attempt,'note':note})+'\n')

    def parse(self,blob,params):
        if params.get('format')=='csv':
            if blob.lstrip().startswith(b'{'):raise ValueError('Unexpected JSON on CSV route')
            rows=list(csv.DictReader(io.StringIO(blob.decode('utf-8-sig'))))
            if rows and 'cmdCode' not in rows[0]:raise ValueError('Unexpected CSV schema')
            return {'data':rows,'count':len(rows),'error':''}
        return json.loads(blob)

    def trade_job(self,freq,period,flow,base,mapping):
        stem=f'monthly_{period}' if freq=='M' else f'annual_{period}_{flow}'
        old=stem+'_hs6.json.gz'
        if old in self.manifest['files']:
            # Preserve and reuse successful original JSON responses already acquired.
            rec=self.manifest['files'][old]
            dat=self.fetch(old,rec['route'],rec['parameters'],True)
        else:
            params={**base,'period':str(period),'cmdCode':'AG6','flowCode':flow,'includeDesc':'false','format':'csv'}
            dat=self.fetch(stem+'_hs6.csv.gz',f'data/v1/get/C/{freq}/HS',params,True)
        rows=dat['data']
        if not rows:raise RuntimeError('Available period returned no trade: '+str(period))
        codes={int(x['partnerCode']) for x in rows}
        absent=[iso for iso,c in mapping.items() if c not in codes]
        return period,flow,len(rows),absent

    def run(self):
        ref=self.fetch('reference_partner_areas.json.gz','files/v1/app/reference/partnerAreas.json')
        countries=ref['results'];mapping={}
        for iso in ISOS:
            rows=[x for x in countries if x.get('PartnerCodeIsoAlpha3')==iso and not x.get('isGroup')
                  and not x.get('entryExpiredDate')]
            # Comtrade USA trade area 842 includes Puerto Rico and US Virgin Islands;
            # 840 is a separate geographic code. Keep the trade-area definition explicit.
            if iso=='USA':rows=[x for x in rows if int(x['PartnerCode'])==842]
            if len(rows)!=1:raise RuntimeError('Ambiguous country code: '+iso)
            mapping[iso]=int(rows[0]['PartnerCode'])
        mapping['WLD']=0
        self.manifest['partner_definition_notes']={'IND':'699, India including Sikkim (1975 onward); not historical code 356',
            'USA':'842, USA including Puerto Rico and US Virgin Islands; not geographic-only 840'}
        self.manifest['partners']=mapping;atomic_json(self.path,self.manifest)
        print('PARTNER_CODES',json.dumps(mapping),flush=True)
        monthly=self.fetch('availability_monthly.json.gz','data/v1/getDA/C/M/HS',{'reporterCode':'360'})['data']
        annual=self.fetch('availability_annual.json.gz','data/v1/getDA/C/A/HS',{'reporterCode':'360'})['data']
        periods=sorted({int(x['period']) for x in monthly if 200601<=int(x['period'])<=202610})
        years=sorted({int(x['period']) for x in annual if 2006<=int(x['period'])<=2025})
        self.manifest['available_months']=periods;self.manifest['available_years']=years
        atomic_json(self.path,self.manifest)
        print('AVAILABILITY',json.dumps({'monthly_count':len(periods),'first':min(periods),'last':max(periods),
            'annual_count':len(years),'annual_first':min(years),'annual_last':max(years)}),flush=True)
        partner=','.join(str(x) for x in sorted(mapping.values()))
        base={'reporterCode':'360','partnerCode':partner,'partner2Code':'0','customsCode':'C00','motCode':'0',
              'maxRecords':MAX_RECORDS,'includeDesc':'true','breakdownMode':'classic'}
        # Concurrent transfers share a strict request-start limiter (<=1 per 1.2s).
        # Workers return only small summaries, not multi-megabyte record lists.
        with ThreadPoolExecutor(max_workers=3) as pool:
            jobs=[pool.submit(self.trade_job,'M',p,'X,M',base,mapping) for p in periods]
            for i,f in enumerate(as_completed(jobs),1):
                p,flow,n,absent=f.result()
                print('MONTH',p,f'{i}/{len(periods)}','rows',n,'missing_partners',','.join(absent) or 'none','calls',self.calls,flush=True)
        # Annual selections are split by flow to remain below the account row cap.
        with ThreadPoolExecutor(max_workers=3) as pool:
            jobs=[pool.submit(self.trade_job,'A',y,flow,base,mapping) for y in years for flow in ['X','M']]
            for f in as_completed(jobs):
                y,flow,n,_=f.result();print('YEAR',y,flow,'rows',n,'calls',self.calls,flush=True)
        # TOTAL controls use the identical reporter, flow and partner definition.
        for freq,selection in [('M',periods),('A',years)]:
            for i in range(0,len(selection),12):
                chunk=selection[i:i+12]
                params={**base,'period':','.join(map(str,chunk)),'cmdCode':'TOTAL','flowCode':'X,M'}
                self.fetch(f'totals_{freq}_{chunk[0]}_{chunk[-1]}.json.gz',f'data/v1/get/C/{freq}/HS',params,True)
                print('TOTAL_CONTROL',freq,chunk[0],chunk[-1],flush=True)
        self.manifest['download_status']='complete';self.manifest['completed_utc']=utc()
        atomic_json(self.path,self.manifest);self.client.close()
        print('DOWNLOAD_COMPLETE','files',len(self.manifest['files']),'calls_this_run',self.calls,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--call-budget',type=int,default=420)
    args=p.parse_args();d=Download(args.call_budget)
    try:d.run()
    except Exception as exc:
        # Only our sanitized exception strings are printed; no client headers/keys.
        print('DOWNLOAD_STOPPED',str(exc),flush=True);raise SystemExit(1)
