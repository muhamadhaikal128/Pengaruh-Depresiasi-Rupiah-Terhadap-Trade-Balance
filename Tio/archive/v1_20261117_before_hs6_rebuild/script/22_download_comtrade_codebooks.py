"""Fetch public native-HS product descriptions, without credentials."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import httpx
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'input/raw/un_comtrade_hs6_20261117'
OUT=ROOT/'intermediate/comtrade_hs6'
YEARS={'H0':1992,'H1':1996,'H2':2002,'H3':2007,'H4':2012,'H5':2017,'H6':2022}

def main():
    manifest=json.loads((RAW/'download_manifest.json').read_text(encoding='utf-8'))
    editions=sorted({ed for rec in manifest['files'].values() for ed in rec.get('native_classifications',[])})
    provenance=[];rows=[]
    for ed in editions:
        path=RAW/f'product_reference_{ed}.json';url=f'https://comtradeapi.un.org/files/v1/app/reference/{ed}.json'
        if not path.exists():
            r=httpx.get(url,timeout=60,follow_redirects=False);r.raise_for_status();path.write_bytes(r.content);time.sleep(1.2)
        data=json.loads(path.read_text(encoding='utf-8-sig'))['results']
        for rec in data:
            hs=str(rec['id'])
            if len(hs)==6 and hs.isdigit():
                rows.append({'HS_Edition':ed,'HS_Edition_Year':YEARS[ed],'HS6':hs,
                    'Product_Description':rec['text'].split(' - ',1)[-1],'Reference_File':path.name})
        provenance.append({'filename':path.name,'url':url,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    df=pd.DataFrame(rows)
    assert not df.duplicated(['HS_Edition','HS6']).any()
    OUT.mkdir(parents=True,exist_ok=True)
    df.to_csv(OUT/'HS6_Product_Codebook_By_Edition.csv',index=False,encoding='utf-8-sig')
    (RAW/'product_reference_manifest.json').write_text(json.dumps({'retrieved_utc':datetime.now(timezone.utc).isoformat(),'sources':provenance},indent=2),encoding='utf-8')
    print('CODEBOOK',len(df),'rows','editions',','.join(editions),flush=True)

if __name__=='__main__':main()
