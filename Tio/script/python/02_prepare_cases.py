"""Prepare contiguous ARDL/NARDL cases; import-input mechanism excluded."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
MID=ROOT/'intermediate';D=ROOT/'output/diagnostics/oskooee'
def longest(g,ok):
 best=[];run=[];prev=None
 for ix,valid in zip(g.index,ok):
  t=pd.Period(g.loc[ix,'Quarter'],freq='Q').ordinal
  if valid:
   run=run+[ix] if prev is not None and t==prev+1 else [ix]
   if len(run)>len(best):best=run.copy()
   prev=t
  else:run=[];prev=None
 return best
def main():
 D.mkdir(parents=True,exist_ok=True)
 p=pd.read_csv(MID/'Trade_Total_Quarter.csv');cg=pd.read_csv(MID/'Trade_Goods_Quarter.csv')
 groups=pd.read_csv(MID/'Goods_Groups.csv').set_index('Group').Label.to_dict()
 cases=[];registry=[]
 def add(code,label,scope,scenario,g,iso,group='',price=False,start=None,proxy=False,alt=False):
  g=g.sort_values('Quarter').copy()
  if start:g=g[g.Quarter.ge(start)].copy()
  world=iso=='WLD'
  z=pd.DataFrame({'Quarter':g.Quarter,'x':g.Exports_USDk,'m':g.Imports_USDk})
  z['y']=np.log(z.m.where(z.m.gt(0))/z.x.where(z.x.gt(0)))
  z['yd']=np.log(g.IDN_GDP_Real_Index_2015mean100)
  z['yf']=np.log(g.Foreign_Activity_Top10_FixedWeight_Index if world else g.Partner_GDP_Real_Index_2015mean100)
  rer=g.REER_BIS_broad if world else g['RER_With_WPI_Proxy_Index_2015mean100' if proxy else 'RER_Bilateral_Index_2015mean100']
  if alt:rer=g.RER_GEM
  z['q']=np.log(rer) if world else -np.log(rer)
  z['cp']=np.log(g.CMD_BCOM_Mean.where(g.CMD_BCOM_Mean.gt(0)))
  z['tb']=z.x-z.m
  need=['y','yd','yf','q']+(['cp'] if price else [])
  ix=longest(z,z[need].notna().all(axis=1));selected=z.loc[ix].copy();sid=len(registry)+1
  reg={'sid':sid,'series_id':code,'label':label,'scope':scope,'scenario':scenario,'ISO3':iso,'Group':group,
   'price_control':int(price),'uses_WPI':int(proxy),'N_contiguous':len(ix),
   'first_quarter':selected.Quarter.min() if len(ix) else '', 'last_quarter':selected.Quarter.max() if len(ix) else '',
   'excluded_incomplete_or_gap':len(z)-len(ix),'status':'ESTIMATE' if len(ix)>=48 else 'SHORT_SAMPLE_HOLD',
   'foreign_activity':'Top10 fixed-weight GDP proxy' if world else 'Partner real GDP',
   'q_orientation':'up=appreciation, NEG=depreciation',
   'source_caveats':'HS6 revision not declared; conservative consensus mapping; macro caveats retained; groups overlap'}
  registry.append(reg)
  if len(ix)>=48:
   for k,v in [('sid',sid),('series_id',code),('price_control',int(price)),('scope',scope),('scenario',scenario),('label',label)]:selected[k]=v
   cases.append(selected)
 add('WORLD','Indonesia - World','aggregate','main',p[p.ISO3.eq('WLD')],'WLD',start='2010Q1')
 add('WORLD_FULL','World: full 2006+ sensitivity','aggregate','world_2006_sensitivity',p[p.ISO3.eq('WLD')],'WLD')
 for iso,g in p[p.ISO3.ne('WLD')].groupby('ISO3',sort=True):add('BIL_'+iso,iso,'bilateral','main',g,iso)
 for (iso,group),g in cg.groupby(['ISO3','Group'],sort=True):
  start='2010Q1' if iso=='WLD' else None
  add('TYPE_'+iso+'_'+group,iso+' / '+groups[group],'goods','main',g,iso,group,start=start)
  add('PRICE_'+iso+'_'+group,iso+' / '+groups[group]+' + BCOM','goods','BCOM_control',g,iso,group,price=True,start=start)
 add('IND_WPI','IND: WPI proxy sensitivity','bilateral','WPI_proxy',p[p.ISO3.eq('IND')],'IND',proxy=True)
 fx=pd.read_csv(MID/'macro/FX_Bilateral_WBGEM_Alternative.csv')
 cpi=pd.read_csv(MID/'macro/FX_Bilateral_Monthly.csv')
 mm=fx.merge(cpi[['ISO3','Date','CPI_Index_2015mean100','CPI_IDN_Index_2015mean100']],on=['ISO3','Date'],validate='one_to_one')
 mm['Quarter']=pd.PeriodIndex(mm.Date,freq='M').asfreq('Q').astype(str)
 mm['RER_GEM']=mm.NER_IDR_per_PartnerCurrency_WBGEM*mm.CPI_Index_2015mean100/mm.CPI_IDN_Index_2015mean100
 aq=mm.groupby(['ISO3','Quarter']).RER_GEM.agg(['mean','count']).reset_index();aq['RER_GEM']=aq['mean'].where(aq['count'].eq(3))
 for iso in ['THA','VNM','KOR']:
  g=p[p.ISO3.eq(iso)].merge(aq[['ISO3','Quarter','RER_GEM']],on=['ISO3','Quarter'],validate='one_to_one')
  add('GEM_'+iso,iso+' GEM FX sensitivity','bilateral','GEM_FX',g,iso,alt=True)
 reg=pd.DataFrame(registry);data=pd.concat(cases,ignore_index=True)
 data['tq']=pd.PeriodIndex(data.Quarter,freq='Q').asi8-pd.Period('1960Q1',freq='Q').ordinal
 assert not data.duplicated(['sid','tq']).any()
 for _,g in data.groupby('sid'):
  assert (np.diff(g.tq)==1).all()
  np.testing.assert_allclose(g.y,np.log(g.m/g.x),atol=1e-12)
 reg.to_csv(D/'case_registry.csv',index=False)
 data.to_csv(MID/'Oskooee_Quarterly_Analysis.csv',index=False,float_format='%.15g')
 paths=[MID/n for n in ['Trade_Total_Quarter.csv','Trade_Goods_Quarter.csv','HS6_Classification.csv']]
 (D/'input_sha256.json').write_text(json.dumps({str(p.relative_to(MID)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2),encoding='utf-8')
 print(reg.groupby(['scope','scenario','status']).size().to_string(),flush=True)
 print('CASES_READY',len(reg),'eligible',int(reg.status.eq('ESTIMATE').sum()),flush=True)
if __name__=='__main__':main()
