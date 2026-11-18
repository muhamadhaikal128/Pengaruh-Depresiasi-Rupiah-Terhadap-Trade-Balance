"""Render both HS6 decks in PowerPoint, inspect text bounds, and export PDF/PNG."""
from pathlib import Path
import json,hashlib,os,time
from zipfile import ZipFile
import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
import win32com.client
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'output/presentation'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text_bounds(shape,slide,record,cell=None):
 if not shape.HasTextFrame or not shape.TextFrame.HasText:return
 tf=shape.TextFrame2
 available_h=shape.Height-tf.MarginTop-tf.MarginBottom
 available_w=shape.Width-tf.MarginLeft-tf.MarginRight
 h=tf.TextRange.BoundHeight;w=tf.TextRange.BoundWidth
 if h>available_h+3 or w>available_w+4:
  record.append({'slide':slide,'shape':shape.Name,'cell':cell,'text':shape.TextFrame.TextRange.Text[:180],
   'height':round(h,2),'available_height':round(available_h,2),'width':round(w,2),'available_width':round(available_w,2)})
def main():
 report_path=OUT/'deck_validation.json';report=json.loads(report_path.read_text('utf-8'))
 before=report['pptx_sha256'];rendered={};overflows=[]
 app=win32com.client.DispatchEx('PowerPoint.Application')
 try:
  for key in ['main_pptx','full_pptx']:
   path=OUT/report['files'][key];pres=None
   try:
    pres=app.Presentations.Open(str(path),ReadOnly=True,Untitled=False,WithWindow=False)
    count=pres.Slides.Count;local=[]
    slides=OUT/('slides_main' if key=='main_pptx' else 'slides_full');slides.mkdir(exist_ok=True)
    for i in range(1,count+1):
     slide=pres.Slides(i)
     # Export every full-deck page; main pages get their own copies for the presentation version.
     changed={int(v) for v in os.environ.get('PPT_CHANGED_SLIDES','').split(',') if v}
     png=slides/f'slide_{i:03d}.png'
     if not changed or i in changed or not png.exists():slide.Export(str(png),'PNG',1600,900)
     for j in range(1,slide.Shapes.Count+1):
      sh=slide.Shapes(j)
      if sh.HasTable:
       for row in range(1,sh.Table.Rows.Count+1):
        for col in range(1,sh.Table.Columns.Count+1):
         text_bounds(sh.Table.Cell(row,col).Shape,i,local,[row,col])
      else:text_bounds(sh,i,local)
     if i%20==0:print('RENDERED',key,i,'/',count,flush=True)
    pdf=path.with_suffix('.pdf');pres.SaveAs(str(pdf),32)
    pres.Close();pres=None
    assert sha(path)==before[path.name],'Rendering modified source deck'
    doc=fitz.open(pdf);assert len(doc)==count
    text='\n'.join(p.get_text() for p in doc)
    assert '2011Q1' in text and '2026Q1' in text
    fonts=sorted({f[3] for page in doc for f in page.get_fonts()})
    rendered[key]={'slides':count,'pdf':pdf.name,'pdf_pages':len(doc),'pdf_sha256':sha(pdf),
     'png_directory':slides.name,'png_count':len(list(slides.glob('slide_*.png'))),'fonts':fonts,'text_overflows':local}
    overflows.extend(dict(deck=key,**v) for v in local)
    doc.close()
   finally:
    if pres is not None:pres.Close()
 finally:
  if app.Presentations.Count==0:app.Quit()
 try:font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',16)
 except OSError:font=ImageFont.load_default()
 previews=[]
 for key,r in rendered.items():
  directory=OUT/r['png_directory'];prefix='main' if key=='main_pptx' else 'full'
  for start in range(0,r['slides'],12):
   sheet=Image.new('RGB',(1700,825),'#EDEDED');draw=ImageDraw.Draw(sheet)
   for n in range(start,min(start+12,r['slides'])):
    with Image.open(directory/f'slide_{n+1:03d}.png') as im:
     im.thumbnail((400,225));thumb=im.convert('RGB').copy()
    j=n-start;x=20+(j%4)*420;y=15+(j//4)*270
    sheet.paste(thumb,(x,y));draw.text((x+3,y+231),str(n+1).zfill(3),fill='#4E3B30',font=font)
   p=OUT/f'preview_{prefix}_{start//12+1:02d}.png';sheet.save(p);previews.append(p.name)
 # Source and math embedding integrity.
 for name,digest in report['input_sha256'].items():assert sha(ROOT/name)==digest,name
 for key in ['main_pptx','full_pptx']:
  with ZipFile(OUT/report['files'][key]) as z:
   assert any(n.startswith('ppt/media/latex_') and n.endswith('.svg') for n in z.namelist())
 report.update({'status':'PASS' if not overflows else 'RENDERED_REVIEW_REQUIRED',
  'rendered':rendered,'text_overflow_candidates':overflows,'previews':previews,
  'pptx_unchanged_by_render':True,'input_files_unchanged_after_render':True})
 report_path.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps({'status':report['status'],'main_slides':report['main_slides'],'full_slides':report['full_slides'],
  'overflow_candidates':overflows,'input_files_unchanged':True},ensure_ascii=False,indent=2),flush=True)
if __name__=='__main__':main()
