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

ROOT = Path(__file__).resolve().parents[1]
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
            'notes/hasil_ardl_nardl_oskooee.md; template PPT benchmark pengguna.')
        return s

    def slide(self,title,subtitle='',source='Hasil estimasi Stata dan pengolahan dataset proyek Tio.',notes=''):
        s=self.p.slides.add_slide(self.p.slide_layouts[4])
        title_sh=s.shapes.title;title_sh.text=title
        title_sh.left=Inches(.70);title_sh.top=Inches(.37)
        title_sh.width=Inches(11.4);title_sh.height=Inches(.69)
        for p in title_sh.text_frame.paragraphs:
            p.font.name='Arial';p.font.size=Pt(18);p.font.bold=True;p.font.color.rgb=rgb('ink')
        if subtitle: text(s,.66,1.19,12.0,.34,subtitle,11.5,'gray')
        # Page number is provided by the original layout's slide-number field.
        text(s,.67,7.15,11.90,.25,source,8.0,'gray')
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

def prepare_assets(primary, allmodels, world, country, goods, analysis):
    assets={};exports={}
    # Annual merchandise flows: only complete years are included.
    w=world.copy();w['Year']=w.Quarter.str[:4].astype(int)
    flowcols=['World_Exports_USDk','World_Imports_USDk','World_Trade_Balance_USDk']
    annual=w.groupby('Year')[flowcols].sum(min_count=4).loc[2010:2025]/1e6
    annual.to_csv(ASSETS/'descriptive_world_annual_USDbn.csv')
    exports['world_2025']=annual.loc[2025].to_dict()
    fig,ax=plt.subplots(figsize=(11,3.45))
    ax.plot(annual.index,annual.World_Exports_USDk,color=hexcolor('brown'),lw=2.5,label='Ekspor')
    ax.plot(annual.index,annual.World_Imports_USDk,color=hexcolor('dark'),lw=2.2,label='Impor')
    ax.set_ylabel('USD miliar per tahun');ax.set_xticks([2010,2013,2016,2019,2022,2025]);style_axis(ax)
    ax.legend(loc='upper left',frameon=False,ncol=2)
    assets['world']=savefig(fig,'world_exports_imports')

    c=country[country.Quarter.str.startswith('2025')].groupby('ISO3')[['Exports_USDk','Imports_USDk']].sum(min_count=4)/1e6
    c=c.sort_values('Exports_USDk');c['Export_Share_Within10']=c.Exports_USDk/c.Exports_USDk.sum()*100
    c.to_csv(ASSETS/'descriptive_partner_2025_USDbn.csv')
    fig,axes=plt.subplots(1,2,figsize=(11.8,4.1),gridspec_kw={'width_ratios':[1.25,1]})
    ypos=np.arange(len(c));axes[0].barh(ypos+.17,c.Exports_USDk,.32,color=hexcolor('brown'),label='Ekspor')
    axes[0].barh(ypos-.17,c.Imports_USDk,.32,color=hexcolor('dark'),label='Impor')
    axes[0].set_yticks(ypos,[COUNTRIES[i] for i in c.index]);axes[0].set_xlabel('USD miliar, tahun 2025');style_axis(axes[0],'x')
    axes[0].legend(frameon=False,loc='lower right',fontsize=10)
    axes[1].barh(ypos,c.Export_Share_Within10,color=hexcolor('brown'))
    axes[1].set_yticks(ypos,c.index);axes[1].set_xlabel('Pangsa ekspor dalam 10 mitra (%)');style_axis(axes[1],'x')
    for y,v in zip(ypos,c.Export_Share_Within10):axes[1].text(v+.4,y,f'{v:.1f}%',va='center',fontsize=10)
    axes[1].set_xlim(0,c.Export_Share_Within10.max()*1.2)
    fig.tight_layout(w_pad=3);assets['partners']=savefig(fig,'partner_trade_2025')

    g=goods[goods.Quarter.str.startswith('2025')].groupby('Commodity_Class')[['Exports_USDk','Imports_USDk']].sum(min_count=40)
    order=['commodity','noncommodity','mixed','unclassified']
    g=g.reindex(order);shares=g.div(g.sum(axis=0),axis=1)*100
    shares.to_csv(ASSETS/'descriptive_goods_shares_2025_pct.csv');exports['goods_shares_2025']=shares.to_dict()
    fig,ax=plt.subplots(figsize=(10.8,2.65));left=np.zeros(2)
    names=['Komoditas','Nonkomoditas','Campuran','Belum terklasifikasi']
    for i,(cls,name,col) in enumerate(zip(order,names,['brown','dark','gold','light'])):
        vals=shares.loc[cls].to_numpy();ax.barh([1,0],vals,left=left,color=hexcolor(col),height=.46,label=name)
        for j,v in enumerate(vals):
            if v>8:ax.text(left[j]+v/2,[1,0][j],f'{v:.1f}%',ha='center',va='center',color='white',fontweight='bold',fontsize=15)
        left+=vals
    ax.set_yticks([1,0],['Ekspor','Impor']);ax.set_xlim(0,100);ax.set_xlabel('Pangsa nilai perdagangan dalam 10 mitra (%)')
    ax.spines[['top','right','left']].set_visible(False);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.28),ncol=4,frameon=False,fontsize=10)
    assets['composition']=savefig(fig,'goods_composition_2025')

    design=pd.read_stata(ROOT/'output/diagnostics/oskooee/models/WORLD_NARDL_AIC4_design.dta')
    periods=pd.to_datetime(design.tq).dt.to_period('Q').astype(str)
    sample=world.set_index('Quarter').loc[periods].copy()
    sample['M_over_X']=sample.World_Imports_USDk/sample.World_Exports_USDk
    descspec=[('Ekspor (USD miliar)','World_Exports_USDk',1e6),('Impor (USD miliar)','World_Imports_USDk',1e6),
              ('Neraca X − M (USD miliar)','World_Trade_Balance_USDk',1e6),('Rasio M / X','M_over_X',1),
              ('ln(M / X)','World_Ln_Imports_Exports',1),('PDB riil Indonesia (indeks)','IDN_GDP_Real_Index_2015mean100',1),
              ('Aktivitas 10 mitra (indeks)','Foreign_Activity_Top10_FixedWeight_Index',1),('REER BIS (indeks)','REER_BIS_broad',1)]
    desc=[]
    for label,col,div in descspec:
        v=sample[col]/div;desc.append([label,int(v.count()),v.mean(),v.std(ddof=1),v.min(),v.max()])
    desc=pd.DataFrame(desc,columns=['Variabel','N','Mean','SD','Min','Max']);desc.to_csv(ASSETS/'descriptive_world_estimation_sample.csv',index=False)
    exports['descriptives']=desc
    desc_log=design[['y','yd','yf','q','pos','neg']].describe().T
    desc_log.to_csv(ASSETS/'descriptive_transformed_world.csv')
    exports['log_descriptives']=desc_log

    reg=pd.read_csv(ROOT/'output/diagnostics/oskooee/case_registry.csv')
    r=reg[(reg.scope.eq('bilateral')) & reg.scenario.eq('main')].copy()
    fig,ax=plt.subplots(figsize=(10.8,3.6))
    for i,iso in enumerate(ISOS):
        v=r[r.series_id.eq('BIL_'+iso)].iloc[0]
        start=pd.Period(v.first_quarter,freq='Q').ordinal/4+1970
        end=pd.Period(v.last_quarter,freq='Q').ordinal/4+1970
        ax.plot([start,end],[i,i],color=hexcolor('brown'),lw=10,solid_capstyle='butt')
        ax.text(end+.2,i,f'{v.first_quarter}–{v.last_quarter}',va='center',fontsize=10)
    ax.set_yticks(range(10),[COUNTRIES[i] for i in ISOS]);ax.invert_yaxis();ax.set_xlim(2005.5,2031.5)
    ax.set_xticks([2006,2010,2014,2018,2022,2026]);style_axis(ax,'x');ax.spines['left'].set_visible(False)
    assets['coverage']=savefig(fig,'bilateral_available_windows')

    dm=pd.read_csv(ROOT/'output/diagnostics/oskooee/dynamic_multipliers.csv')
    def multiplier(model,name):
        fig,ax=plt.subplots(figsize=(10.6,3.8))
        for direction,label,color in [('depreciation','Depresiasi: −ln(1,10)','brown'),('appreciation','Apresiasi: +ln(1,10)','blue')]:
            v=dm[dm.model_id.eq(model)&dm.direction.eq(direction)].sort_values('horizon_quarters')
            ax.plot(v.horizon_quarters,v.effect_logpoints,color=hexcolor(color),lw=2.2,label=label)
            ax.fill_between(v.horizon_quarters.to_numpy(),v.lower95_logpoints.to_numpy(),v.upper95_logpoints.to_numpy(),color=hexcolor(color),alpha=.12)
        ax.axhline(0,color='#777777',lw=.9);ax.set_xlabel('Horizon sejak perubahan kurs (kuartal)')
        ax.set_ylabel('100 × Δln(M/X)');style_axis(ax);ax.legend(loc='best',frameon=False,fontsize=11)
        return savefig(fig,name)
    assets['world_response']=multiplier('WORLD_NARDL_AIC4','world_nardl_response')
    assets['aus_response']=multiplier('BIL_AUS_NARDL_AIC4','aus_nardl_response')

    def forest(df,name):
        df=df.copy();df['iso']=df.series_id.str.split('_').str[1]
        df=df.set_index('iso').loc[ISOS].reset_index()
        fig,ax=plt.subplots(figsize=(10.8,4.4))
        for i,row in df.iterrows():
            supported=bool(row.Levels_supported5);clean=bool(row.Diagnostic_clean5)
            col='brown' if supported and clean else ('gold' if supported else 'gray')
            ax.plot([row.lr_neg_lo95,row.lr_neg_hi95],[i,i],color=hexcolor(col),lw=2,alpha=.90)
            ax.scatter([row.lr_neg_b],[i],s=52,color=hexcolor(col),marker='o' if supported else 'D',zorder=3,
                       facecolor=hexcolor(col) if supported else 'white',linewidth=1.5)
        ax.axvline(0,color=hexcolor('red'),lw=1);ax.set_yticks(range(10),[COUNTRIES[i] for i in ISOS]);ax.invert_yaxis()
        ax.set_xlabel('Koefisien NEG jangka panjang; interval nominal 95%');style_axis(ax,'x')
        from matplotlib.lines import Line2D
        legend=[Line2D([],[],marker='o',linestyle='None',color=hexcolor('brown'),label='Levels + diagnostik'),
                Line2D([],[],marker='o',linestyle='None',color=hexcolor('gold'),label='Levels; diagnostik ditolak'),
                Line2D([],[],marker='D',linestyle='None',color=hexcolor('gray'),markerfacecolor='white',label='Levels belum didukung')]
        fig.legend(handles=legend,loc='lower center',ncol=3,frameon=False,fontsize=10)
        fig.tight_layout(rect=(0,.08,1,1));return savefig(fig,name)
    n=primary[primary.estimator.eq('NARDL')]
    assets['forest_bil']=forest(n[n.scope.eq('bilateral')],'bilateral_lr_negative')
    for cls in ['commodity','noncommodity']:
        assets['forest_'+cls]=forest(n[n.series_id.str.endswith('_'+cls)],'goods_lr_'+cls)

    diag=[('BG(4)','bg4_p'),('Heterosk.','hetero_p'),('RESET','reset_p'),('Normalitas','JB_p'),('ARCH(4)','ARCH4_p'),('CUSUMSQ','CUSUMSQ_p_MC')]
    fig,ax=plt.subplots(figsize=(10.8,3.15))
    vals=[int((primary[k]<.05).sum()) for _,k in diag]
    ax.barh([v[0] for v in diag],vals,color=hexcolor('brown'),height=.55);ax.invert_yaxis()
    for i,v in enumerate(vals):ax.text(v+.25,i,f'{v} / 62',va='center')
    ax.set_xlim(0,max(vals)+5);ax.set_xlabel('Model yang menolak H0 diagnostik pada 5%');style_axis(ax,'x')
    assets['diagnostics']=savefig(fig,'diagnostic_rejection_counts')

    st=pd.read_csv(ROOT/'output/diagnostics/oskooee/stability_paths.csv')
    fig,axes=plt.subplots(1,2,figsize=(11.6,3.65))
    for ax,model in zip(axes,['WORLD_NARDL_AIC4','BIL_AUS_NARDL_AIC4']):
        d=st[st.model_id.eq(model)];xx=1960+d.tq/4
        ax.fill_between(xx,d.lower,d.upper,color=hexcolor('beige'),label='Band MC 95%')
        ax.plot(xx,d.expected,color=hexcolor('gray'),lw=1,ls=':')
        ax.plot(xx,d.CUSUMSQ,color=hexcolor('brown'),lw=2,label='CUSUMSQ')
        ax.set_title('Indonesia–dunia' if 'WORLD' in model else 'Indonesia–Australia')
        ax.set_ylim(-.03,1.03);ax.set_xlabel('Tahun');style_axis(ax)
        ax.legend(frameon=False,fontsize=10,loc='lower right')
    axes[0].set_ylabel('Akumulasi kuadrat residual rekursif')
    fig.tight_layout(w_pad=2.5);assets['stability']=savefig(fig,'stability_world_aus')
    return assets,exports

def build(template):
    OUT.mkdir(parents=True,exist_ok=True);ASSETS.mkdir(exist_ok=True)
    files={
        'primary':ROOT/'output/tables/oskooee/results_primary_models.csv',
        'all':ROOT/'output/tables/oskooee/results_all_models.csv',
        'world':ROOT/'intermediate/Panel_World_Quarter.csv',
        'country':ROOT/'intermediate/Panel_Country_Quarter.csv',
        'goods':ROOT/'intermediate/Panel_CommodityGroup_Country_Quarter.csv',
        'analysis':ROOT/'intermediate/Oskooee_Quarterly_Analysis.csv',
    }
    before={str(v.relative_to(ROOT)):digest(v) for v in files.values()}
    data={k:pd.read_csv(v) for k,v in files.items()}
    primary=data['primary'];allmodels=data['all']
    assert len(primary)==62 and len(allmodels)==174
    a,e=prepare_assets(primary,allmodels,data['world'],data['country'],data['goods'],data['analysis'])
    d=Deck(template);d.cover()

    s=d.slide('Apakah depresiasi selalu memperbaiki perdagangan Indonesia?',
        'Pertanyaan penelitian dimulai dari neraca perdagangan, lalu ditelusuri menurut mitra dan kelompok barang.',
        notes='Hipotesis awal pengguna menyangkut ekspor. Estimasi replikasi saat ini menggunakan rasio impor/ekspor, sehingga kesimpulan dibatasi pada trade balance. Kanal input impor dan TiVA ditangguhkan.')
    for x,title,body in [( .68,'01  Agregat dunia','Bagaimana rasio impor terhadap ekspor merespons perubahan kurs riil efektif?'),
                          (4.76,'02  Sepuluh mitra','Apakah respons berbeda antarhubungan bilateral Indonesia dengan mitra dagang?'),
                          (8.84,'03  Jenis barang','Apakah komoditas dan nonkomoditas menunjukkan respons kurs yang berbeda?')]:
        box(s,x,1.85,3.80,2.35,'beige');text(s,x+.18,2.05,3.45,.55,title,17,'brown',True)
        text(s,x+.18,2.82,3.42,1.15,body,16)
    text(s,.85,4.65,11.60,.80,'Hipotesis kerja: struktur komoditas dan harga global dapat membatasi respons perdagangan terhadap depresiasi.',20,'dark',True)
    callout(s,'Outcome yang diestimasi adalah ln(M/X); perubahan ekspor secara terpisah belum diidentifikasi.',6.20,size=13)

    v=e['world_2025']
    s=d.slide('Perdagangan Indonesia meningkat, dengan dinamika ekspor dan impor berbeda',
        'Statistik deskriptif Indonesia–dunia | nilai nominal barang, tahun lengkap 2010–2025.',
        'Sumber: World Bank GEM; intermediate/Panel_World_Quarter.csv. USD ribu dikonversi menjadi USD miliar.',
        'Angka tahunan dijumlahkan hanya bila empat kuartal lengkap. Tahun 2026 tidak ditampilkan sebagai satu tahun penuh. Periode 2006–2009 tidak dipakai dalam grafik utama karena audit ketidakselarasan sumber.')
    cards(s,[(fmt(v['World_Exports_USDk'],1),'Ekspor 2025','USD miliar'),(fmt(v['World_Imports_USDk'],1),'Impor 2025','USD miliar'),(fmt(v['World_Trade_Balance_USDk'],1),'Neraca X − M 2025','USD miliar')],y=1.63,h=1.36)
    picture(s,a['world'],.73,3.16,11.8,3.55)

    s=d.slide('Sepuluh mitra memiliki skala dan posisi perdagangan yang berbeda',
        'Statistik deskriptif 2025 | pangsa ekspor dihitung di dalam sampel 10 mitra.',
        'Sumber: panel bilateral proyek Tio (Trade Map/CEIC asal); Panel_Country_Quarter.csv.',
        'Pangsa pada panel kanan menggunakan total ekspor ke sepuluh mitra sebagai penyebut, bukan total ekspor Indonesia ke dunia. Tidak mengklaim pemeringkatan top ten dunia terbaru. Data perdagangan dapat berbeda vintage dengan GEM.')
    picture(s,a['partners'],.60,1.68,12.1,4.82)
    callout(s,'Perbedaan ukuran pasar dan pola impor menjadi alasan estimasi bilateral secara terpisah.',6.44,size=13)

    share=e['goods_shares_2025']['Exports_USDk']['commodity']
    s=d.slide(f'Komoditas mencakup {share:.1f}% ekspor pada sampel sepuluh mitra tahun 2025'.replace('.',','),
        'Klasifikasi HS-4 berbasis UNCTAD A11 | pangsa dihitung dari nilai perdagangan nominal.',
        'Sumber: HS4_Commodity_Classification.csv dan Panel_CommodityGroup_Country_Quarter.csv; pengolahan Tio.',
        'Empat kategori dipertahankan dalam penyebut: komoditas, nonkomoditas, mixed, unclassified. Model biner hanya memakai dua kategori pertama. Statistik ini khusus sepuluh mitra pada 2025; bukan dunia dan bukan angka gabungan seluruh tahun.')
    picture(s,a['composition'],.78,1.95,11.8,3.40)
    text(s,.88,5.65,11.55,.55,'Komposisi ekspor memberi motivasi untuk membandingkan kelompok; komposisi saja belum membuktikan sensitivitas kurs.',17,'dark',True)
    callout(s,'Kelompok campuran dan belum terklasifikasi tidak dipaksa menjadi komoditas atau nonkomoditas.',6.40,size=12.5)

    s=d.slide('Variabel utama mengikuti spesifikasi trade balance dalam paper',
        'Frekuensi kuartalan | definisi dan orientasi tanda dijaga konsisten di seluruh model.',
        'Sumber: Bahmani-Oskooee & Fariditavana (2015/2016), DOI 10.1007/s11079-015-9369-5; skrip 12–13.',
        'Perdagangan nominal digunakan sebagai rasio M/X. GDP adalah log indeks level riil, bukan pertumbuhan GDP. Kurs riil bilateral semula naik berarti depresiasi sehingga q dibalik tanda. CPI berfungsi membangun kurs riil; bukan regressor tambahan terpisah.')
    rows=[['y = ln(M/X)','Rasio impor terhadap ekspor','Turun = perbaikan neraca perdagangan'],
          ['X dan M','Nilai barang nominal, USD','X − M ditampilkan sebagai deskriptif'],
          ['yd = ln(PDB riil IDN)','Indeks level riil, rata-rata 2015 = 100','Kontrol aktivitas domestik'],
          ['yf = ln(PDB riil mitra)','Bilateral: indeks PDB mitra','Dunia: proksi aktivitas 10 mitra'],
          ['q = ln(kurs riil)','Naik = apresiasi; turun = depresiasi','Dunia: REER BIS; bilateral: −ln(RER)'],
          ['POS dan NEG','Akumulasi Δq positif dan negatif','Memisahkan apresiasi dan depresiasi'],
          ['cp = ln(BCOM)','Indeks harga komoditas global','Hanya pada sensitivitas jenis barang']]
    table(s,['Variabel','Definisi / satuan','Fungsi dalam analisis'],rows,h=4.82,widths=[2.1,4,5],size=12.8)

    s=d.slide('Statistik deskriptif memakai sampel estimasi agregat yang sama',
        'Indonesia–dunia | 2011Q1–2026Q1 | 61 kuartal efektif pada ARDL dan NARDL utama.',
        'Sumber: WORLD_NARDL_AIC4_design.dta dan Panel_World_Quarter.csv; simpangan baku sampel (N − 1).',
        'Tanggal dipilih dari desain estimasi Stata, lalu dicocokkan dengan panel dunia. Tidak menggunakan seluruh 4.388 baris dataset analisis yang mencakup pengulangan seri/skenario. Indeks PDB berbasis rata-rata 2015; basis REER mengikuti BIS.')
    rows=[[r.Variabel,int(r.N),fmt(r.Mean),fmt(r.SD),fmt(r.Min),fmt(r.Max)] for r in e['descriptives'].itertuples()]
    table(s,['Variabel','N','Rata-rata','SD','Minimum','Maksimum'],rows,h=4.85,widths=[4.0,.6,1.35,1.35,1.35,1.35],size=12)

    s=d.slide('Ketersediaan data membatasi kesetaraan sampel antarmitra',
        'Window tersedia sebelum holdback lag | estimasi utama memakai rentang lengkap berurutan.',
        'Sumber: output/diagnostics/oskooee/case_registry.csv; audit_validitas_data_macro.md.',
        'Grafik menunjukkan window tersedia, bukan window estimasi setelah empat lag. India CPI baseline dimulai 2013. AS berhenti 2025Q3 karena CPI Oktober kosong; Vietnam berhenti 2025Q2 karena BIS FX Agustus kosong. Data tidak dirapatkan melewati celah.')
    picture(s,a['coverage'],.65,1.63,12.05,4.20)
    text(s,.88,6.00,11.65,.63,'Agregat utama: window 2010Q1–2026Q1. Permintaan asing merupakan proksi PDB 10 mitra berbobot ekspor tetap 2006–2008.',14,'dark',True)

    s=d.slide('Dua mekanisme memberi arah respons yang perlu diuji',
        'Kerangka hipotesis | model mengukur respons historis bersyarat pada aktivitas domestik dan mitra.',
        'Sumber: kerangka penelitian Tio dan spesifikasi paper replikasi; harga BCOM sebagai kontrol sensitivitas.',
        'Kanal daya saing dan harga komoditas ditampilkan sebagai hipotesis, bukan mekanisme kausal teridentifikasi. Mengontrol BCOM saja tidak mengidentifikasi penuh pengaruh harga global. Kanal input impor secara eksplisit ditangguhkan.')
    for x,title,body in [( .73,'Daya saing harga','Depresiasi riil → barang Indonesia relatif lebih murah → ekspor dan impor menyesuaikan dengan jeda.'),
                          (6.88,'Harga komoditas global','Nilai ekspor komoditas dapat bergerak bersama harga global → respons nilai perdagangan terhadap kurs dapat terbatas.')]:
        box(s,x,1.90,5.72,2.72,'beige');text(s,x+.23,2.10,5.25,.50,title,20,'brown',True)
        text(s,x+.23,2.88,5.20,1.35,body,17)
    text(s,.90,5.13,11.52,.67,'Uji empiris: bandingkan ARDL dan NARDL, estimasi per mitra dan kelompok barang, serta tambahkan BCOM sebagai sensitivitas.',18,'dark',True)
    callout(s,'Kanal ketergantungan bahan baku impor / TiVA ditangguhkan sesuai ruang lingkup penelitian.',6.36,size=13)

    s=d.slide('ARDL menghubungkan dinamika jangka pendek dan hubungan level',
        'Adaptasi Bahmani-Oskooee & Fariditavana | intercept tanpa tren, ECM dengan level t − 1.',
        'Sumber: paper replikasi DOI 10.1007/s11079-015-9369-5; 13_run_oskooee_models.do.',
        'Persamaan disajikan dalam bentuk UECM. z terdiri dari yd, yf, dan q; untuk sensitivitas harga ditambahkan cp. Batas lag utama empat lag ARDL levels setara maksimum tiga lag first difference ECM. Ini berbeda dari paper yang memiliki sampel lebih panjang dan delapan lag first difference.')
    box(s,.78,1.85,11.77,1.36,'beige')
    text(s,1.02,2.05,11.24,.83,'Δyₜ = α + ρyₜ₋₁ + θ′zₜ₋₁\n          + ΣφⱼΔyₜ₋ⱼ + ΣΓⱼ′Δzₜ₋ⱼ + εₜ',22,'dark',True)
    steps(s,[('Hubungan level','z = [ln(PDB IDN), ln(PDB mitra), q]. Koefisien LR dinormalisasi sebagai −θ / ρ.'),
             ('Seleksi lag','AIC, maksimum 4 lag levels pada sampel holdback yang sama; maksimum 2 lag sebagai sensitivitas.'),
             ('Syarat interpretasi','Koefisien level dibaca setelah memeriksa unit-root, F/t bounds, akar dinamis, dan diagnostik.')],y=3.65,spacing=.84)

    s=d.slide('NARDL memisahkan apresiasi dan depresiasi secara eksplisit',
        'Kurs q naik = apresiasi | NEG merupakan akumulasi perubahan bertanda negatif.',
        'Sumber: paper replikasi; notes/hasil_ardl_nardl_oskooee.md; definisi variabel dalam skrip 12.',
        'POS_t = jumlah max(Δq,0); NEG_t = jumlah min(Δq,0). Koefisien NEG positif dikalikan depresiasi negatif menurunkan y, sehingga trade balance membaik. Wald menguji LR_POS = LR_NEG, bukan koefisien bertanda berlawanan. Ketika bounds tidak mendukung, Wald signifikan tidak membuktikan asimetri jangka panjang yang mapan.')
    box(s,.78,1.80,11.78,1.26,'beige')
    text(s,1.02,1.99,11.25,.78,'POSₜ = Σ max(Δqₛ, 0)       NEGₜ = Σ min(Δqₛ, 0)\nyₜ = a + βd ydₜ + βf yfₜ + β⁺ POSₜ + β⁻ NEGₜ + uₜ',21,'dark',True)
    table(s,['Elemen','Makna','Cara membaca'],[
        ['β⁻ > 0','Depresiasi menurunkan ln(M/X)','Arah perbaikan trade balance'],
        ['β⁻ < 0','Depresiasi menaikkan ln(M/X)','Arah perburukan trade balance'],
        ['Wald LR','H₀: β⁺ = β⁻','Asimetri nominal; perlu dukungan levels'],
        ['Multiplier dinamis','100 × perubahan ln(M/X)','Negatif = membaik; positif = memburuk']],y=3.55,h=2.63,widths=[2.1,4.5,4.5],size=13)
    callout(s,'Trade balance dapat berubah karena ekspor, impor, atau keduanya; koefisien ini bukan efek ekspor saja.',6.42,size=12.5)

    s=d.slide('Estimasi mencakup 62 model utama dan 112 model sensitivitas',
        '31 seri utama × 2 estimator | seluruh model diselesaikan di Stata 19.5 IC.',
        'Sumber: results_primary_models.csv; results_all_models.csv; analysis_validation_report.json.',
        'Model utama: dunia 2, bilateral 20, jenis barang 40. Sensitivitas: cap lag dua sebanyak 62, BCOM 40, GEM FX 6, India WPI 2, dunia 2006+ 2. HS4 hanya disaring; 2.115 dari 12.214 seri memenuhi kriteria awal, bukan telah diestimasi.')
    cards(s,[('2','Agregat dunia','1 seri × ARDL / NARDL'),('20','Sepuluh mitra','10 seri × ARDL / NARDL'),('40','Jenis barang','20 seri × ARDL / NARDL')],y=1.72)
    table(s,['Uji sensitivitas','Model','Tujuan'],[
        ['Maksimum 2 lag levels',62,'Kepekaan terhadap kompleksitas dinamika'],
        ['Kontrol harga BCOM',40,'Peran harga komoditas pada model kelompok'],
        ['Alternatif FX GEM',6,'THA, VNM, KOR: perbedaan keluarga sumber'],
        ['India WPI dan dunia 2006+',4,'Periode / proksi harga alternatif']],y=3.55,h=2.62,widths=[3.6,.8,6],size=13)
    callout(s,'Model per HS-4 individual belum dijalankan; run ini berfokus pada kelompok komoditas dan nonkomoditas.',6.43,size=12.5)

    s=d.slide('Hubungan jangka panjang dinilai melalui beberapa tahap pemeriksaan',
        'Hasil koefisien dipisahkan dari kelayakan interpretasinya.',
        'Sumber: ardl 1.0.6; Kripfganz–Schneider; diagnostic_summary.csv; independent_OLS_checks.csv.',
        'Bounds case III dengan critical values finite sample, keputusan F dan t bersama. Levels_supported5 juga memeriksa joint-X, akar AR, risiko I(2), residual df. Diagnostic_clean5 merupakan flag gabungan tidak ditolak pada uji yang dicantumkan. Tidak menolak diagnostik bukan bukti model benar.')
    steps(s,[('Orde integrasi','ADF dan PP pada level serta first difference; ARDL mensyaratkan tidak ada I(2).'),
             ('Dukungan hubungan level','F dan t bounds finite-sample 5%, lalu joint-X, stabilitas akar AR, dan kecukupan sampel.'),
             ('Residual dan stabilitas','BG, heteroskedastisitas, RESET, normalitas, ARCH, CUSUM, dan CUSUMSQ.'),
             ('Validasi komputasi','Ekuivalensi ECM–levels dan prediksi OLS independen lolos pada seluruh 174 model.')],y=1.80,spacing=1.08)
    callout(s,'Koefisien ECT negatif dan p-value t biasa yang signifikan belum cukup untuk menetapkan kointegrasi.',6.38,size=12.8)

    s=d.slide('Agregat dunia belum mendukung hubungan level pada taraf 5%',
        'Sampel efektif 2011Q1–2026Q1 | N = 61 | angka LR ditampilkan sebagai keluaran estimasi bersyarat.',
        'Sumber: results_primary_models.csv, WORLD_ARDL_AIC4 dan WORLD_NARDL_AIC4.',
        'ARDL F=2.3606 dan t=-2.1556; NARDL F=3.8237 dan t=-2.7126. Kedua keputusan gabungan F/t adalah No rejection, bukan dukungan levels 5%. Wald asimetri p=0.00718 adalah nominal. NARDL CUSUMSQ p MC=0.0126. Jangan menyimpulkan depresiasi selalu memperbaiki/memperburuk neraca agregat.')
    world=primary[primary.scope.eq('aggregate')].set_index('estimator')
    rows=[]
    for est in ['ARDL','NARDL']:
        r=world.loc[est]
        rows.append([est,r.lag_order,fmt(r.lr_q_b,3),fmt(r.lr_pos_b,3),fmt(r.lr_neg_b,3),pval(r.lr_asym_p),'Belum didukung'])
    table(s,['Model','Lag levels','LR q','LR POS','LR NEG','p asimetri','Levels 5%'],rows,y=1.83,h=1.76,widths=[1,2,1,1.1,1.1,1.5,2.1],size=13)
    steps(s,[('Hasil statistik utama','Kedua baseline tidak menolak hipotesis tidak ada hubungan level pada taraf 5%.'),
             ('Asimetri belum menjadi kesimpulan LR','Wald NARDL p = 0,007; dukungan bounds tidak terpenuhi dan CUSUMSQ menolak stabilitas.')],y=4.03,spacing=.98)
    callout(s,'Kesimpulan agregat: bukti jangka panjang masih belum memadai pada spesifikasi dan proksi saat ini.',6.39,size=13)

    s=d.slide('Respons dinamis agregat perlu dibaca bersama batas modelnya',
        'NARDL dunia | shock simetris pada q sebesar ±ln(1,10) | interval pointwise nominal 95%.',
        'Sumber: dynamic_multipliers.csv, WORLD_NARDL_AIC4. Interval delta-method, bersyarat pada lag terpilih.',
        'Shock -ln(1.10) merupakan kebalikan dari faktor apresiasi 1.10; bukan persis penurunan indeks 10%. Respons ditampilkan dalam 100 x log-point, bukan persen perubahan ekspor. Model tidak memiliki dukungan levels 5% dan terdapat CUSUMSQ instability, sehingga pola tidak diklaim sebagai bukti J-curve.')
    picture(s,a['world_response'],.75,1.72,11.9,4.5)
    callout(s,'Kurva merupakan ilustrasi dari model terpilih; belum cukup untuk menyatakan J-curve atau efek ekspor.',6.42,size=12.7)

    s=d.slide('Bukti bilateral bervariasi; dukungan paling jelas muncul pada Australia',
        'NARDL bilateral | seluruh 10 mitra ditampilkan | koefisien NEG dan interval nominal 95%.',
        'Sumber: results_primary_models.csv. Cokelat = levels + diagnostik; jingga = levels; kosong = levels belum didukung.',
        'Interval ditampilkan pula untuk model tanpa dukungan levels agar pelaporan lengkap; koefisien tersebut tidak diartikan sebagai LR mapan. Australia dan Malaysia lolos levels+diagnostik. Malaysia p BH=0.0591; Australia=0.00399. Thailand levels didukung tetapi diagnostik ditolak. Sampel tidak identik.')
    picture(s,a['forest_bil'],.58,1.68,12.0,4.78)
    callout(s,'NEG positif berarti arah perbaikan saat depresiasi; status levels dan diagnostik tetap menentukan interpretasi.',6.46,size=12.1)

    s=d.slide('Australia menunjukkan arah perbaikan dengan dukungan diagnostik lebih kuat',
        'Indonesia–Australia | NARDL utama, N = 77 | 2007Q1–2026Q1.',
        'Sumber: BIL_AUS_NARDL_AIC4; results_primary_models.csv dan dynamic_multipliers.csv.',
        'LR NEG=3.3560, interval95 [1.5631,5.1490], p nominal0.000399, p BH0.003990. Lolos levels dan flag diagnostik. Hasil bersyarat sumber GDP/CPI, termasuk interpolasi CPI Australia oleh penyedia. Bukti kasus ini tidak digeneralisasi ke seluruh perdagangan Indonesia.')
    cards(s,[('3,356','Koefisien LR NEG','Arah perbaikan saat depresiasi'),('0,004','p-value BH','Koreksi eksploratif 10 NARDL bilateral'),('77','Observasi efektif','Levels + diagnostik mendukung')],y=1.63,h=1.37)
    picture(s,a['aus_response'],.77,3.23,11.8,3.15)
    text(s,.88,6.48,11.55,.38,'Temuan bersyarat pada pasangan Australia; tidak dapat digeneralisasi sebagai manfaat depresiasi bagi semua ekspor.',12.4,'dark',True)

    s=d.slide('Komoditas: arah koefisien berbeda dan ketidakpastian tetap besar',
        'NARDL kelompok komoditas × 10 mitra | seluruh estimasi ditampilkan, termasuk yang diagnostiknya bermasalah.',
        'Sumber: results_primary_models.csv, TYPE_*_commodity_NARDL_AIC4. Legenda status sama dengan grafik bilateral.',
        'Tujuh dari sepuluh model komoditas NARDL mendapat levels supported; hanya AUS, IND, MYS juga lolos diagnostik. Koefisien NEG ketiganya tidak signifikan nominal5%. CHN negatif signifikan tetapi diagnostik ditolak. Tidak menafsirkan koefisien tidak signifikan sebagai nol atau bukti dominasi harga global.')
    picture(s,a['forest_commodity'],.58,1.69,12.0,4.77)
    callout(s,'Pada AUS, IND, dan MYS yang lolos penyaringan, koefisien depresiasi komoditas belum signifikan nominal 5%.',6.45,size=12)

    s=d.slide('Nonkomoditas belum memperoleh dukungan hubungan level pada 5%',
        'NARDL kelompok nonkomoditas × 10 mitra | koefisien LR hanya keluaran bersyarat dari model terpilih.',
        'Sumber: results_primary_models.csv, TYPE_*_noncommodity_NARDL_AIC4. Simbol kosong = levels belum didukung.',
        'Tidak ada model utama nonkomoditas ARDL/NARDL yang lolos flag levels supported5. Interval nominal yang tidak meliputi nol pada beberapa NARDL tidak mengatasi kegagalan dukungan levels. Tidak signifikan bukan bukti komoditas/nonkomoditas sama, dan beda signifikansi bukan uji beda koefisien antarkelompok.')
    picture(s,a['forest_noncommodity'],.58,1.69,12.0,4.77)
    callout(s,'Perbedaan sensitivitas komoditas–nonkomoditas belum diuji langsung dengan kovarians lintas kelompok.',6.45,size=12.5)

    s=d.slide('Penyaringan mempersempit jumlah model yang layak dibaca lebih jauh',
        '62 model utama | seluruh hasil tetap dilaporkan; model tidak dihapus agar terlihat lebih baik.',
        'Sumber: results_primary_models.csv. Flag gabungan adalah alat penyaringan, bukan jaminan model benar.',
        '27 menolak no-level relation lewat keputusan F/t5. 18 lolos syarat levels tambahan. 7 juga lolos seluruh flag diagnostik yang tercantum. Tiga dari tujuh memiliki p BH koefisien depresiasi <5%: BIL_AUS_ARDL, BIL_AUS_NARDL, TYPE_AUS_commodity_ARDL. Dua estimator pada seri sama bukan bukti independen.')
    cards(s,[('27 / 62','F dan t bounds','Menolak no-level relation 5%'),('18 / 62','Levels didukung','Lolos pemeriksaan tambahan'),('7 / 62','Levels + diagnostik','Tidak ditolak oleh flag gabungan')],y=1.80,h=1.55)
    clean=primary[primary.Levels_supported5 & primary.Diagnostic_clean5]
    rows=[]
    for r in clean.itertuples():
        name=r.model_id.replace('_AIC4','').replace('BIL_','').replace('TYPE_','').replace('_commodity',' komoditas').replace('_',' ')
        rows.append([name,fmt(r.lr_neg_b if r.estimator=='NARDL' else r.lr_q_b,3),pval(r.Dep_LR_p),pval(r.Dep_LR_p_BH)])
    table(s,['Model tersaring','Koef. depresiasi¹','p nominal','p BH'],rows,y=3.72,h=2.75,widths=[5,2,1.5,1.5],size=11.5)
    text(s,.88,6.60,11.4,.30,'¹ ARDL: q; NARDL: NEG. Tanda positif menunjukkan arah perbaikan ketika q turun.',10.5,'gray')

    s=d.slide('Diagnostik mengingatkan bahwa inferensi OLS perlu kehati-hatian',
        'Jumlah penolakan pada 5% di antara 62 model utama | uji berulang dapat menimbulkan false alarm.',
        'Sumber: diagnostic_summary.csv. CUSUMSQ menggunakan 19.999 simulasi referensi Gaussian dengan seed tetap.',
        'BG4=12, BP=14, RESET=11, JB=12, ARCH4=5, CUSUMSQ=19. Penolakan diagnostik bukan kepastian salah model, namun p-value OLS klasik tidak boleh diperlakukan kuat. Tidak ada model utama ditandai I2 belum disingkirkan; daya uji sampel pendek tetap terbatas.')
    picture(s,a['diagnostics'],.76,1.80,11.85,3.94)
    text(s,.90,5.96,11.45,.76,'P-value dan interval masih bersifat nominal setelah seleksi AIC. Koreksi BH bersifat eksploratif dan belum mengoreksi ketidakpastian pemilihan lag.',16,'dark',True)

    s=d.slide('Hasil peka terhadap panjang lag dan kontrol harga komoditas',
        'Ringkasan sensitivitas | angka menunjukkan model dengan levels didukung dan diagnostik tidak ditolak.',
        'Sumber: results_all_models.csv. AIC antarcap memiliki N efektif berbeda; tidak dibandingkan secara langsung.',
        'Tabulasi menggunakan jumlah Levels_supported5 dan gabungan dengan Diagnostic_clean5, bukan clean saja. Model PRICE_IND_commodity_NARDL_AIC4 N49/K25 tidak memiliki critical values finite-sample, sehingga ditandai unavailable. Kesamaan jumlah dukungan tidak berarti koefisien identik atau mekanisme harga teridentifikasi.')
    rows=[]
    for label,scope,scenario,cap in [('Dunia: utama','aggregate','main',4),('Dunia: lag ≤ 2','aggregate','main',2),('Dunia: periode 2006+','aggregate','world_2006_sensitivity',4),
        ('Bilateral: utama','bilateral','main',4),('Bilateral: lag ≤ 2','bilateral','main',2),('Jenis barang: utama','goods','main',4),
        ('Jenis barang: lag ≤ 2','goods','main',2),('Jenis barang: + BCOM','goods','BCOM_control',4)]:
        v=allmodels[(allmodels.scope.eq(scope))&allmodels.scenario.eq(scenario)&allmodels.cap.eq(cap)]
        rows.append([label,len(v),int(v.Levels_supported5.sum()),int((v.Levels_supported5&v.Diagnostic_clean5).sum())])
    table(s,['Keluarga model','Jumlah','Levels 5%','Levels + diagnostik'],rows,y=1.70,h=4.62,widths=[5.4,1.2,1.8,2.8],size=12.5)
    callout(s,'Kontrol BCOM merupakan pemeriksaan sensitivitas; belum membuktikan bahwa harga global adalah penyebab utama.',6.45,size=12.3)

    s=d.slide('Kesimpulan awal: manfaat depresiasi belum dapat digeneralisasi',
        'Temuan menjawab trade balance bersyarat; hipotesis tentang ekspor memerlukan pengujian tambahan.',
        'Sumber: sintesis 62 model utama, 112 sensitivitas dan catatan audit data Tio.',
        'Hindari klaim hipotesis terbukti, efek nol, efek kausal ekspor, atau komoditas pasti kurang sensitif. Bukti terkuat tersaring terdapat pada Australia; agregat belum didukung. Bukti negatif yang tidak signifikan bukan bukti kerugian. Model bilateral bersampel berbeda.')
    steps(s,[('Agregat','Belum ada dukungan hubungan level 5% pada kedua baseline Indonesia–dunia.'),
             ('Bilateral','Australia menunjukkan arah perbaikan dengan dukungan penyaringan lebih kuat; hasil mitra lain beragam.'),
             ('Jenis barang','Komoditas menunjukkan ketidakpastian dan heterogenitas; nonkomoditas belum didukung levels.'),
             ('Status hipotesis','Hipotesis komoditas belum terbukti. Perlu uji beda kelompok dan model ekspor tersendiri.')],y=1.85,spacing=1.07)
    callout(s,'Rumusan aman: respons perdagangan terhadap depresiasi berbeda menurut pasangan dan spesifikasi.',6.43,size=13)

    s=d.slide('Prioritas lanjutan: perkuat data dan uji perbedaan secara langsung',
        'Langkah berikut disusun dari fondasi data hingga pengujian mekanisme yang lebih spesifik.',
        'Sumber: notes/hasil_ardl_nardl_oskooee.md; audit_validitas_data_macro.md; kelayakan awal HS-4.',
        'Usulan ini merupakan agenda, belum dilaksanakan dalam run saat ini. Hipotesis input impor/TiVA tetap on hold. HS4 pre-eligible bukan jaminan dapat diestimasi. Ekspor nominal dan volume membutuhkan pembedaan serta deflator yang tepat.')
    steps(s,[('Harmonisasi sumber dan periode','Perjelas selisih impor dunia 2006–2009; audit vintage GDP dan konsistensi CPI / kurs.'),
             ('Bandingkan kelompok secara formal','Gunakan desain dengan uji beda koefisien dan kovarians lintas kelompok; samakan window sampel.'),
             ('Pisahkan ekspor dan impor','Model ekspor tersendiri, termasuk peran harga versus volume, diperlukan untuk hipotesis ekspor.'),
             ('Perluas setelah fondasi stabil','HS-4 individual dapat diteliti bertahap; kanal input impor menunggu tahap berikutnya.')],y=1.85,spacing=1.07)

    d.divider()

    s=d.slide('Lampiran | NARDL bilateral: koefisien dan status interpretasi',
        'Semua 10 mitra | p BH dikoreksi secara eksploratif di dalam keluarga NARDL bilateral.',
        'Sumber: results_primary_models.csv. ✓ = terpenuhi / tidak ditolak; — = belum. Interval dan p-value nominal.',
        'Status levels supported memasukkan bounds F/t dan syarat tambahan, bukan F saja. Diagnostic flag tidak ditolak bukan jaminan model benar. Koefisien tanpa levels support belum diartikan sebagai hubungan LR mapan.')
    v=primary[(primary.scope.eq('bilateral'))&primary.estimator.eq('NARDL')]
    rows=[]
    for iso in ISOS:
        r=v[v.series_id.eq('BIL_'+iso)].iloc[0]
        rows.append([COUNTRIES[iso],int(r.N),fmt(r.lr_neg_b,3),pval(r.Dep_LR_p),pval(r.Dep_LR_p_BH),'✓' if r.Levels_supported5 else '—','✓' if r.Diagnostic_clean5 else '—'])
    table(s,['Mitra','N','LR NEG','p nominal','p BH','Levels','Diagnostik'],rows,y=1.70,h=4.98,widths=[3.1,.6,1.4,1.4,1.4,1.2,1.6],size=11.8)

    for cls,title in [('commodity','komoditas'),('noncommodity','nonkomoditas')]:
        s=d.slide('Lampiran | NARDL '+title+': koefisien dan status interpretasi',
            'Kelompok barang pada 10 mitra | p BH dalam keluarga 20 NARDL jenis barang.',
            'Sumber: results_primary_models.csv. ✓ = terpenuhi / tidak ditolak; — = belum; p-value setelah seleksi AIC.',
            'Perbandingan dua tabel kelompok bukan uji statistik beda koefisien antarkelompok. Koefisien tanpa levels support belum layak diartikan sebagai hubungan LR mapan.')
        rows=[]
        for iso in ISOS:
            r=primary[primary.model_id.eq(f'TYPE_{iso}_{cls}_NARDL_AIC4')].iloc[0]
            rows.append([COUNTRIES[iso],int(r.N),fmt(r.lr_neg_b,3),pval(r.Dep_LR_p),pval(r.Dep_LR_p_BH),'✓' if r.Levels_supported5 else '—','✓' if r.Diagnostic_clean5 else '—'])
        table(s,['Mitra','N','LR NEG','p nominal','p BH','Levels','Diagnostik'],rows,y=1.70,h=4.98,widths=[3.1,.6,1.4,1.4,1.4,1.2,1.6],size=11.8)

    s=d.slide('Lampiran | ARDL linear melengkapi pembacaan model nonlinear',
        'Sepuluh mitra | koefisien q positif memberi arah perbaikan ketika q turun (depresiasi).',
        'Sumber: results_primary_models.csv, BIL_*_ARDL_AIC4. p BH dalam 10 model ARDL bilateral.',
        'ARDL linear memaksakan respons simetris. Tabel memungkinkan pembaca menilai apakah pembacaan berbeda dengan NARDL. Perbedaan estimator pada sampel sama bukan observasi independen.')
    rows=[]
    for iso in ISOS:
        r=primary[primary.model_id.eq(f'BIL_{iso}_ARDL_AIC4')].iloc[0]
        rows.append([COUNTRIES[iso],int(r.N),fmt(r.lr_q_b,3),pval(r.Dep_LR_p),pval(r.Dep_LR_p_BH),'✓' if r.Levels_supported5 else '—','✓' if r.Diagnostic_clean5 else '—'])
    table(s,['Mitra','N','LR q','p nominal','p BH','Levels','Diagnostik'],rows,y=1.70,h=4.98,widths=[3.1,.6,1.4,1.4,1.4,1.2,1.6],size=11.8)

    s=d.slide('Lampiran | Statistik variabel hasil transformasi pada sampel agregat',
        'N = 61 | 2011Q1–2026Q1 | nilai POS / NEG bergantung pada titik awal akumulasi seri.',
        'Sumber: output/diagnostics/oskooee/models/WORLD_NARDL_AIC4_design.dta.',
        'Mean dan SD adalah statistik sampel hasil transformasi yang benar-benar masuk model. NEG tidak diubah menjadi besaran positif. Konstanta dapat menyerap perubahan basis indeks atau titik awal kumulatif; slope tetap dibaca sesuai definisi q.')
    rows=[]
    labels={'y':'y = ln(M/X)','yd':'yd = ln(PDB IDN)','yf':'yf = ln(aktivitas 10 mitra)','q':'q = ln(REER BIS)','pos':'POS: apresiasi kumulatif','neg':'NEG: depresiasi kumulatif'}
    for key,row in e['log_descriptives'].iterrows():
        rows.append([labels[key],int(row['count']),fmt(row['mean'],3),fmt(row['std'],3),fmt(row['min'],3),fmt(row['max'],3)])
    table(s,['Variabel model','N','Rata-rata','SD','Minimum','Maksimum'],rows,y=1.80,h=3.98,widths=[4,.6,1.35,1.35,1.35,1.35],size=12.5)
    callout(s,'q naik = apresiasi. NEG tetap bertanda negatif; pembalikan tanda akan membalik interpretasi koefisien.',6.40,size=12.7)

    s=d.slide('Lampiran | Stabilitas dunia dan Australia memberi hasil berbeda',
        'CUSUMSQ residual rekursif | band simultan referensi Gaussian finite-sample, 19.999 simulasi.',
        'Sumber: stability_paths.csv; diagnostic_summary.csv. Band Monte Carlo aproksimasi, bukan tabel persis paper.',
        'Dunia NARDL p MC=0.0126. Australia NARDL tidak menolak stabilitas dalam flag gabungan. CUSUM memakai implementasi resmi Stata dan telah dicocokkan dengan konstruksi independen; CUSUMSQ dihitung melalui simulasi referensi dengan seed tetap.')
    picture(s,a['stability'],.65,1.86,12.0,4.28)
    callout(s,'Stabilitas memperkuat penilaian suatu spesifikasi, tetapi tidak mengubah hasil menjadi bukti kausal.',6.43,size=13)

    s=d.slide('Lampiran | Catatan data yang memengaruhi pembacaan hasil',
        'Integritas file dan validasi sumber mempunyai tujuan berbeda; beberapa isu harmonisasi masih terbuka.',
        'Sumber: audit_validitas_data_macro.md; sumber_data_macro_dan_merge.md; hasil_ardl_nardl_oskooee.md.',
        'Selisih impor GEM vs WDI 2006 maksimum24.283%. World start2010. CPI Australia interpolasi penyedia. India CPI mulai2013; WPI sensitivity terpisah. USA CPI October2025 missing dan VNM FX August2025 missing. Raw perdagangan asal CEIC/ITC tidak berada di Tio; checksum memastikan tidak berubah, bukan validasi penuh ke sumber asal.')
    table(s,['Isu','Implikasi / perlakuan'],[
        ['Dunia 2006–2009','Selisih impor antarsumber hingga 24,3%; baseline mulai 2010.'],
        ['Permintaan asing agregat','Proksi 10 mitra berbobot tetap; bukan PDB seluruh dunia.'],
        ['India / Australia','India CPI mulai 2013; WPI terpisah. CPI AUS interpolasi penyedia.'],
        ['Celah AS / Vietnam','AS berakhir 2025Q3; VNM 2025Q2. Celah tidak ditambal otomatis.'],
        ['Jenis barang','Cakupan 10 mitra; mixed dan unclassified tetap terpisah.'],
        ['Sumber perdagangan awal','Raw CEIC / Trade Map asal tidak tersedia di Tio untuk validasi penuh.'],
        ['Sensitivitas India + BCOM','N = 49, K = 25: critical values bounds finite-sample tidak tersedia.']],y=1.68,h=4.99,widths=[3.0,8.1],size=12.5)

    s=d.slide('Lampiran | Peta sumber dan konstruksi variabel',
        'Dokumentasi rinci dan respons sumber disimpan bersama manifest serta checksum.',
        'Sumber: Macro_Source_Manifest.csv; download_manifest.json; catatan audit; klasifikasi HS-4; workbook harga pengguna.',
        'Investing.com tidak berhasil diunduh (403); kurs yang dipakai berasal dari BIS, dengan GEM sebagai sensitivitas terpisah. Tidak ada klaim menggunakan data Investing. Data harga BCOM berasal dari workbook pengguna; transformasi dan audit dicatat dalam data_komoditas_den.md.')
    table(s,['Komponen','Sumber / konstruksi','Lokasi dokumentasi'],[
        ['Perdagangan dunia','World Bank GEM: merchandise, customs, nominal USD','sumber_data_macro_dan_merge.md'],
        ['Perdagangan bilateral / HS','Panel asal CEIC / Trade Map yang sudah ada','catatan_data_panel.md'],
        ['PDB riil IDN + mitra','GEM: level kuartalan SA → indeks 2015 = 100','Macro_Source_Manifest.csv'],
        ['Kurs dan CPI','BIS FX / CPI; CPI VNM dari GEM; RER silang','audit_validitas_data_macro.md'],
        ['REER / permintaan dunia','BIS REER; PDB 10 mitra, bobot ekspor 2006–2008','12_prepare_oskooee_models.py'],
        ['Komoditas / harga','HS-4 UNCTAD A11; BCOM dari workbook pengguna','klasifikasi_komoditas_hs4.md; data_komoditas_den.md']],y=1.73,h=4.76,widths=[2.4,5.6,4],size=11.7)

    s=d.slide('Lampiran | Hasil dapat dilacak ke data, kode, dan diagnostik',
        'Folder Tio | alur reproduksi terpisah dari pembuatan deck.',
        'Sumber: struktur proyek; master do-file dan wrapper pipeline; delivery_validation.json.',
        'Deck dibangun dari keluaran penelitian yang sudah divalidasi, tanpa mengestimasi ulang. CSV deskriptif dan grafik deck tersimpan di output/presentation/assets. Slide notes menyimpan sumber dan batas interpretasi. PPTX dapat diedit, PDF dan PNG dipakai untuk pemeriksaan visual.')
    table(s,['Kebutuhan','Lokasi di Tio/'],[
        ['Data mentah dan referensi','input/raw/; input/reference/'],
        ['Panel analisis kuartalan','intermediate/Oskooee_Quarterly_Analysis.csv'],
        ['Do-file / pipeline','script/00_master.do; 00_run_oskooee.ps1; 12–16'],
        ['Hasil lengkap dan tabel gambar','output/tables/oskooee/Oskooee_Results.xlsx; PNG / PDF'],
        ['Grafik dan format Stata','output/figures/oskooee/; output/gph/oskooee/'],
        ['Diagnostik / validasi','output/diagnostics/oskooee/'],
        ['Deck dan data grafiknya','output/presentation/; output/presentation/assets/']],y=1.72,h=4.87,widths=[3.5,8.5],size=12.4)

    s=d.slide('Lampiran | Referensi metodologi utama',
        'Referensi implementasi dan batas inferensi untuk membaca hasil penelitian.',
        'Sumber: paper pengguna dan referensi implementasi yang disimpan di input/reference/oskooee_replication/.',
        'Paper Bahmani-Oskooee online2015 dan volume jurnal2016. Implementasi ardl dan bounds Kripfganz–Schneider bukan klaim reproduksi persis critical values historis paper. CUSUMSQ aproksimasi MC ditandai. Dokumen audit sumber lokal memuat URL provenance masing-masing respons sumber.')
    steps(s,[('Bahmani-Oskooee & Fariditavana (2015 / 2016)','Nonlinear ARDL Approach and the J-Curve Phenomenon. Open Economies Review 27: 51–70. DOI: 10.1007/s11079-015-9369-5.'),
             ('Kripfganz & Schneider','ARDL dan inferensi bounds finite-sample. Implementasi Stata ardl 1.0.6. DOI artikel Stata Journal: 10.1177/1536867X231212434.'),
             ('Stata: estat sbcusum','CUSUM recursive dan pemeriksaan stabilitas. Dokumentasi: stata.com/manuals/tsestatsbcusum.pdf.'),
             ('Audit dan klasifikasi proyek Tio','Catatan sumber, manifest unduhan, UNCTAD A11 untuk HS-4, serta audit workbook harga komoditas.')],y=1.83,spacing=1.10)

    path=OUT/'Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pptx'
    d.p.save(str(path))
    (OUT/'slide_notes.md').write_text('\n\n'.join(f"## {r['slide']:02d}. {r['title']}\n\n{r['notes']}" for r in d.slides),encoding='utf-8')
    pd.DataFrame([{'Slide':r['slide'],'Judul':r['title']} for r in d.slides]).to_csv(OUT/'slide_index.csv',index=False,encoding='utf-8-sig')
    after={str(v.relative_to(ROOT)):digest(v) for v in files.values()}
    assert before==after,'Input data changed while building the deck'
    # The source master/layout/theme packages should remain byte-identical.
    with ZipFile(template) as src,ZipFile(path) as dst:
        parts=[n for n in src.namelist() if n.endswith('.xml') and n.startswith(('ppt/theme/','ppt/slideMasters/','ppt/slideLayouts/'))]
        matches={n:src.read(n)==dst.read(n) for n in parts}
    # python-pptx may reserialize XML; use canonical XML comparison if necessary.
    from lxml import etree
    with ZipFile(template) as src,ZipFile(path) as dst:
        canonical={n:etree.tostring(etree.fromstring(src.read(n)),method='c14n')==etree.tostring(etree.fromstring(dst.read(n)),method='c14n') for n in parts}
    report={'slides':len(d.p.slides),'template':str(template),'template_sha256':digest(template),
        'pptx_sha256':digest(path),'input_sha256':before,'input_unchanged':before==after,
        'original_master_layout_theme_xml_parts':len(parts),'preserved_xml_parts_canonical':sum(canonical.values()),
        'all_master_layout_theme_parts_preserved':all(canonical.values()),
        'main_models':len(primary),'sensitivity_models':len(allmodels)-len(primary),
        'world_estimation_N':int(e['descriptives'].N.min()),'render_validation':'pending'}
    (OUT/'deck_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    (OUT/'README.md').write_text('''# Deck penelitian: depresiasi rupiah dan trade balance

PPTX mengikuti cover, logo, master, layout, font dan tema benchmark pengguna. Isi merupakan hasil estimasi awal proyek Tio per 17 November 2026, bukan klaim pengesahan institusional.

- `Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pptx`: presentasi final editable. File tanpa akhiran `_final` adalah draf render awal.
- PDF dan `slides/`: hasil render PowerPoint jika tersedia.
- `assets/`: grafik PNG/PDF dan CSV statistik deskriptif yang dipakai dalam deck.
- `slide_notes.md`: sumber, definisi, narasi, dan batas interpretasi setiap slide.
- `deck_validation.json`: checksum, pelestarian template, dan pemeriksaan hasil.

Reproduksi: jalankan `script/17_build_research_deck.py`, lalu `script/18_render_research_deck.py`. Set `PYTHONPATH` sesuai paket proyek. Template disimpan pada `input/reference/presentation_template/`. Grafik ilmiah dibangun dengan matplotlib; teks dan tabel utama dalam PPT dapat diedit. Data mentah, panel, dan hasil estimasi tidak diubah.

Sampel: statistik agregat N=61 memakai tanggal desain estimasi 2011Q1–2026Q1. Grafik tahunan dan komposisi 2025 memakai tahun lengkap, dengan penyebut 10 mitra untuk grafik bilateral/jenis barang. Koefisien yang tidak mendapat dukungan levels tetap diperlihatkan dan ditandai. P-value/interval nominal setelah seleksi AIC; BH eksploratif bukan koreksi seleksi model.
''',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--template',type=Path,default=ROOT/'input/reference/presentation_template/Simulasi Nilai Tukar Rupiah_Meeting Sore_rev.pptx')
    args=parser.parse_args();build(args.template)
