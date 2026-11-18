"""Rebuild monetary HS6 panels and seven overlapping goods groups from raw workbooks."""
from pathlib import Path
from collections import defaultdict
import hashlib,json,re
import numpy as np
import pandas as pd
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[2]
MID=ROOT/'intermediate';RAW=ROOT/'input/raw/trademap_hs6_20261117'
REF=ROOT/'input/reference/classification_sources';D=ROOT/'output/diagnostics/data'
GROUPS={'manufacturing':'Non-komoditas (manufaktur)','consumption':'Barang konsumsi',
 'agriculture':'Komoditas pertanian & pangan','intermediate':'Bahan baku/penolong',
 'capital':'Barang modal','commodity':'Komoditas (total)','energy_mining':'Komoditas energi & tambang'}
ISO={'australia':'AUS','china':'CHN','india':'IND','japan':'JPN','korea-republic-of':'KOR',
 'malaysia':'MYS','singapore':'SGP','thailand':'THA','united-states-of-america':'USA','viet-nam':'VNM','world':'WLD'}
FIELDS=['Exports_USDk','Imports_USDk']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csv(d,p):
 p.parent.mkdir(parents=True,exist_ok=True)
 d.to_csv(p,index=False,float_format='%.15g',compression={'method':'gzip','compresslevel':3} if p.name.endswith('.gz') else None)
def consensus(v):
 s=set(v);return next(iter(s)) if len(s)==1 else 'mixed' if s else 'unclassified'
def classify():
 detail=pd.read_csv(REF/'HS6_SITC3_Commodity_Crosswalk.csv',dtype={'HS6':str,'SITC3':str})
 # Commodity group definitions use the same A11 definition as the previous study.
 com=defaultdict(set);agri=defaultdict(set);energy=defaultdict(set)
 for r in detail.itertuples():
  com[r.HS6].add(r.Commodity_Class)
  agri[r.HS6].add(int(r.Commodity_Class=='commodity' and r.Commodity_Subgroup in ['Food_beverages_tobacco_oils','Agricultural_raw_materials']))
  energy[r.HS6].add(int(r.Commodity_Class=='commodity' and r.Commodity_Subgroup in ['Fuels','Ores_metals_precious_stones_gold']))
 bec=defaultdict(set);bec_codes=defaultdict(set)
 w=load_workbook(REF/'unsd_correlations_2022.xlsx',read_only=True,data_only=True)
 for row in w.active.iter_rows(min_row=2,values_only=True):
  b=str(row[8] or '').strip();end={'1':'intermediate','2':'capital','3':'consumption'}.get(b[2:3],'unclassified')
  for value in row[:7]:
   h=str(value or '').strip().replace('.','')
   if re.fullmatch(r'\d{6}',h):bec[h].add(end);bec_codes[h].add(b)
 w.close()
 rows=[]
 for h in sorted(set(com)|set(bec)):
  c=consensus(com[h]);e=consensus(bec[h])
  rows.append({'HS6':h,'Commodity_Class':c,'BEC5_EndUse':e,'BEC5_Possible_Codes':';'.join(sorted(bec_codes[h])),
   'manufacturing':int(c=='noncommodity'),'consumption':int(e=='consumption'),
   'agriculture':int(agri[h]=={1}),'intermediate':int(e=='intermediate'),'capital':int(e=='capital'),
   'commodity':int(c=='commodity'),'energy_mining':int(energy[h]=={1}),
   'HS_Edition_Policy':'Conservative consensus across revisions; workbook revision not declared'})
 result=pd.DataFrame(rows);assert not result.HS6.duplicated().any()
 csv(result,MID/'HS6_Classification.csv')
 csv(pd.DataFrame([{'Group':k,'Label':v,'Overlapping':True} for k,v in GROUPS.items()]),MID/'Goods_Groups.csv')
 return result.set_index('HS6')
def ratios(g):
 g['Trade_Balance_USDk']=g.Exports_USDk-g.Imports_USDk
 good=g.Exports_USDk.gt(0)&g.Imports_USDk.gt(0)
 g['Ln_Imports_Exports']=np.log(g.Imports_USDk.where(good)/g.Exports_USDk.where(good))
 return g
def qaggregate(d,keys):
 d=d.copy();d['Quarter']=pd.PeriodIndex(d.Date,freq='M').asfreq('Q').astype(str)
 gr=d.groupby(keys+['Quarter'],sort=True)
 q=gr[FIELDS].sum(min_count=3).reset_index()
 n=gr[FIELDS].count().rename(columns={'Exports_USDk':'NMonths_Exports','Imports_USDk':'NMonths_Imports'}).reset_index()
 return ratios(q.merge(n,on=keys+['Quarter'],validate='one_to_one'))
def main():
 D.mkdir(parents=True,exist_ok=True);(MID/'hs6').mkdir(parents=True,exist_ok=True)
 classification=classify();manifest=json.loads((RAW/'source_manifest.json').read_text('utf-8'))
 totals=[];groups=[];audit=[];quality=[];coverage=[];labels={};inputhash={}
 for source in manifest['files']:
  p=RAW/source['filename'];assert sha(p)==source['sha256'];inputhash[p.name]=sha(p)
  name=p.name.lower();flow='Exports_USDk' if 'exports-to-' in name else 'Imports_USDk'
  slug=re.search(r'(?:exports-to-|imports-from-)(.+?)-by-product',name).group(1);iso=ISO[slug]
  w=load_workbook(p,read_only=True,data_only=True);sheet=w['Data'];it=sheet.iter_rows(values_only=True)
  for _ in range(4):next(it)
  header=next(it);months=[re.match(r'(\d{6}) \(USD Thousand\)',str(v)) for v in header[6:]]
  assert all(months),p.name
  dates=[pd.Period(x.group(1),freq='M').strftime('%Y-%m') for x in months]
  assert dates==pd.period_range('2006-01','2026-08',freq='M').astype(str).tolist(),p.name
  codes=[];values=[];total=None
  for row in it:
   h=str(row[4] or '').strip().lstrip("'")
   if not h:continue
   array=pd.to_numeric(pd.Series(row[6:6+len(dates)]),errors='coerce').to_numpy(dtype=float)
   if h=='TOTAL':
    assert str(row[0])=='360' and str(row[1])=='Indonesia',(p.name,'Reporter must be Indonesia',row[:4])
    assert total is None,p.name;total=array;continue
   assert re.fullmatch(r'\d{6}',h),(p.name,h)
   assert not np.any(array<0),(p.name,h)
   codes.append(h);values.append(array);labels.setdefault(h,str(row[5] or ''))
  w.close();assert total is not None and len(codes)==len(set(codes))
  a=np.asarray(values);assert a.shape==(len(codes),248)
  mapped=classification.reindex(codes).copy()
  for c in ['Commodity_Class','BEC5_EndUse']:mapped[c]=mapped[c].fillna('unclassified')
  for k in GROUPS:mapped[k]=mapped[k].fillna(0)
  row=pd.DataFrame({'ISO3':iso,'Date':dates,flow:total});totals.append(row)
  # Preserve the exact product values, including explicit zeros and blanks.
  long=pd.DataFrame({'HS6':np.repeat(codes,len(dates)),'Date':np.tile(dates,len(codes)),
       'Value_USDk':a.ravel(),'ISO3':iso,'Flow':'Export' if flow.startswith('Exports') else 'Import'})
  csv(long,MID/'hs6'/f"{iso}_{'Export' if flow.startswith('Exports') else 'Import'}_Month.csv.gz")
  observed=np.nansum(a,axis=0);valid=np.isfinite(a).sum(axis=0)
  for i,date in enumerate(dates):
   audit.append({'ISO3':iso,'Flow':flow,'Date':date,'TOTAL_USDk':total[i],'HS6_Sum_USDk':observed[i],
    'Difference_USDk':observed[i]-total[i],'Difference_pct':100*(observed[i]-total[i])/total[i] if total[i] else np.nan,
    'Rounding_Bound_USDk':.5*(np.count_nonzero(a[:,i])+1),'Observed_HS6':int(valid[i])})
  for k in GROUPS:
   mask=mapped[k].eq(1).to_numpy();sub=a[mask];n=len(sub)
   val=np.nansum(sub,axis=0);count=np.isfinite(sub).sum(axis=0)
   val=np.where(count==n,val,np.nan) if n else np.zeros(248)
   groups.append(pd.DataFrame({'ISO3':iso,'Group':k,'Date':dates,flow:val}))
  for field in ['Commodity_Class','BEC5_EndUse']:
   for cls in sorted(mapped[field].unique()):
    mask=mapped[field].eq(cls).to_numpy();amount=float(np.nansum(a[mask]))
    coverage.append({'ISO3':iso,'Flow':flow,'Classification':field,'Class':cls,'HS6_Codes':int(mask.sum()),
      'Value_USDk_AllPeriods':amount,'Value_Share_pct':100*amount/float(np.nansum(a))})
  quality.append({'File':p.name,'ISO3':iso,'Flow':flow,'HS6_Codes':len(codes),'Rows':a.size,
    'Missing_Values':int(np.isnan(a).sum()),'Zero_Values':int((a==0).sum()),'First_Month':dates[0],'Last_Month':dates[-1]})
  print('IMPORTED',iso,flow,len(codes),'codes','missing',int(np.isnan(a).sum()),flush=True)
 tm=pd.concat(totals,ignore_index=True).groupby(['ISO3','Date'],as_index=False)[FIELDS].sum(min_count=1)
 gm=pd.concat(groups,ignore_index=True).groupby(['ISO3','Group','Date'],as_index=False)[FIELDS].sum(min_count=1)
 assert len(tm)==11*248 and len(gm)==11*7*248
 pm=pd.read_csv(MID/'macro/Macro_Country_Month.csv');pq=pd.read_csv(MID/'macro/Macro_Country_Quarter.csv')
 wq=pd.read_csv(MID/'macro/Macro_World_Quarter.csv')
 worldm=pm[pm.ISO3.eq('CHN')][['Date']+[c for c in pm if c.startswith(('IDN_','REER_','CPI_IDN_','CMD_','IDR_'))]].copy()
 worldm['ISO3']='WLD';macro_m=pd.concat([pm,worldm],ignore_index=True)
 # Update the foreign-demand weights using the new workbook TOTAL values.
 weights=tm[tm.ISO3.ne('WLD')&tm.Date.between('2006-01','2008-12')].groupby('ISO3').Exports_USDk.sum()
 weights=weights/weights.sum();csv(weights.rename('Export_Weight_2006_2008').reset_index(),MID/'Foreign_Demand_Weights.csv')
 z=pq.assign(weight=pq.ISO3.map(weights));z['weighted_activity']=z.weight*z.Partner_GDP_Real_Index_2015mean100
 demand=z.groupby('Quarter').weighted_activity.sum(min_count=10)
 wq['Foreign_Activity_Top10_FixedWeight_Index']=wq.Quarter.map(demand);wq['ISO3']='WLD'
 macro_q=pd.concat([pq,wq],ignore_index=True)
 totals_m=ratios(tm).merge(macro_m,on=['ISO3','Date'],how='left',validate='one_to_one')
 groups_m=ratios(gm).merge(macro_m,on=['ISO3','Date'],how='left',validate='many_to_one')
 totals_q=qaggregate(tm,['ISO3']).merge(macro_q,on=['ISO3','Quarter'],how='left',validate='one_to_one')
 groups_q=qaggregate(gm,['ISO3','Group']).merge(macro_q,on=['ISO3','Quarter'],how='left',validate='many_to_one')
 csv(totals_m,MID/'Trade_Total_Month.csv');csv(totals_q,MID/'Trade_Total_Quarter.csv')
 csv(groups_m,MID/'Trade_Goods_Month.csv');csv(groups_q,MID/'Trade_Goods_Quarter.csv')
 # Compatibility file used by the plotting engine; values now come from Trade Map.
 world=totals_q[totals_q.ISO3.eq('WLD')].rename(columns={c:'World_'+c for c in FIELDS+['Trade_Balance_USDk']})
 csv(world,MID/'Panel_World_Quarter.csv')
 csv(pd.DataFrame([{'HS6':k,'Product':v} for k,v in sorted(labels.items())]),MID/'HS6_Product_Lookup.csv')
 csv(pd.DataFrame(audit),D/'HS6_vs_TOTAL.csv');csv(pd.DataFrame(quality),D/'Workbook_Coverage.csv')
 csv(pd.DataFrame(coverage),D/'Classification_Coverage.csv')
 (D/'input_sha256.json').write_text(json.dumps(inputhash,indent=2),encoding='utf-8')
 info={'workbooks':22,'monthly_start':'2006-01','monthly_end':'2026-08','groups':GROUPS,
   'classification_policy':'Consensus across possible HS revisions; no automatic time-series harmonization',
   'BEC':'UNSD complete correlations 2022, BEC revision5; SNA end use from third code digit',
   'group_overlap':'BEC end-use categories overlap commodity categories; do not sum seven groups',
   'import_input_dependency':'excluded','original_inputs_unchanged':all(sha(RAW/n)==h for n,h in inputhash.items())}
 (D/'Data_Validation.json').write_text(json.dumps(info,indent=2,ensure_ascii=False),encoding='utf-8')
 print('HS6_DATA_BUILD_COMPLETE',flush=True)
if __name__=='__main__':main()
