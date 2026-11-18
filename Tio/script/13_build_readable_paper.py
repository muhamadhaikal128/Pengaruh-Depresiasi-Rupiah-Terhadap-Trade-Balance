"""Build a plain-language edition of the existing paper without re-estimation."""
from pathlib import Path
import importlib.util,json,hashlib,re,subprocess,shutil,ast
import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'output/paper';OUT=OLD/'bahasa_mudah'
for p in [OUT,OUT/'sections',OUT/'assets',OUT/'tables']:p.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('paper_base',ROOT/'script/12_build_research_paper.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
def response(ax,r,title=None):
 z=base.DM[base.DM.model_id.eq(r.model_id)].copy();assert len(z)==50
 for direction,label,co in [('depreciation','Rupiah melemah','brown'),('appreciation','Rupiah menguat','blue')]:
  q=z[z.direction.eq(direction)].sort_values('horizon_quarters')
  ax.plot(q.horizon_quarters,-q.effect_logpoints,color=base.COL[co],lw=1.65,label=label)
  ax.fill_between(q.horizon_quarters,-q.upper95_logpoints,-q.lower95_logpoints,color=base.COL[co],alpha=.14,lw=0)
 if title and ' | ' in title:
  status='hubungan jangka panjang belum cukup jelas' if base.status(r)=='--' else 'lolos pemeriksaan model' if base.status(r)=='L+D' else 'ada catatan diagnostic tests'
  title=r.estimator+' | '+status
 ax.axhline(0,color=base.COL['gray'],lw=.65)
 ax.set_xlim(0,24);ax.set_xticks([0,4,8,12,16,20,24])
 ax.set_xlabel('Kuartal setelah kurs berubah',fontsize=9)
 ax.set_ylabel(r'$100\,\Delta\ln(X/M)$',fontsize=11)
 ax.set_title((title or r.estimator).replace('--','–'),loc='left',fontsize=9.3,fontweight='bold')
 ax.legend(frameon=False,ncol=2,fontsize=8,loc='best');base.grid(ax)
def clean_risk(r):
 a=[]
 if r.Bounds5!='Reject no-level relation':a.append('bounds test belum memberi bukti yang cukup')
 if not base.pd.isna(r.lr_x_p) and r.lr_x_p>=.05:a.append('joint-X test belum mendukung')
 if r.I2_not_ruled_out:a.append('ada catatan pada unit root tests')
 if not r.Dynamic_stable:a.append('respons dinamis belum stabil')
 if r.df_r<15:a.append('sisa informasi untuk mengestimasi error terlalu sedikit')
 if not r.Diagnostic_clean5:a.append('ada catatan pada residual atau stabilitas model')
 return '; '.join(a) or 'tidak ada masalah yang terdeteksi pada pemeriksaan yang dipakai'
def figures():
 base.OUT=OUT;base.A=OUT/'assets';base.TB=OUT/'tables'
 base.response=response
 import logging
 logging.getLogger('fontTools').setLevel(logging.ERROR)
 base.figs()
def compile_validate():
 report0=json.loads((OLD/'paper_validation.json').read_text('utf-8'))
 before={name:sha(ROOT/name) for name in report0['input_sha256']}
 assert before==report0['input_sha256'],'Estimation outputs changed since the source paper'
 old_pdf_digest=sha(OLD/'Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio.pdf')
 table_before={p.name:sha(p) for p in (OLD/'tables').glob('*.tex')}
 for p in (OLD/'tables').glob('*.tex'):shutil.copy2(p,OUT/'tables'/p.name)
 shutil.copy2(OLD/'numbers.tex',OUT/'numbers.tex')
 # Plot data and estimates are unchanged; only presentation wording changes.
 if __import__('os').environ.get('READABLE_TEXT_ONLY')!='1':figures()
 else:assert (OUT/'assets/response_WORLD.pdf').exists()
 exe='C:/Users/Administrator/AppData/Roaming/TinyTeX/bin/windows/pdflatex.exe'
 for n in range(3):
  result=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','-no-shell-escape','paper.tex'],
    cwd=OUT,capture_output=True,text=True,encoding='utf-8',errors='replace')
  (OUT/f'compile_{n+1}.txt').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
  if result.returncode:raise RuntimeError('See '+str(OUT/f'compile_{n+1}.txt'))
 target=OLD/'Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio_Bahasa_Mudah.pdf'
 shutil.copy2(OUT/'paper.pdf',target)
 assert all(sha(OUT/'tables'/name)==digest for name,digest in table_before.items())
 assert sha(OLD/'numbers.tex')==sha(OUT/'numbers.tex')
 after={name:sha(ROOT/name) for name in before};assert before==after
 doc=fitz.open(target);text='\n'.join(p.get_text() for p in doc)
 assert '??' not in text and 'TODO' not in text
 log=(OUT/'paper.log').read_text('utf-8',errors='replace')
 bad=[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line.lower() or 'LaTeX Error' in line]
 outside=[]
 for i,page in enumerate(doc,1):
  for block in page.get_text('dict')['blocks']:
   if 'lines' in block:
    x0,y0,x1,y1=block['bbox']
    if x0<15 or y0<12 or x1>page.rect.width-15 or y1>page.rect.height-12:outside.append(i)
 pv=OUT/'previews';pv.mkdir(exist_ok=True)
 for i,page in enumerate(doc):
  page.get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False).save(pv/f'page_{i+1:03d}.png')
 try:font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)
 except OSError:font=ImageFont.load_default()
 for start in range(0,len(doc),12):
  sheet=Image.new('RGB',(920,1030),'#EDEDED');d=ImageDraw.Draw(sheet)
  for k,i in enumerate(range(start,min(start+12,len(doc)))):
   with Image.open(pv/f'page_{i+1:03d}.png') as im:
    im.thumbnail((210,300));thumb=im.convert('RGB').copy()
   x=15+(k%4)*225;y=10+(k//4)*340
   sheet.paste(thumb,(x,y));d.text((x+3,y+307),str(i+1),fill='#4E3B30',font=font)
  sheet.save(OUT/f'contact_{start//12+1:02d}.png')
 (OUT/'paper_text.txt').write_text(text,encoding='utf-8')
 report={'status':'PASS' if not bad and not outside else 'REVIEW_REQUIRED',
 'pdf':target.name,'pages':len(doc),'language_revision_date':'2026-11-18','estimation_date':'2026-11-17',
 'estimation_inputs_unchanged':before==after,'numeric_tables_byte_identical':True,'numeric_macros_byte_identical':True,
 'primary_models':176,'sensitivity_models':340,'reestimated':False,
 'overfull_or_reference_errors':bad,'text_outside_margins':outside,
 'source_pdf_preserved':sha(OLD/'Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio.pdf')==old_pdf_digest,
 'pdf_sha256':sha(target),'input_sha256':before}
 (OUT/'validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
 (OUT/'README.md').write_text('# Paper dengan bahasa lebih mudah\n\nBuka ../'+target.name+
 '\n\nRevisi bahasa 18 November 2026. Hasil estimasi tetap run 17 November 2026. Angka tabel dan rumus angka disalin identik; seluruh 516 estimasi tetap tersedia. Narasi menjelaskan istilah seperti long-run relationship, confidence interval, p-value dan diagnostic tests dengan contoh sederhana. Sumber LaTeX dalam folder ini dapat diedit. Reproduksi melalui script/13_build_readable_paper.py.\n',encoding='utf-8')
 print(json.dumps({k:report[k] for k in ['status','pages','numeric_tables_byte_identical','estimation_inputs_unchanged','overfull_or_reference_errors']},indent=2),flush=True)
 doc.close()
if __name__=='__main__':compile_validate()
