"""Audit changing classification coverage without changing any model inputs."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
def main():
 mid=ROOT/'intermediate';cl=pd.read_csv(mid/'HS6_Classification.csv',dtype={'HS6':str}).set_index('HS6')
 parts=[]
 for path in sorted((mid/'hs6').glob('*_Month.csv.gz')):
  iso,flow,_=path.name.split('_',2)
  for d in pd.read_csv(path,usecols=['HS6','Date','Value_USDk'],dtype={'HS6':str},chunksize=300000):
   d['Year']=d.Date.str[:4].astype(int)
   for kind in ['Commodity_Class','BEC5_EndUse']:
    d['Class']=d.HS6.map(cl[kind]).fillna('unclassified')
    g=d.groupby(['Year','Class'],as_index=False).Value_USDk.sum(min_count=1)
    g['ISO3']=iso;g['Flow']=flow;g['Classification']=kind;parts.append(g)
 out=pd.concat(parts,ignore_index=True).groupby(['ISO3','Flow','Year','Classification','Class'],as_index=False).Value_USDk.sum(min_count=1)
 totals=out.groupby(['ISO3','Flow','Year','Classification']).Value_USDk.transform('sum')
 out['Value_Share_pct']=100*out.Value_USDk/totals
 target=ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv';out.to_csv(target,index=False,float_format='%.12g')
 print('TEMPORAL_CLASSIFICATION_AUDIT_COMPLETE',len(out),flush=True)
if __name__=='__main__':main()
