"""Build an audited research presentation using the user's original PowerPoint master.

Run with the project's Python packages on PYTHONPATH. Input datasets are read only.
Rendering is a separate optional step through Microsoft PowerPoint (see script 18).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
from pathlib import Path
from zipfile import ZipFile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output' / 'presentation'
ASSETS = OUT / 'assets'
C = dict(brown='A5644E', dark='4E3B30', beige='F2E8E1', gold='C17529',
         ochre='F0A22E', gray='6B6B6B', light='EDEDED', ink='1A1A1A',
         grid='E5DFDA', white='FFFFFF', red='B23B2E', green='5E8C2A', blue='2F5D8C')
COUNTRIES = {'AUS':'Australia', 'CHN':'Tiongkok', 'IND':'India', 'JPN':'Jepang',
             'KOR':'Korea Selatan', 'MYS':'Malaysia', 'SGP':'Singapura',
             'THA':'Thailand', 'USA':'Amerika Serikat', 'VNM':'Vietnam'}
ISOS = list(COUNTRIES)
plt.rcParams.update({'font.family':'Arial', 'font.size':12, 'axes.labelsize':12,
                     'axes.titlesize':13, 'axes.titleweight':'bold',
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'axes.edgecolor':'#B8ACA3', 'axes.labelcolor':'#1A1A1A',
                     'xtick.color':'#6B6B6B', 'ytick.color':'#6B6B6B',
                     'figure.facecolor':'white', 'savefig.facecolor':'white'})

def rgb(key):
    return RGBColor.from_string(C.get(key, key))

def hexcolor(key):
    return '#' + C.get(key, key)

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def fmt(v, n=2):
    if pd.isna(v): return '—'
    return f'{float(v):,.{n}f}'.replace(',', '|').replace('.', ',').replace('|', '.')

def pval(v):
    if pd.isna(v): return '—'
    return '<0,001' if v < .001 else f'{v:.3f}'.replace('.', ',')

def savefig(fig, name):
    fig.savefig(ASSETS / f'{name}.png', dpi=220, bbox_inches='tight', pad_inches=.10)
    fig.savefig(ASSETS / f'{name}.pdf', bbox_inches='tight', pad_inches=.10)
    plt.close(fig)
    return ASSETS / f'{name}.png'

def style_axis(ax, grid='y'):
    ax.set_axisbelow(True)
    ax.grid(axis=grid, color=hexcolor('grid'), lw=.7)
    ax.spines[['top','right']].set_visible(False)

def box(slide, x,y,w,h, fill='beige', line=None):
    sh=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=rgb(fill)
    if line:
        sh.line.color.rgb=rgb(line); sh.line.width=Pt(.7)
    else: sh.line.fill.background()
    return sh

def text(slide, x,y,w,h, content, size=15, color='ink', bold=False,
         align=PP_ALIGN.LEFT, font='Arial', fill=None):
    sh=slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf=sh.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=Inches(.01); tf.margin_right=Inches(.01)
    tf.margin_top=Inches(.01); tf.margin_bottom=Inches(.01)
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb=rgb(fill)
    for i,line in enumerate(str(content).split('\n')):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.text=line; p.alignment=align; p.space_after=Pt(5)
        p.font.name=font; p.font.size=Pt(size); p.font.bold=bold; p.font.color.rgb=rgb(color)
    return sh

def picture(slide, path, x,y,w,h):
    with Image.open(path) as im: iw,ih=im.size
    scale=min(w/iw,h/ih); dw,dh=iw*scale,ih*scale
    return slide.shapes.add_picture(str(path), Inches(x+(w-dw)/2), Inches(y+(h-dh)/2),
                                    width=Inches(dw), height=Inches(dh))

def table(slide, headers, rows, x=.65,y=1.65,w=12.0,h=4.6,widths=None,size=12,emphasis=None):
    tb=slide.shapes.add_table(len(rows)+1,len(headers), Inches(x), Inches(y), Inches(w), Inches(h)).table
    if widths:
        for col,part in zip(tb.columns,widths): col.width=Inches(w*part/sum(widths))
    for i,row in enumerate([headers]+list(rows)):
        for j,val in enumerate(row):
            cell=tb.cell(i,j); cell.text=str(val)
            cell.margin_left=Inches(.09);cell.margin_right=Inches(.07)
            cell.margin_top=Inches(.05);cell.margin_bottom=Inches(.04)
            cell.vertical_anchor=MSO_ANCHOR.MIDDLE
            cell.fill.solid();cell.fill.fore_color.rgb=rgb('brown' if i==0 else ('beige' if i%2 else 'white'))
            for p in cell.text_frame.paragraphs:
                p.font.name='Arial';p.font.size=Pt(size);p.font.bold=(i==0)
                p.font.color.rgb=rgb('white' if i==0 else 'ink');p.space_after=Pt(0)
                p.alignment=PP_ALIGN.LEFT if j==0 else PP_ALIGN.CENTER
            pr=cell._tc.get_or_add_tcPr()
            for edge in ['lnL','lnR','lnT','lnB']:
                el=OxmlElement('a:'+edge);el.set('w','6350')
                fill=OxmlElement('a:solidFill');co=OxmlElement('a:srgbClr');co.set('val','FFFFFF')
                fill.append(co);el.append(fill);pr.append(el)
    return tb

class Deck:
    def __init__(self, template):
        self.p=Presentation(str(template));self.slides=[]
        ids=self.p.slides._sldIdLst
        for sid in list(ids)[1:]:
            self.p.part.drop_rel(sid.rId);ids.remove(sid)
        # Original section lists refer to slides that have been removed.
        for el in list(self.p._element):
            if el.tag.split('}')[-1] in ['sectionLst','custShowLst']:
                self.p._element.remove(el)
        for ext in self.p._element.xpath('./p:extLst'):
            for child in list(ext):
                if any(node.tag.split('}')[-1]=='sectionLst' for node in child.iter()):
                    ext.remove(child)
        self.p.core_properties.title='Depresiasi Rupiah dan Neraca Perdagangan Indonesia'
        self.p.core_properties.subject='Hasil estimasi awal ARDL dan NARDL, 17 November 2026'
        self.p.core_properties.author='Tio'
        self.p.core_properties.keywords='Indonesia, trade balance, ARDL, NARDL, komoditas'
        self.p.core_properties.comments='Template visual berasal dari benchmark pengguna; isi penelitian dihitung dari keluaran lokal.'

    def notes(self, s, title, body, sources):
        note=f'{title}\n\n{body}\n\nSUMBER DAN REPRODUKSI\n{sources}\n\nVersi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.'
        s.notes_slide.notes_text_frame.text=note
        self.slides.append({'slide':len(self.slides)+1,'title':title,'notes':note})

    def cover(self):
        s=self.p.slides[0]
        title=s.shapes.title
        title.text='Depresiasi Rupiah dan\nNeraca Perdagangan Indonesia'
        for p in title.text_frame.paragraphs:
            p.font.name='Arial Nova';p.font.size=Pt(24);p.font.bold=True
            p.font.color.rgb=rgb('white');p.alignment=PP_ALIGN.CENTER
        sub=s.placeholders[1]
        sub.left=Inches(2.55);sub.top=Inches(5.48)
        sub.width=Inches(8.55);sub.height=Inches(.92)
        sub.text='ARDL–NARDL: agregat, 10 mitra, dan jenis barang\n17 November 2026 | Hasil estimasi awal'
        for p in sub.text_frame.paragraphs:
            p.font.name='Arial Nova';p.font.size=Pt(15);p.font.bold=True
            p.font.color.rgb=rgb('white');p.alignment=PP_ALIGN.CENTER
        self.notes(s,'Depresiasi Rupiah dan Neraca Perdagangan Indonesia',
            'Deck membahas bukti awal dan batas interpretasinya. Identitas visual, foto cover, logo, master, layout dan tema mengikuti benchmark pengguna. Penyusunan isi: proyek Tio; bukan klaim pengesahan institusional.',
            'notes/hasil_ardl_nardl_hs6.md; template PPT benchmark pengguna.')
        return s

    def slide(self,title,subtitle='',source='Hasil estimasi Stata dan pengolahan dataset proyek Tio.',notes=''):
        s=self.p.slides.add_slide(self.p.slide_layouts[4])
        title_sh=s.shapes.title;title_sh.text=title;title_sh.text_frame.word_wrap=True
        title_sh.left=Inches(.70);title_sh.top=Inches(.37)
        title_sh.width=Inches(11.4);title_sh.height=Inches(.69)
        for p in title_sh.text_frame.paragraphs:
            p.font.name='Arial';p.font.size=Pt(18);p.font.bold=True;p.font.color.rgb=rgb('ink')
        if subtitle: text(s,.66,1.19,12.0,.34,subtitle,11.5,'gray')
        # Page number is provided by the original layout's slide-number field.
        text(s,.67,7.15,11.90,.25,source,8.0,'gray')
        # The benchmark folio box fits two digits. Overlay a same-color folio
        # for three-digit appendix pages while preserving all original masters.
        if len(self.p.slides)>=100:
            box(s,12.9333,7.105,0.4,0.395,'91581F')
            folio=text(s,12.9433,7.15,0.38,0.26,str(len(self.p.slides)),8,'white',True,PP_ALIGN.CENTER)
            folio.name='Three-digit folio'
            folio.text_frame.word_wrap=False
            folio.text_frame.vertical_anchor=MSO_ANCHOR.MIDDLE
        self.notes(s,title,notes,source)
        return s

    def divider(self):
        s=self.p.slides.add_slide(self.p.slide_layouts[0])
        s.shapes.title.text='Lampiran'
        s.placeholders[1].text='Hasil lengkap, diagnostik, definisi, dan sumber data'
        self.notes(s,'Lampiran','Rincian untuk pemeriksaan dan reproduksi hasil.','Output model dan manifest sumber di proyek Tio.')
        return s

def callout(s,content,y=6.35,color='beige',size=13):
    box(s,.68,y,11.96,.52,color)
    text(s,.84,y+.07,11.62,.40,content,size,'dark',True)

def cards(s, items,y=1.65,h=1.42):
    n=len(items);gap=.24;w=(12-gap*(n-1))/n
    for i,(big,label,desc) in enumerate(items):
        x=.67+i*(w+gap);box(s,x,y,w,h,'beige')
        text(s,x+.16,y+.10,w-.32,.52,big,28,'brown',True)
        text(s,x+.16,y+.67,w-.32,.30,label,14,'ink',True)
        text(s,x+.16,y+1.04,w-.32,.34,desc,10.5,'gray')

def steps(s, items, y=1.75, spacing=.95, x=.75, w=11.8):
    for i,(title,body) in enumerate(items):
        yy=y+i*spacing
        sh=s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(yy), Inches(.35), Inches(.35))
        sh.fill.solid();sh.fill.fore_color.rgb=rgb('brown');sh.line.fill.background()
        text(s,x+.03,yy+.02,.29,.25,str(i+1),12,'white',True,PP_ALIGN.CENTER)
        text(s,x+.52,yy-.02,w-.52,.35,title,15,'dark',True)
        text(s,x+.52,yy+.38,w-.65,spacing-.43,body,13,'ink')

