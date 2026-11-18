"""Render the generated deck in Microsoft PowerPoint and validate the delivered files."""
import hashlib
import json
import os
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/presentation'
os.environ.setdefault('TEMP',str(ROOT.drive+'\\temp'))
os.environ.setdefault('TMP',str(ROOT.drive+'\\temp'))

import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
import win32com.client

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    pptx=OUT/'Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pptx'
    pdf=pptx.with_suffix('.pdf')
    slides=OUT/'slides';slides.mkdir(exist_ok=True)
    original_hash=sha(pptx)
    app=win32com.client.DispatchEx('PowerPoint.Application')
    pres=None;overflows=[];count=0
    try:
        pres=app.Presentations.Open(str(pptx),ReadOnly=True,Untitled=False,WithWindow=False)
        count=pres.Slides.Count
        for i in range(1,count+1):
            s=pres.Slides(i)
            s.Export(str(slides/f'slide_{i:02d}.png'),'PNG',1600,900)
            for j in range(1,s.Shapes.Count+1):
                sh=s.Shapes(j)
                if sh.HasTable:
                    for row in range(1,sh.Table.Rows.Count+1):
                        for col in range(1,sh.Table.Columns.Count+1):
                            cell=sh.Table.Cell(row,col).Shape
                            tf=cell.TextFrame2
                            available=cell.Height-tf.MarginTop-tf.MarginBottom
                            bound=tf.TextRange.BoundHeight
                            if bound>available+3:
                                overflows.append({'slide':i,'shape':sh.Name,'cell':[row,col],
                                    'text':cell.TextFrame.TextRange.Text[:150],
                                    'bound_height_pt':round(bound,2),'available_pt':round(available,2)})
                if sh.HasTextFrame and sh.TextFrame.HasText:
                    tf=sh.TextFrame2
                    available=sh.Height-tf.MarginTop-tf.MarginBottom
                    bound=tf.TextRange.BoundHeight
                    if bound>available+3:
                        overflows.append({'slide':i,'shape':sh.Name,'text':sh.TextFrame.TextRange.Text[:150],
                                          'bound_height_pt':round(bound,2),'available_pt':round(available,2)})
        pres.SaveAs(str(pdf),32)
    finally:
        if pres is not None:pres.Close()
        # PowerPoint may reuse an existing COM server. Leave other documents open.
        if app.Presentations.Count==0:app.Quit()
    assert sha(pptx)==original_hash,'Rendering changed PPTX'
    doc=fitz.open(pdf)
    assert len(doc)==count
    fonts=sorted({f[3] for p in doc for f in p.get_fonts()})
    pdftext='\n'.join(p.get_text() for p in doc)
    assert '2011Q1' in pdftext and '2026Q1' in pdftext
    previews=[]
    try:label_font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
    except OSError:label_font=ImageFont.load_default()
    for start in range(0,count,12):
        page_images=[]
        for i in range(start,min(start+12,count)):
            with Image.open(slides/f'slide_{i+1:02d}.png') as im:
                im.thumbnail((400,225));thumb=im.convert('RGB').copy()
            page_images.append((i+1,thumb))
        sheet=Image.new('RGB',(4*420+20,3*264+20),'#EDEDED');draw=ImageDraw.Draw(sheet)
        for k,(n,thumb) in enumerate(page_images):
            x=20+(k%4)*420;y=20+(k//4)*264
            sheet.paste(thumb,(x,y));draw.text((x+4,y+231),f'{n:02d}',fill='#4E3B30',font=label_font)
        p=OUT/f'preview_{start//12+1:02d}.png';sheet.save(p);previews.append(p.name)
    report_path=OUT/'deck_validation.json'
    report=json.loads(report_path.read_text(encoding='utf-8'))
    report.update({'render_validation':'completed','powerpoint_rendered_slides':count,
        'pdf_pages':len(doc),'pdf_sha256':sha(pdf),'pdf_fonts':fonts,
        'slide_png_count':len(list(slides.glob('slide_*.png'))),
        'text_height_overflow_candidates':overflows,'preview_files':previews})
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    doc.close()
    print(json.dumps({k:report[k] for k in ['render_validation','powerpoint_rendered_slides','pdf_pages','pdf_fonts','text_height_overflow_candidates']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
