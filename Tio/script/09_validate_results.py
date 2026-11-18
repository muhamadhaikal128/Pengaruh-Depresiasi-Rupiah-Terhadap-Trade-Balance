from pathlib import Path
import json,hashlib
import pandas as pd
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def main():
 T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee'
 s=pd.read_csv(T/'results_primary_models.csv');a=pd.read_csv(T/'results_all_models.csv')
 reg=pd.read_csv(D/'case_registry.csv');report=json.loads((D/'analysis_validation_report.json').read_text('utf-8'))
 unavailable=a[a.Bounds5.eq('Unavailable')][['model_id','N','df_r','lag_order']].copy()
 unavailable['Estimated_Parameters']=unavailable.N-unavailable.df_r
 expected=int(reg.status.eq('ESTIMATE').sum()*2+(reg.scenario.eq('main')&reg.status.eq('ESTIMATE')).sum()*2)
 assert len(a)==expected and report['status']=='PASS'
 required=[]
 for model in s.model_id:
  for suffix in ['multipliers','stability','residuals']:
   for extension in ['png','pdf']:required.append(ROOT/'output/figures/oskooee'/f'{model}_{suffix}.{extension}')
  for extension in ['png','pdf']:required.append(T/f'{model}_coefficients.{extension}')
  for suffix in ['cusum','cusumsq','multipliers','residuals']:required.append(ROOT/'output/gph/oskooee'/f'{model}_{suffix}.gph')
 for iso in sorted(s[s.scope.eq('goods')].ISO3.unique()):
  for est in ['ARDL','NARDL']:
   for extension in ['png','pdf']:required.append(ROOT/'output/figures/oskooee'/f'forest_{iso}_{est}_goods.{extension}')
   required.append(ROOT/'output/gph/oskooee'/f'forest_{iso}_{est}_goods.gph')
 for p in required:assert p.is_file() and p.stat().st_size>0,p
 imgs=list(T.glob('*.png'))+list((ROOT/'output/figures/oskooee').glob('*.png'))
 for p in imgs:
  with Image.open(p) as im:im.verify()
 # Test unavailability is reported separately from failed coefficient estimation.
 from openpyxl import load_workbook
 from openpyxl.utils.dataframe import dataframe_to_rows
 wb=load_workbook(T/'Oskooee_Results.xlsx')
 if 'Bounds_unavailable' in wb:del wb['Bounds_unavailable']
 ws=wb.create_sheet('Bounds_unavailable')
 for row in dataframe_to_rows(unavailable.astype(object).where(pd.notna(unavailable),None),index=False,header=True):ws.append(row)
 ws.freeze_panes='B2';ws.auto_filter.ref=ws.dimensions
 wb.save(T/'Oskooee_Results.xlsx');wb.close()
 note=ROOT/'notes/hasil_ardl_nardl_hs6.md'
 content=note.read_text(encoding='utf-8')
 marker='\n## Bounds finite-sample yang tidak tersedia\n'
 if marker in content:content=content.split(marker)[0]
 if len(unavailable):
  content+=marker+'\nKoefisien tetap diestimasi, tetapi critical values bounds finite-sample tidak tersedia pada sensitivitas berikut karena N terlalu kecil relatif terhadap jumlah parameter. Statusnya Unavailable; hasil ini tidak dipakai sebagai dukungan hubungan level.\n\n'
  content+='| Model | N | Parameter | Lag |\n|---|---:|---:|---|\n'
  for row in unavailable.itertuples():content+=f'| {row.model_id} | {int(row.N)} | {int(row.Estimated_Parameters)} | {row.lag_order} |\n'
 content+='\nPerdagangan bernilai nominal dan belum disesuaikan musiman. Run ini menguji arah/level kurs; tidak ada variabel volatilitas kurs terpisah.\n'
 note.write_text(content,encoding='utf-8')
 manifest=json.loads((ROOT/'input/raw/trademap_hs6_20261117/source_manifest.json').read_text('utf-8'))
 assert len(manifest['files'])==22
 for r in manifest['files']:
  assert hashlib.sha256((ROOT/'input/raw/trademap_hs6_20261117'/r['filename']).read_bytes()).hexdigest()==r['sha256']
 provenance=json.loads((ROOT/'output/diagnostics/data/Classification_Macro_Provenance_SHA256.json').read_text('utf-8'))
 for filename,digest in provenance.items():assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest,filename
 cross=pd.read_csv(D/'CUSUM_cross_implementation_check.csv')
 assert cross.official_path_reproduces_stored_statistic.all()
 assert cross.loc[cross.independent_check_applicable,'difference'].max()<2e-5
 recursive_exceptions=cross.loc[~cross.independent_check_applicable,'model_id'].tolist()
 report['official_Stata_CUSUM_paths_verified']=len(cross)
 report['independent_CUSUM_initialization_exceptions']=recursive_exceptions
 (D/'analysis_validation_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 tables=ROOT/'output/tables/data';tables.mkdir(parents=True,exist_ok=True)
 with pd.ExcelWriter(tables/'HS6_Data_Audit.xlsx',engine='openpyxl') as wr:
  for name,file in [('Workbook_coverage','Workbook_Coverage.csv'),('HS6_vs_TOTAL','HS6_vs_TOTAL.csv'),('Classification_coverage','Classification_Coverage.csv')]:
   pd.read_csv(ROOT/'output/diagnostics/data'/file).to_excel(wr,sheet_name=name,index=False)
  pd.read_csv(ROOT/'intermediate/HS6_Classification.csv',dtype={'HS6':str}).to_excel(wr,sheet_name='HS6_classification',index=False)
  pd.read_csv(ROOT/'intermediate/Goods_Groups.csv').to_excel(wr,sheet_name='Goods_groups',index=False)
  yearly=ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv'
  if yearly.exists():pd.read_csv(yearly).to_excel(wr,sheet_name='Classification_by_year',index=False)
 arc=ROOT/'archive/v1_20261117_before_hs6_rebuild'
 files={str(p.relative_to(arc)):p.stat().st_size for p in arc.rglob('*') if p.is_file() and p.name not in ['archive_manifest.json','README_ARCHIVE.md']}
 (arc/'archive_manifest.json').write_text(json.dumps({'files':len(files),'bytes':sum(files.values()),'file_sizes':files,'credential_archived':False},indent=2),encoding='utf-8')
 result={'status':'PASS','models':len(a),'primary':len(s),'sensitivity':len(a)-len(s),
  'required_artifacts_checked':len(required),'png_files_verified':len(imgs),'raw_workbooks_hash_verified':22,
  'finite_sample_bounds_unavailable':unavailable.model_id.tolist(),
  'official_Stata_CUSUM_paths_verified':len(cross),'independent_CUSUM_initialization_exceptions':recursive_exceptions,
  'classification_macro_provenance_hashes_verified':len(provenance),
  'stata_do_files':[p.name for p in sorted((ROOT/'script').glob('*.do'))],
  'archive':str(arc),'archive_files':len(files),'import_input_dependency':'EXCLUDED',
  'group_classification':'7 overlapping HS6/BEC5 groups, world and ten partners',
  'HS_revision_limitation':'Workbook revision not declared; conservative consensus across official correspondences'}
 (D/'delivery_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
