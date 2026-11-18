"""Build the HS6 research deck from audited Stata results; no re-estimation."""
from pathlib import Path
import os,sys,json,hashlib,re,subprocess,math,textwrap
from zipfile import ZipFile
import numpy as np
import pandas as pd
from PIL import Image,ImageChops
import pymupdf as fitz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.opc.package import Part
from pptx.opc.packuri import PackURI
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.xmlchemy import OxmlElement
from pptx.oxml.ns import qn
from lxml import etree
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'script/python'))
import presentation_style as st
OUT=ROOT/'output/presentation';A=OUT/'assets';EQ=OUT/'equations'
for p in [OUT,A,EQ]:p.mkdir(parents=True,exist_ok=True)
T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee'
TEMPLATE=ROOT/'input/reference/presentation_template/Simulasi Nilai Tukar Rupiah_Meeting Sore_rev.pptx'
COUNTRIES={'WLD':'Dunia','AUS':'Australia','CHN':'Tiongkok','IND':'India','JPN':'Jepang',
 'KOR':'Korea Selatan','MYS':'Malaysia','SGP':'Singapura','THA':'Thailand','USA':'Amerika Serikat','VNM':'Vietnam'}
ISOS=list(COUNTRIES)[1:]
GROUPS={'manufacturing':'Non-komoditas manufaktur','consumption':'Barang konsumsi',
 'agriculture':'Komoditas pertanian & pangan','intermediate':'Bahan baku/penolong',
 'capital':'Barang modal','commodity':'Komoditas total','energy_mining':'Komoditas energi & tambang'}
COL=st.C
plt.rcParams.update({'font.family':'Arial','font.size':10,'mathtext.fontset':'cm',
 'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#4E3B30',
 'axes.edgecolor':'#B8ACA3','xtick.color':'#6B6B6B','ytick.color':'#6B6B6B',
 'figure.facecolor':'white','savefig.facecolor':'white','svg.fonttype':'path'})
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dec(v,n=2):
 if pd.isna(v):return '—'
 return f'{float(v):,.{n}f}'.replace(',','|').replace('.',',').replace('|','.')
def prob(v):
 return 'tidak tersedia' if pd.isna(v) else '<0,001' if v<.001 else dec(v,3)
def color(k):return '#'+COL[k]
def figure(fig,name):
 fig.savefig(A/(name+'.png'),dpi=185,bbox_inches='tight',pad_inches=.08)
 fig.savefig(A/(name+'.pdf'),bbox_inches='tight',pad_inches=.08)
 plt.close(fig);return A/(name+'.png')
def grid(ax,axis='y'):
 ax.grid(axis=axis,color=color('grid'),lw=.6);ax.set_axisbelow(True)
def human(row):
 if row.scope=='aggregate':return 'Indonesia–seluruh dunia'
 if row.scope=='bilateral':return 'Indonesia–'+COUNTRIES[row.ISO3]
 return COUNTRIES[row.ISO3]+' | '+GROUPS[row.Group]
def trade_label(row):
 partner='seluruh dunia' if row.ISO3=='WLD' else COUNTRIES[row.ISO3]
 return 'Indonesia–'+partner+(' | '+GROUPS[row.Group] if row.scope=='goods' else '')
def qualification(row):
 if not row.Levels_supported5:return 'Hubungan level belum didukung'
 return 'Level didukung; diagnostik memadai' if row.Diagnostic_clean5 else 'Level didukung; catatan diagnostik'
def coef(row):
 v='lr_q' if row.estimator=='ARDL' else 'lr_neg'
 return row[v+'_b'],row[v+'_lo95'],row[v+'_hi95'],row[v+'_p']
def response_data(model):
 a=DM[DM.model_id.eq(model)].copy()
 assert len(a)==50 and set(a.direction)=={'appreciation','depreciation'}
 a['J_response']=-a.effect_logpoints
 a['J_lower']=-a.upper95_logpoints
 a['J_upper']=-a.lower95_logpoints
 assert a.J_lower.le(a.J_response+1e-7).all() and a.J_upper.ge(a.J_response-1e-7).all()
 return a
def classify_curve(row):
 z=response_data(row.model_id);z=z[z.direction.eq('depreciation')].sort_values('horizon_quarters')
 early=z[z.horizon_quarters.le(4)];late=z[z.horizon_quarters.ge(16)]
 a=bool(early.J_response.lt(0).any());b=bool(late.J_response.mean()>0)
 ec=bool(early.J_upper.lt(0).any());lc=bool(z.iloc[-1].J_lower>0)
 label=('Pola J pada estimasi titik' if a and b else 'Perbaikan tanpa fase awal memburuk' if b else 'Akhir horizon belum membaik')
 if not row.Dynamic_stable:label='Respons dinamis tidak stabil'
 return {'model_id':row.model_id,'scope':row.scope,'scenario':row.scenario,'cap':row.cap,'ISO3':row.ISO3,'Group':row.Group,
  'estimator':row.estimator,'point_pattern':label,'early_negative_point':a,'late_positive_point':b,
  'early_CI_below_zero':ec,'terminal_CI_above_zero':lc,'phase_CI_separated':ec and lc,
  'response_impact':float(z.iloc[0].J_response),'response_q4':float(z.iloc[4].J_response),
  'response_q24':float(z.iloc[-1].J_response),'Levels_supported5':bool(row.Levels_supported5),
  'Diagnostic_clean5':bool(row.Diagnostic_clean5)}
def plot_response(ax,row,small=False,title=None):
 fs=8.5 if small else 11
 z=response_data(row.model_id)
 for direction,label,col in [('depreciation','Depresiasi','brown'),('appreciation','Apresiasi','blue')]:
  g=z[z.direction.eq(direction)].sort_values('horizon_quarters')
  ax.plot(g.horizon_quarters,g.J_response,color=color(col),lw=1.6 if small else 2.1,label=label)
  ax.fill_between(g.horizon_quarters,g.J_lower,g.J_upper,color=color(col),alpha=.13,lw=0)
 ax.axhline(0,color=color('gray'),lw=.8)
 ax.set_xlim(0,24);ax.set_xticks([0,4,8,12,16,20,24] if not small else [0,8,16,24])
 ax.tick_params(labelsize=fs-1)
 ax.set_xlabel('Kuartal setelah guncangan',fontsize=fs)
 ax.set_ylabel(r'$100\Delta\ln(X_t/M_t)$',fontsize=fs+2)
 ttl=title if title is not None else row.estimator+' | '+qualification(row)
 ax.set_title(ttl,fontsize=fs,fontweight='bold',loc='left',pad=7)
 grid(ax)
 if not small:ax.legend(loc='best',frameon=False,fontsize=9,ncol=2)
 # Each subplot uses its own scale. Never clip intervals to make results look precise.
 return ax
PAIR_ASSETS={};PAIR_SLIDES={}
def pair_asset(rows,key):
 if key in PAIR_ASSETS:return PAIR_ASSETS[key]
 fig,axes=plt.subplots(1,2,figsize=(11.7,3.35))
 for ax,est in zip(axes,['ARDL','NARDL']):
  r=rows[rows.estimator.eq(est)].iloc[0]
  plot_response(ax,r)
 fig.tight_layout(w_pad=2.4)
 path=figure(fig,'response_'+key)
 PAIR_ASSETS[key]=path
 return path
def sensitivity_grid(cases,key):
 fig,axs=plt.subplots(len(cases),2,figsize=(11.7,4.75 if len(cases)==2 else 2.5),squeeze=False)
 for i,(_,rows) in enumerate(cases):
  for j,est in enumerate(['ARDL','NARDL']):
   r=rows[rows.estimator.eq(est)].iloc[0]
   desc=human(r)
   if len(desc)>42:desc=desc[:40]+'…'
   plot_response(axs[i,j],r,small=True,title=desc+' | '+est)
 for ax in axs.flat:ax.legend(frameon=False,fontsize=7,loc='best',ncol=2)
 fig.tight_layout(h_pad=1.2,w_pad=2.2)
 return figure(fig,'sensitivity_'+key)
def forest_frame(frame,name,scope='goods'):
 fig,axes=plt.subplots(1,2,figsize=(11.7,4.15))
 for ax,est in zip(axes,['ARDL','NARDL']):
  a=frame[frame.estimator.eq(est)].copy()
  order=list(GROUPS) if scope=='goods' else ISOS
  a['order']=a.Group.map({x:i for i,x in enumerate(order)}) if scope=='goods' else a.ISO3.map({x:i for i,x in enumerate(order)})
  a=a.sort_values('order')
  for j,r in enumerate(a.itertuples()):
   b,lo,hi,p=coef(pd.Series(r._asdict()))
   co='brown' if r.Levels_supported5 and r.Diagnostic_clean5 else 'gold' if r.Levels_supported5 else 'gray'
   ax.plot([lo,hi],[j,j],color=color(co),lw=1.7)
   ax.scatter([b],[j],s=35,edgecolor=color(co),facecolor=color(co) if r.Levels_supported5 else 'white',zorder=3)
  ax.axvline(0,color=color('red'),lw=.9)
  lab=[GROUPS[r.Group] if scope=='goods' else COUNTRIES[r.ISO3] for r in a.itertuples()]
  lab=[x.replace('Komoditas pertanian & pangan','Pertanian & pangan').replace('Non-komoditas manufaktur','Manufaktur nonkomoditas').replace('Komoditas energi & tambang','Energi & tambang') for x in lab]
  ax.set_yticks(range(len(a)),lab,fontsize=9);ax.invert_yaxis()
  ax.set_xlabel(r'$\beta_q$' if est=='ARDL' else r'$\beta_-$',fontsize=14)
  ax.set_title(est+' | interval nominal 95%',fontsize=11,fontweight='bold')
  grid(ax,'x')
 handles=[Line2D([],[],marker='o',ls='',color=color('brown'),label='Level + diagnostik'),
  Line2D([],[],marker='o',ls='',color=color('gold'),label='Level; catatan diagnostik'),
  Line2D([],[],marker='o',ls='',color=color('gray'),markerfacecolor='white',label='Level belum didukung')]
 fig.legend(handles=handles,loc='lower center',ncol=3,frameon=False,fontsize=9)
 fig.tight_layout(rect=(0,.08,1,1),w_pad=2)
 return figure(fig,name)
FORMULAS={
 'outcome':r'y_t=\ln\!\left(\frac{M_t}{X_t}\right),\qquad TB_t=X_t-M_t',
 'income':r'd_t=\ln Y_{\mathrm{IDN},t},\qquad f_t=\ln Y_{\mathrm{mitra},t}',
 'qworld':r'q_t=\ln(\mathrm{REER}_t),\qquad q_t\uparrow\ \Longleftrightarrow\ \mathrm{apresiasi}',
 'qbilateral':r'q_{i,t}=-\ln(\mathrm{RER}_{i,t})',
 'partial':r'q_t^+=\sum_{s=1}^{t}\max(\Delta q_s,0),\qquad q_t^-=\sum_{s=1}^{t}\min(\Delta q_s,0)',
 'lr_ardl':r'y_t=\alpha+\beta_d d_t+\beta_f f_t+\beta_q q_t+u_t',
 'lr_nardl':r'y_t=\alpha+\beta_d d_t+\beta_f f_t+\beta_+q_t^++\beta_-q_t^-+u_t',
 'uecm':r'\begin{aligned}\Delta y_t={}&a+\rho y_{t-1}+\theta_d d_{t-1}+\theta_f f_{t-1}+\theta_+q_{t-1}^{+}+\theta_-q_{t-1}^{-}\\ &+\sum_{j=1}^{P}\phi_j\Delta y_{t-j}+\sum_{j=0}^{Q_d}\gamma_{d,j}\Delta d_{t-j}+\sum_{j=0}^{Q_f}\gamma_{f,j}\Delta f_{t-j}\\ &+\sum_{j=0}^{Q_+}\pi_j^+\Delta q_{t-j}^++\sum_{j=0}^{Q_-}\pi_j^-\Delta q_{t-j}^-+\varepsilon_t\end{aligned}',
 'lr_normalize':r'\beta_-=-\frac{\theta_-}{\rho},\qquad \beta_+=-\frac{\theta_+}{\rho},\qquad \rho<0',
 'asymmetry':r'H_0^{\mathrm{LR}}:\ \beta_+=\beta_-,\qquad H_0^{\mathrm{SR}}:\ \sum_j\pi_j^+=\sum_j\pi_j^-',
 'bounds':r'H_0:\ \rho=\theta_d=\theta_f=\theta_+=\theta_-=0',
 'display':r'R_h^{J}=-100\,\Delta_h y=100\,\Delta_h\ln\!\left(\frac{X}{M}\right)',
 'shock':r'\Delta q^-=-\ln(1.10),\qquad \Delta q^+=+\ln(1.10)',
 'effect':r'\Delta y_{\infty}^{-}=\beta_-\,\Delta q^-,\qquad \beta_->0,\ \Delta q^-<0\ \Longrightarrow\ \Delta y_\infty^-<0',
 'multiplier':r'm_h^{\pm}=\frac{\partial y_{t+h}}{\partial q_t^\pm},\qquad R_h^{J,\pm}=-100\,m_h^\pm\Delta q^\pm',
 'jcriterion':r'\min_{0\leq h\leq4}R_h^{J,-}<0,\qquad \frac{1}{9}\sum_{h=16}^{24}R_h^{J,-}>0',
 'pricecontrol':r'y_t=\alpha+\beta_d d_t+\beta_f f_t+\beta_+q_t^++\beta_-q_t^-+\beta_c\ln(\mathrm{BCOM}_t)+u_t',
 'weights':r'f_t=\ln\!\left(\sum_{i=1}^{10}w_iY_{i,t}^{(2015=100)}\right),\qquad \sum_{i=1}^{10}w_i=1',
 'var_y':r'y_t','var_d':r'd_t','var_f':r'f_t','var_q':r'q_t',
 'var_pos':r'q_t^+','var_neg':r'q_t^-','var_c':r'\ln(\mathrm{BCOM}_t)',
 'beta_q':r'\beta_q','beta_neg':r'\beta_-','beta_pos':r'\beta_+',
 'i2':r'I(0),\ I(1),\ I(2)','elasticity':r'\beta_-','n':r'N'
}
def render_equations():
 tex=[r'\documentclass{article}',r'\usepackage[paperwidth=13in,paperheight=3.6in,margin=0.15in]{geometry}',
  r'\usepackage{amsmath,amssymb}',r'\pagestyle{empty}',r'\setlength{\parindent}{0pt}',
  r'\begin{document}',r'\fontsize{22}{30}\selectfont']
 for i,(key,value) in enumerate(FORMULAS.items()):
  if i:tex.append(r'\newpage')
  tex.append(r'\vspace*{0.15in}\noindent\(\displaystyle '+value+r'\)')
  (EQ/(key+'.tex')).write_text(value,encoding='utf-8')
 tex.append(r'\end{document}')
 (EQ/'all_formulas.tex').write_text('\n'.join(tex),encoding='utf-8')
 exe=Path('C:/Users/Administrator/AppData/Roaming/TinyTeX/bin/windows/pdflatex.exe')
 result=subprocess.run([str(exe),'-interaction=nonstopmode','-halt-on-error','-no-shell-escape',
  '-output-directory='+str(EQ),str(EQ/'all_formulas.tex')],cwd=EQ,capture_output=True,text=True,encoding='utf-8',errors='replace')
 (EQ/'latex_build.log').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
 if result.returncode:raise RuntimeError('LaTeX compilation failed; see equations/latex_build.log')
 doc=fitz.open(EQ/'all_formulas.pdf')
 assert len(doc)==len(FORMULAS),(len(doc),len(FORMULAS))
 for page,(key,value) in zip(doc,FORMULAS.items()):
  pix=page.get_pixmap(matrix=fitz.Matrix(3.5,3.5),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  bounds=ImageChops.difference(im,Image.new('RGB',im.size,'white')).getbbox()
  assert bounds,key
  l,t,r,b=bounds;pad=12
  im.crop((max(0,l-pad),max(0,t-pad),min(im.width,r+pad),min(im.height,b+pad))).save(EQ/(key+'.png'))
  rect=fitz.Rect(max(0,l-pad)/3.5,max(0,t-pad)/3.5,min(im.width,r+pad)/3.5,min(im.height,b+pad)/3.5)
  page.set_cropbox(rect)
  (EQ/(key+'.svg')).write_text(page.get_svg_image(text_as_path=True),encoding='utf-8')
 doc.close()
 (EQ/'formula_manifest.json').write_text(json.dumps(FORMULAS,indent=2,ensure_ascii=False),encoding='utf-8')
SVG_PARTS={}
def mathbox(slide,key,x,y,w,h):
 sh=st.picture(slide,EQ/(key+'.png'),x,y,w,h)
 if key not in SVG_PARTS:
  SVG_PARTS[key]=Part(PackURI('/ppt/media/latex_'+key+'.svg'),'image/svg+xml',slide.part.package,(EQ/(key+'.svg')).read_bytes())
 rid=slide.part.relate_to(SVG_PARTS[key],RT.IMAGE)
 blip=sh._pic.blipFill.blip
 exts=OxmlElement('a:extLst');ext=OxmlElement('a:ext');ext.set('uri','{96DAC541-7B7A-43D3-8B79-37D633B846F1}')
 svg=etree.Element('{http://schemas.microsoft.com/office/drawing/2016/SVG/main}svgBlip')
 svg.set(qn('r:embed'),rid);ext.append(svg);exts.append(ext);blip.append(exts)
 sh.name='LaTeX: '+key
 sh._pic.nvPicPr.cNvPr.set('descr',FORMULAS[key])
 return sh
def paragraph(slide,title,body,x=8.75,y=1.8,w=3.75,h=3.9):
 st.text(slide,x,y,w,.6,title,16,'brown',True)
 st.text(slide,x,y+.7,w,h-.7,body,14,'ink')
def note_row(row):
 b,lo,hi,p=coef(row);classification=CURVES.set_index('model_id').loc[row.model_id]
 direction='mengarah pada perbaikan' if b>0 else 'mengarah pada pemburukan'
 return (f'{row.estimator}: sampel estimasi {row.Estimation_Start} sampai {row.Estimation_End}, {int(row.N)} kuartal. '
 f'Lag level {row.lag_order}. Koefisien kurs yang relevan untuk depresiasi {dec(b,4)}, '
 f'interval nominal 95% [{dec(lo,4)}; {dec(hi,4)}], probabilitas nominal {prob(p)}. '
 f'Dengan definisi kurs penelitian, tanda ini {direction} neraca pada depresiasi. '
 f'{qualification(row)}. Flag lengkap: {row.Diagnostic_Flags}. '
 f'Pemeriksaan visual-operasional: {classification.point_pattern}. Respons kuartal pertama {dec(classification.response_impact)}, '
 f'kuartal keempat {dec(classification.response_q4)}, kuartal ke-24 {dec(classification.response_q24)} poin log kali seratus. '
 'Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.')
def load():
 global ALL,PRIMARY,DM,CURVES,TOTAL,GOODS,REG
 ALL=pd.read_csv(T/'results_all_models.csv');PRIMARY=pd.read_csv(T/'results_primary_models.csv')
 DM=pd.read_csv(D/'dynamic_multipliers.csv')
 TOTAL=pd.read_csv(ROOT/'intermediate/Trade_Total_Quarter.csv')
 GOODS=pd.read_csv(ROOT/'intermediate/Trade_Goods_Quarter.csv')
 REG=pd.read_csv(D/'case_registry.csv')
 assert len(ALL)==516 and len(PRIMARY)==176
 assert set(DM.model_id)==set(ALL.model_id)
 CURVES=pd.DataFrame([classify_curve(r) for _,r in ALL.iterrows()])
 CURVES.to_csv(A/'jcurve_classification_all_516.csv',index=False,float_format='%.12g')
def prepare_assets():
 assets={};facts={}
 w=TOTAL[TOTAL.ISO3.eq('WLD')].copy();w['Year']=w.Quarter.str[:4].astype(int)
 annual=w.groupby('Year')[['Exports_USDk','Imports_USDk','Trade_Balance_USDk']].sum(min_count=4)/1e6
 annual=annual.loc[2006:2025];annual.rename(columns={c:c.replace('_USDk','_USDbn') for c in annual.columns}).assign(Reporter='Indonesia',Partner='All partners').to_csv(A/'world_annual_USDbn.csv')
 facts['world2025']={k.replace('_USDk','_USDbn'):v for k,v in annual.loc[2025].to_dict().items()}
 fig,ax=plt.subplots(2,1,figsize=(10.8,4.25),sharex=True,gridspec_kw={'height_ratios':[1.6,1]})
 ax[0].plot(annual.index,annual.Exports_USDk,color=color('brown'),lw=2.3,label='Ekspor')
 ax[0].plot(annual.index,annual.Imports_USDk,color=color('dark'),lw=2.1,label='Impor')
 ax[0].set_ylabel('USD miliar');ax[0].legend(frameon=False,ncol=2);grid(ax[0])
 ax[1].bar(annual.index,annual.Trade_Balance_USDk,color=[color('brown') if v>=0 else color('gold') for v in annual.Trade_Balance_USDk])
 ax[1].axhline(0,color=color('gray'),lw=.7);ax[1].set_ylabel('Neraca, USD miliar');grid(ax[1])
 ax[1].set_xticks([2006,2010,2014,2018,2022,2025]);fig.tight_layout()
 assets['world']=figure(fig,'world_flows_annual')
 p=TOTAL[TOTAL.ISO3.ne('WLD')&TOTAL.Quarter.str.startswith('2025')].groupby('ISO3')[['Exports_USDk','Imports_USDk']].sum(min_count=4)/1e6
 p['Net']=p.Exports_USDk-p.Imports_USDk
 p['Share_World_Exports']=100*p.Exports_USDk/facts['world2025']['Exports_USDbn']
 p.rename(columns={'Exports_USDk':'Exports_USDbn','Imports_USDk':'Imports_USDbn','Net':'Trade_Balance_USDbn','Share_World_Exports':'Share_of_Indonesia_Total_Exports_pct'}).rename_axis('Partner_ISO3').assign(Reporter='Indonesia').to_csv(A/'partner_trade_2025.csv')
 facts['partner_export_share']=float(p.Share_World_Exports.sum())
 facts['partner_import_share']=float(100*p.Imports_USDk.sum()/facts['world2025']['Imports_USDbn'])
 fig,axes=plt.subplots(1,2,figsize=(11.8,4.2),gridspec_kw={'width_ratios':[1.4,1]})
 ps=p.sort_values('Exports_USDk')
 y=np.arange(10);axes[0].barh(y+.18,ps.Exports_USDk,.33,color=color('brown'),label='Ekspor')
 axes[0].barh(y-.18,ps.Imports_USDk,.33,color=color('dark'),label='Impor')
 axes[0].set_yticks(y,[COUNTRIES[x] for x in ps.index]);axes[0].set_xlabel('USD miliar');axes[0].legend(frameon=False,ncol=2);grid(axes[0],'x')
 axes[1].barh(y,ps.Share_World_Exports,color=color('brown'));axes[1].set_yticks(y,ps.index);axes[1].set_xlabel('Pangsa ekspor terhadap dunia (%)')
 for i,v in enumerate(ps.Share_World_Exports):axes[1].text(v+.2,i,dec(v,1),va='center',fontsize=9)
 axes[1].set_xlim(0,ps.Share_World_Exports.max()*1.18);grid(axes[1],'x');fig.tight_layout(w_pad=2)
 assets['partner_trade']=figure(fig,'partner_trade_2025')
 coverage=pd.read_csv(ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv')
 c=coverage[coverage.ISO3.eq('WLD')&coverage.Year.eq(2025)]
 facts['classification_2025']=c.to_dict('records')
 for kind,name,labels,colors in [
 ('Commodity_Class','composition_commodity',{'commodity':'Komoditas','noncommodity':'Manufaktur nonkomoditas','mixed':'Campuran','unclassified':'Belum terpetakan'},['brown','dark','gold','light']),
 ('BEC5_EndUse','composition_BEC',{'intermediate':'Bahan baku/penolong','capital':'Modal','consumption':'Konsumsi','mixed':'Campuran','unclassified':'Belum terpetakan'},['brown','dark','gold','gray','light'])]:
  z=c[c.Classification.eq(kind)].pivot(index='Class',columns='Flow',values='Value_Share_pct').reindex(list(labels)).fillna(0)
  fig,ax=plt.subplots(figsize=(11,2.8));left=np.zeros(2)
  for (cls,label),co in zip(labels.items(),colors):
   vals=z.loc[cls,['Export','Import']].to_numpy()
   ax.barh([1,0],vals,left=left,height=.5,color=color(co),label=label)
   for j,v in enumerate(vals):
    if v>7:ax.text(left[j]+v/2,[1,0][j],dec(v,1)+'%',ha='center',va='center',color='white' if co!='light' else color('ink'),fontsize=13,fontweight='bold')
   left+=vals
  ax.set_yticks([1,0],['Ekspor','Impor']);ax.set_xlim(0,100);ax.set_xlabel('Pangsa nilai rincian HS-6 (%)')
  ax.legend(loc='upper center',bbox_to_anchor=(.5,-.23),ncol=3 if kind=='BEC5_EndUse' else 4,frameon=False,fontsize=9)
  ax.spines[['top','right','left']].set_visible(False);assets[name]=figure(fig,name)
 g=GOODS[GOODS.ISO3.eq('WLD')&GOODS.Quarter.str.startswith('2025')].groupby('Group')[['Exports_USDk','Imports_USDk']].sum(min_count=4)/1e6
 g=g.reindex(list(GROUPS));g.rename(columns={c:c.replace('_USDk','_USDbn') for c in g.columns}).assign(Reporter='Indonesia',Partner='All partners').to_csv(A/'world_goods_2025_USDbn.csv')
 fig,ax=plt.subplots(figsize=(10.8,4))
 y=np.arange(7);ax.barh(y+.17,g.Exports_USDk,.32,color=color('brown'),label='Ekspor')
 ax.barh(y-.17,g.Imports_USDk,.32,color=color('dark'),label='Impor')
 ax.set_yticks(y,list(GROUPS.values()),fontsize=10);ax.invert_yaxis();ax.set_xlabel('USD miliar pada 2025');ax.legend(frameon=False,ncol=2);grid(ax,'x');fig.tight_layout()
 assets['goods_trade']=figure(fig,'world_goods_trade_2025')
 design=pd.read_stata(D/'models/WORLD_NARDL_AIC4_design.dta',convert_dates=False)
 dates=[str(pd.Period('1960Q1',freq='Q')+int(v)) for v in design.tq]
 sample=w.set_index('Quarter').loc[dates].copy()
 specs=[('Ekspor, USD miliar','Exports_USDk',1e6),('Impor, USD miliar','Imports_USDk',1e6),
 ('Neraca, USD miliar','Trade_Balance_USDk',1e6),('PDB riil Indonesia, indeks','IDN_GDP_Real_Index_2015mean100',1),
 ('Aktivitas luar negeri, indeks','Foreign_Activity_Top10_FixedWeight_Index',1),('REER, indeks','REER_BIS_broad',1)]
 desc=[]
 for label,col,div in specs:
  v=sample[col]/div;desc.append([label,int(v.count()),v.mean(),v.std(ddof=1),v.min(),v.max()])
 desc=pd.DataFrame(desc,columns=['Variabel','Kuartal','Rata-rata','Simpangan baku','Minimum','Maksimum'])
 desc.to_csv(A/'descriptive_world_estimation_sample.csv',index=False)
 facts['descriptive_rows']=[[r[0],str(r[1])]+[dec(v) for v in r[2:]] for r in desc.itertuples(index=False,name=None)]
 facts['world_sample']=[dates[0],dates[-1],len(dates)]
 fig,axes=plt.subplots(2,1,figsize=(10.8,4),sharex=True)
 axes[0].plot(np.arange(len(design)),np.exp(design.y),color=color('brown'),lw=1.8)
 axes[0].axhline(1,color=color('gray'),lw=.7);axes[0].set_ylabel(r'$M_t/X_t$',fontsize=14);grid(axes[0])
 axes[1].plot(np.arange(len(design)),np.exp(design.q),color=color('dark'),lw=1.8)
 axes[1].set_ylabel('REER, indeks');grid(axes[1]);ticks=np.arange(0,len(dates),8)
 axes[1].set_xticks(ticks,np.array(dates)[ticks],rotation=20);fig.tight_layout()
 assets['world_macro']=figure(fig,'world_ratio_and_REER')
 reg=PRIMARY[PRIMARY.scope.eq('bilateral')&PRIMARY.estimator.eq('NARDL')].set_index('ISO3')
 fig,ax=plt.subplots(figsize=(11,3.8))
 for i,iso in enumerate(ISOS):
  r=reg.loc[iso];first=pd.Period(r.Estimation_Start,freq='Q');last=pd.Period(r.Estimation_End,freq='Q')
  x1=first.year+(first.quarter-1)/4;x2=last.year+(last.quarter-1)/4
  ax.plot([x1,x2],[i,i],color=color('brown'),lw=9,solid_capstyle='butt')
  ax.text(x2+.2,i,f'{r.Estimation_Start}–{r.Estimation_End} | {int(r.N)} kuartal',fontsize=9,va='center')
 ax.set_yticks(range(10),[COUNTRIES[x] for x in ISOS]);ax.invert_yaxis();ax.set_xlim(2006,2033)
 ax.set_xticks([2007,2011,2015,2019,2023,2026]);grid(ax,'x');fig.tight_layout()
 assets['coverage']=figure(fig,'estimation_windows')
 fig,ax=plt.subplots(figsize=(10.8,3.3))
 h=np.arange(25);v=-8*np.exp(-h/3)+6*(1-np.exp(-h/8))
 ax.plot(h,v,color=color('brown'),lw=2.5);ax.axhline(0,color=color('gray'),lw=.8)
 ax.axvspan(0,4,color=color('beige'));ax.set_xlabel('Kuartal setelah depresiasi')
 ax.set_ylabel(r'$R_h^J$',fontsize=16);ax.set_yticks([]);ax.set_xticks([0,4,8,12,16,20,24])
 ax.text(1,-6.4,'Penyesuaian kontrak dan harga',fontsize=10)
 ax.text(10,2.5,'Respons volume mulai mendominasi',fontsize=10);grid(ax)
 assets['theory_J']=figure(fig,'theoretical_J_illustration')
 assets['forest_bilateral']=forest_frame(PRIMARY[PRIMARY.scope.eq('bilateral')],'forest_bilateral','bilateral')
 for iso in COUNTRIES:
  assets['forest_'+iso]=forest_frame(PRIMARY[PRIMARY.scope.eq('goods')&PRIMARY.ISO3.eq(iso)],'forest_goods_'+iso)
 diag=[('Korelasi serial','bg4_p'),('Heteroskedastisitas','hetero_p'),('RESET','reset_p'),
 ('Normalitas residual','JB_p'),('ARCH','ARCH4_p'),('CUSUMSQ','CUSUMSQ_p_MC')]
 vals=[int(PRIMARY[k].lt(.05).sum()) for _,k in diag]
 vals.append(int((~PRIMARY.CUSUM_stable5).sum()));labs=[x[0] for x in diag]+['CUSUM']
 fig,ax=plt.subplots(figsize=(10.8,3.7));ax.barh(range(7),vals,color=color('brown'),height=.58)
 ax.set_yticks(range(7),labs);ax.invert_yaxis()
 for i,v in enumerate(vals):ax.text(v+.4,i,f'{v} dari 176',va='center',fontsize=10)
 ax.set_xlim(0,max(vals)*1.25);ax.set_xlabel('Jumlah penolakan pada taraf 5%');grid(ax,'x');fig.tight_layout()
 assets['diagnostics']=figure(fig,'diagnostic_rejections')
 stability=pd.read_csv(D/'stability_paths.csv')
 fig,axes=plt.subplots(1,3,figsize=(11.8,3.3))
 for ax,model,label in zip(axes,['WORLD_NARDL_AIC4','BIL_AUS_NARDL_AIC4','BIL_MYS_NARDL_AIC4'],['Dunia','Australia','Malaysia']):
  z=stability[stability.model_id.eq(model)];x=1960+z.tq/4
  ax.fill_between(x,z.lower,z.upper,color=color('beige'));ax.plot(x,z.expected,':',color=color('gray'))
  ax.plot(x,z.CUSUMSQ,color=color('brown'),lw=1.8);ax.set_title(label,fontsize=12,fontweight='bold')
  ax.set_xlabel('Tahun');ax.set_ylim(-.05,1.05);grid(ax)
  pv=PRIMARY.set_index('model_id').loc[model,'CUSUMSQ_p_MC'];ax.text(.02,.92,'Probabilitas '+prob(pv),transform=ax.transAxes,fontsize=9)
 fig.tight_layout(w_pad=2);assets['stability']=figure(fig,'CUSUMSQ_world_AUS_MYS')
 counts=CURVES[CURVES.model_id.isin(PRIMARY.model_id)].groupby(['estimator','point_pattern']).size().unstack(fill_value=0)
 counts.to_csv(A/'jcurve_point_pattern_counts_primary.csv')
 facts['pattern_counts']=counts.to_dict()
 facts['assets']= {k:str(v.name) for k,v in assets.items()}
 (A/'descriptive_facts.json').write_text(json.dumps(facts,indent=2,ensure_ascii=False),encoding='utf-8')
 return assets,facts

def body_slide(d,title,subtitle,left_title,left_body,right_title,right_body,notes,source='Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.'):
 s=d.slide(title,subtitle,source,notes)
 st.box(s,.67,1.78,5.82,4.95,'beige')
 st.text(s,.87,1.98,5.4,.72,left_title,18,'brown',True)
 st.text(s,.87,2.83,5.35,3.6,left_body,16)
 st.text(s,6.95,1.99,5.35,.72,right_title,18,'brown',True)
 st.text(s,6.95,2.83,5.4,3.6,right_body,16)
 return s
def graph_slide(d,title,subtitle,path,body,notes,source='Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.'):
 s=d.slide(title,subtitle,source,notes)
 st.picture(s,path,.66,1.66,12.0,4.23)
 st.box(s,.67,6.05,11.98,.79,'beige')
 st.text(s,.84,6.12,11.62,.65,body,13.5,'dark')
 return s
def table_slide(d,title,subtitle,headers,rows,notes,source='Sumber: keluaran Stata proyek Tio.',widths=None,size=12):
 s=d.slide(title,subtitle,source,notes)
 height=min(4.9,max(1.5,.53*(len(rows)+1)))
 st.table(s,headers,rows,x=.67,y=1.75,w=12,h=height,widths=widths,size=size)
 if len(rows)<=4:
  summary=' '.join(re.split(r'(?<=[.!?])\s+',notes)[:3])
  st.text(s,.85,2.0+height,11.55,1.7,textwrap.shorten(summary,width=650,placeholder='…'),15,'dark')
 return s
def section(d,code,title,description):
 s=d.slide(title,'Lampiran lengkap | gunakan daftar isi untuk berpindah bagian.',
  'Sumber: keluaran estimasi Stata HS-6; seluruh spesifikasi tetap ditampilkan.',
  description)
 st.box(s,.67,1.85,11.98,4.75,'beige')
 st.text(s,1.0,2.2,2.0,1.15,code,60,'brown',True)
 st.text(s,3.2,2.35,8.8,1.1,title,25,'dark',True)
 st.text(s,3.2,3.85,8.8,1.95,description,19,'dark')
 return s
def pair_for(series,cap=4):
 z=PRIMARY[PRIMARY.series_id.eq(series)&PRIMARY.cap.eq(cap)]
 if z.empty:z=ALL[ALL.series_id.eq(series)&ALL.cap.eq(cap)]
 assert len(z)==2,(series,len(z))
 return z
def model_table_row(r):
 b,lo,hi,p=coef(r)
 return [r.estimator,str(int(r.N)),r.lag_order,dec(b,3),prob(p),
   'Didukung' if r.Levels_supported5 else 'Belum',
   'Memadai' if r.Diagnostic_clean5 else 'Catatan']
def body_pair(d,series,title,body,source=None):
 z=pair_for(series);path=pair_asset(z,series)
 notes='\n\n'.join(note_row(r) for _,r in z.iterrows())
 return graph_slide(d,title,
  'Garis cokelat: depresiasi; biru: apresiasi. Positif berarti rasio ekspor terhadap impor membaik.',
  path,body,notes,source or 'Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.')
def plot_selected_nardl(ids,name,ncol=2):
 a=PRIMARY[PRIMARY.series_id.isin(ids)&PRIMARY.estimator.eq('NARDL')]
 nrow=math.ceil(len(a)/ncol);fig,axes=plt.subplots(nrow,ncol,figsize=(11.7,4.5),squeeze=False)
 for ax,(_,r) in zip(axes.flat,a.iterrows()):plot_response(ax,r,small=True,title=human(r))
 for ax in list(axes.flat)[len(a):]:ax.set_visible(False)
 for ax in axes.flat:
  if ax.get_visible():ax.legend(fontsize=7,frameon=False,ncol=2)
 fig.tight_layout(w_pad=2,h_pad=1.8)
 return figure(fig,name)
def add_navigation(slide,target,label='Kembali ke daftar isi'):
 sh=st.text(slide,.69,6.91,2.35,.19,label,8,'brown')
 sh.click_action.target_slide=target
def main_slides(d,a,f):
 d.cover()
 cover=d.p.slides[0]
 cover.placeholders[1].text='HS-6 | ARDL dan NARDL: dunia, 10 mitra, dan tujuh kelompok barang\n17 November 2026 | Penelitian Tio'
 for p in cover.placeholders[1].text_frame.paragraphs:
  p.font.name='Arial Nova';p.font.size=Pt(14);p.font.bold=True;p.font.color.rgb=st.rgb('white');p.alignment=PP_ALIGN.CENTER
 d.slides[0]['notes']='Penelitian Tio berdasarkan 22 workbook Trade Map HS-6 dan 516 estimasi Stata. Template cover, foto, font dan palet mengikuti benchmark pengguna. Deck utama menguraikan hasil; deck lengkap melampirkan semua respons utama dan sensitivitas.'
 cover.notes_slide.notes_text_frame.text=d.slides[0]['notes']
 s=body_slide(d,'Apakah depresiasi selalu memperbaiki neraca perdagangan?',
  'Pertanyaan penelitian: respons nilai perdagangan Indonesia setelah kurs riil berubah.',
  'Pengalaman tiap pasar tidak harus sama',
  'Depresiasi mengubah harga relatif, tetapi kemampuan perdagangan meresponsnya bergantung pada jenis barang, struktur pasar dan waktu penyesuaian. Karena itu, satu koefisien agregat dapat menyamarkan respons yang berbeda.',
  'Apa yang diuji dalam penelitian ini',
  'Analisis membandingkan perdagangan dengan Indonesia–seluruh dunia, sepuluh mitra dan tujuh kelompok barang. Fokusnya adalah neraca perdagangan bernilai nominal. Respons ekspor saja dan kandungan input impor belum diidentifikasi.',
  'Hipotesis penelitian adalah bahwa depresiasi tidak memberikan manfaat yang seragam bagi neraca Indonesia. Hipotesis tersebut lebih sempit daripada pernyataan bahwa depresiasi selalu merugikan: beberapa pasar atau jenis barang dapat membaik, sebagian tidak berubah secara terukur, dan sebagian lain memburuk. Kerangka dinamis digunakan karena penyesuaian tidak harus selesai pada kuartal yang sama. Perlu dijaga batas antara pertanyaan tentang ekspor dan pertanyaan tentang neraca. Model mengamati impor relatif terhadap ekspor, sehingga perubahan keduanya dapat menghasilkan pola yang sama.')
 s=body_slide(d,'Seluruh analisis berpusat pada ekspor dan impor Indonesia',
  'Urutan pembahasan membedakan gambaran data, hasil model, dan penafsiran ekonomi.',
  'Tiga cakupan perdagangan Indonesia',
  'Agregat: ekspor Indonesia ke seluruh negara dan impor Indonesia dari seluruh negara.\n\nBilateral: arus Indonesia dengan masing-masing sepuluh mitra.\n\nKelompok barang: arus Indonesia yang dirinci menurut kategori hasil klasifikasi HS-6.',
  'HS-6 menjadi dasar tujuh kelompok',
  'File produk tersedia per HS-6. Regresi barang saat ini dijalankan untuk tujuh kelompok hasil klasifikasi, belum untuk tiap kode HS-6 secara terpisah.\n\nWorld atau WLD adalah mitra agregat. Negara pelapor pada seluruh file tetap Indonesia.',
  'Deck utama dibangun untuk pembahasan penelitian. Bagian lampiran dalam versi lengkap berfungsi sebagai atlas: setiap seri utama memiliki halaman ARDL dan NARDL yang berdampingan; sensitivitas disusun menurut perubahan spesifikasi. Grafik koefisien menyajikan interval agar pembaca dapat melihat ketepatan estimasi. Rangkaian ini mencegah pemilihan hanya model yang tampak sesuai hipotesis.')
 w=f['world2025']
 graph_slide(d,'Surplus perdagangan tidak dengan sendirinya mengungkapkan pengaruh kurs',
  'Perdagangan barang Indonesia dengan dunia, 2006–2025; hanya tahun lengkap.',
  a['world'],f"Pada 2025, ekspor mencapai USD {dec(w['Exports_USDbn'])} miliar dan impor USD {dec(w['Imports_USDbn'])} miliar. Surplus USD {dec(w['Trade_Balance_USDbn'])} miliar adalah hasil banyak faktor, bukan ukuran efek depresiasi.",
  'Grafik ini adalah statistik deskriptif dari baris TOTAL workbook Indonesia–seluruh dunia, bukan fitted value model. Nilai nominal dipengaruhi harga, volume, permintaan domestik, aktivitas mitra dan perubahan komposisi. Episode surplus juga dapat bertepatan dengan penguatan harga komoditas atau lemahnya impor. Tanpa desain identifikasi tambahan, arah kurs pada suatu tahun tidak dapat diberi tanggung jawab atas seluruh perubahan neraca. Data Juli–Agustus 2026 belum merupakan kuartal atau tahun lengkap dan tidak dipakai dalam grafik tahunan ini.',
  'Sumber: Trade_Total_Quarter.csv; baris TOTAL Trade Map. USD ribu dikonversi menjadi USD miliar.')
 table_slide(d,'Sampel agregat mencakup 61 kuartal dengan variasi neraca yang besar',
  'Statistik sampel estimasi agregat Indonesia: 2011Q1–2026Q1, setelah holdback maksimum empat lag.',
  ['Variabel','Kuartal','Rata-rata','Simpangan baku','Minimum','Maksimum'],f['descriptive_rows'],
  'Statistik dihitung pada tanggal yang benar-benar masuk desain NARDL agregat Indonesia, bukan pada seluruh raw data. Angka ekspor dan impor adalah nilai per kuartal. Neraca dapat negatif meskipun rata-ratanya positif, menunjukkan bahwa rata-rata jangka panjang tidak mewakili seluruh pengalaman sampel. Indeks GDP riil dibentuk pada basis rata-rata 2015 dan bukan pertumbuhan GDP. Indeks aktivitas luar negeri adalah agregat tetap sepuluh mitra. Tanggal awal data tersedia dan tanggal awal estimasi berbeda karena penyiapan lag.',
  'Sumber: WORLD_NARDL_AIC4_design.dta; Trade_Total_Quarter.csv; descriptive_world_estimation_sample.csv.',
  widths=[3.7,1.0,1.6,1.8,1.6,1.6],size=12.2)
 graph_slide(d,'Sepuluh mitra mencakup sebagian besar perdagangan, tetapi polanya berbeda',
  'Nilai perdagangan dan pangsa ekspor terhadap dunia pada 2025.',
  a['partner_trade'],f"Sepuluh mitra sampel mencakup {dec(f['partner_export_share'],1)}% total ekspor dan {dec(f['partner_import_share'],1)}% total impor Indonesia. Tiongkok menjadi pasar besar sekaligus sumber impor utama; keseimbangan bilateral berbeda dari neraca total.",
  'Penyebut pangsa pada panel kanan adalah seluruh ekspor Indonesia ke dunia, bukan ekspor yang hanya ditujukan ke sepuluh mitra. Karena itu, pangsa kesepuluh negara tidak dijumlahkan menjadi seratus persen. Negara-negara ini merupakan mitra yang dipilih dalam penelitian; grafik tidak mengklaim bahwa daftar tersebut persis peringkat sepuluh negara terbesar pada setiap tahun. Perbedaan surplus dan defisit bilateral tidak secara langsung menentukan signifikansi koefisien kurs. Model tetap mengendalikan aktivitas riil Indonesia dan masing-masing mitra.',
  'Sumber: Trade_Total_Quarter.csv; nilai 2025 lengkap. Pangsa memakai TOTAL perdagangan Indonesia.')
 cc=pd.DataFrame(f['classification_2025'])
 com=float(cc[cc.Flow.eq('Export')&cc.Classification.eq('Commodity_Class')&cc.Class.eq('commodity')].Value_Share_pct.iloc[0])
 non=float(cc[cc.Flow.eq('Export')&cc.Classification.eq('Commodity_Class')&cc.Class.eq('noncommodity')].Value_Share_pct.iloc[0])
 graph_slide(d,'Komoditas penting bagi ekspor, tetapi manufaktur juga berperan besar',
  'Klasifikasi UNCTAD A11 melalui SITC; pangsa nilai rincian HS-6 dunia pada 2025.',
  a['composition_commodity'],f"Komoditas mencakup {dec(com,1)}% total ekspor dan manufaktur nonkomoditas {dec(non,1)}%. Struktur ini memberi alasan membedakan barang, tetapi belum membuktikan perbedaan sensitivitas terhadap kurs.",
  'Definisi komoditas menggunakan kelompok A11 UNCTAD: pangan dan bahan mentah pertanian, bahan bakar, bijih dan mineral, serta logam dan komoditas mineral tertentu. Manufaktur nonkomoditas adalah kategori pelengkap yang dapat dipetakan secara konsisten. Penyebut grafik adalah jumlah rincian HS-6, sehingga mixed dan unclassified tetap terlihat. Pangsa yang ditampilkan khusus 2025; angka seluruh periode tidak diberi label sebagai pangsa tahun tersebut. Harga komoditas internasional dapat menjadi salah satu alasan respons kurs berbeda, tetapi komposisi saja tidak mengidentifikasi saluran itu.',
  'Sumber: Classification_Coverage_By_Year.csv; UNSD HS–SITC; UNCTAD A11. Mixed tetap terpisah.')
 graph_slide(d,'BEC menjelaskan penggunaan barang, bukan kandungan impor dalam ekspor',
  'Dimensi penggunaan akhir BEC Rev.5 berbeda dari dimensi komoditas.',
  a['composition_BEC'],'Barang konsumsi, modal, dan bahan baku/penolong dapat berasal dari kelompok komoditas maupun manufaktur. Klasifikasi penggunaan barang tidak mengukur ketergantungan eksportir pada input impor.',
  'BEC Rev.5 memisahkan penggunaan SNA dari kategori ekonomi. Karena itu, intermediate goods bukan sinonim nonkomoditas dan barang konsumsi bukan sinonim manufaktur. Bahan pangan dapat menjadi konsumsi akhir, sedangkan komoditas pertanian lain merupakan input produksi. Pengujian kandungan impor ekspor memerlukan informasi hubungan input-output atau transaksi perusahaan yang tidak menjadi bagian run ini. Kode dengan beberapa kemungkinan penggunaan tetap ambigu; pemetaan tersebut tidak dipaksa mengikuti hipotesis.',
  'Sumber: UNSD BEC Rev.5 dan korespondensi 2022; Classification_Coverage_By_Year.csv.')
 graph_slide(d,'Tujuh kelompok memakai dua dimensi klasifikasi yang bertumpang tindih',
  'Nilai total ekspor dan impor Indonesia pada 2025; kategori antarsumbu saling bertumpang tindih.',
  a['goods_trade'],'Pertanian/pangan dan energi/tambang merinci komoditas total. Konsumsi, modal, serta bahan baku/penolong memakai sumbu penggunaan. Menjumlahkan ketujuh kelompok akan menghitung sebagian nilai lebih dari sekali.',
  'Panel kelompok dibentuk dari kode HS-6, bukan dari pemaksaan klasifikasi di tingkat HS-4. Meski lebih rinci, kode yang berubah makna antar revisi tetap menimbulkan persoalan. Pengelompokan menggunakan konsensus konservatif dari korespondensi resmi, sebab workbook tidak menyebut revisi HS untuk tiap observasi. Cakupan yang tidak dapat ditentukan dikeluarkan dari kelompok terkait tetapi tetap berada dalam TOTAL. Tumpang tindih kelompok juga berarti bahwa hasil tujuh regresi tidak dapat dianggap tujuh eksperimen independen.',
  'Sumber: Trade_Goods_Quarter.csv; HS6_Classification.csv. Kelompok tidak boleh dijumlahkan.')
 s=d.slide('Variabel model mempertahankan definisi paper dan orientasi kurs',
  'Outcome, aktivitas riil, kurs, dan kontrol harga dijelaskan sebelum membaca koefisien.',
  'Sumber: Bahmani-Oskooee & Fariditavana; konstruksi dataset Tio; kontrol BCOM hanya sensitivitas.',
  'Outcome mempertahankan log impor atas ekspor. GDP bukan pertumbuhan tahunan, melainkan log indeks level riil. Kurs disusun sehingga kenaikannya berarti apresiasi di seluruh model. Untuk dunia dipakai REER BIS, sedangkan untuk bilateral digunakan negatif log RER pada dataset. Partial sums dibentuk berurutan pada sampel tiap kasus; celah waktu tidak dirapatkan. BCOM tidak masuk baseline.')
 specs=[('var_y','Neraca relatif','Log impor dibagi ekspor; kenaikan berarti memburuk.'),
 ('var_d','Aktivitas domestik','Log indeks level PDB riil Indonesia.'),
 ('var_f','Aktivitas luar negeri','Log GDP mitra; agregat Indonesia memakai proksi sepuluh mitra.'),
 ('var_q','Kurs riil','Kenaikan selalu berarti apresiasi.'),
 ('var_pos','Akumulasi apresiasi','Jumlah perubahan positif log kurs.'),
 ('var_neg','Akumulasi depresiasi','Jumlah perubahan negatif log kurs.'),
 ('var_c','Harga global','Log indeks BCOM; hanya pada sensitivitas.')]
 for i,(key,label,desc) in enumerate(specs):
  y=1.76+i*.68
  if i%2==0:st.box(s,.67,y,12,.63,'beige')
  mathbox(s,key,.82,y+.12,.9,.36)
  st.text(s,1.95,y+.14,2.8,.36,label,14,'dark',True)
  st.text(s,4.72,y+.13,7.7,.42,desc,13)
 graph_slide(d,'Kurs dan neraca bergerak bersama banyak perubahan ekonomi',
  'Rasio impor/ekspor dan REER pada tanggal sampel estimasi agregat Indonesia.',
  a['world_macro'],'Pergerakan dua seri ini memberi konteks waktu. Hubungan visual belum memisahkan pengaruh permintaan, harga global, komposisi perdagangan, dan kemungkinan respons kurs terhadap neraca.',
  'Rasio impor terhadap ekspor berada di atas satu saat impor melebihi ekspor. REER pada panel bawah disusun pada orientasi apresiasi. Perbandingan dua deret dapat menunjukkan episode yang menarik untuk didiskusikan, tetapi juga rentan terhadap tren, kejutan bersama dan perbedaan waktu penyesuaian. Estimasi dinamis memasukkan aktivitas ekonomi, namun tidak dengan sendirinya menyelesaikan endogenitas kurs. Karena itu, bahasa hasil dipertahankan sebagai hubungan kondisional, bukan efek kausal yang sudah teridentifikasi.',
  'Sumber: WORLD_NARDL_AIC4_design.dta; Trade_Total_Quarter.csv. Grafik bersifat deskriptif.')
 graph_slide(d,'Perbedaan rentang sampel membatasi perbandingan antarmitra',
  'Rentang estimasi utama setelah lag; deret terpanjang yang lengkap dipertahankan.',
  a['coverage'],'India mulai lebih akhir karena ketersediaan CPI. Sampel AS dan Vietnam berhenti sebelum beberapa mitra lain akibat celah seri. Perbedaan koefisien dapat mencerminkan struktur pasar sekaligus pengalaman waktu yang berbeda.',
  'India menggunakan CPI murni mulai 2013 pada data tersedia; setelah holdback lag, sampel estimasi menjadi 49 kuartal. WPI hanya dipakai sebagai sensitivitas terpisah. CPI AS Oktober 2025 dan kurs Vietnam Agustus 2025 kosong pada keluarga seri utama. Program memilih jendela lengkap terpanjang dan tidak menyambung sisa kuartal seolah tidak ada celah. Tindakan ini mempertahankan arti lag, tetapi mengurangi keseragaman rentang waktu. Pembandingan antarmitra belum merupakan uji formal pada sampel yang sama.',
  'Sumber: case_registry.csv; results_primary_models.csv; audit_validitas_data_macro.md.')
 body_slide(d,'Pengaruh harga relatif bergantung pada cara barang diperdagangkan',
  'Alasan ekonomi untuk membedakan komoditas dan manufaktur.',
  'Harga internasional dan respons volume',
  'Ketika harga barang mengikuti pasar global, perubahan kurs domestik tidak harus segera mengubah harga yang dibayar pembeli asing. Respons nilai ekspor juga bergantung pada volume yang dapat dipasok dan kontrak yang belum disesuaikan.',
  'Komposisi pasar dan waktu respons',
  'Barang manufaktur tidak selalu bereaksi lebih besar. Diferensiasi produk, hubungan pemasok dan kondisi permintaan mitra dapat menunda penyesuaian. Arah respons perlu dibaca sebagai pertanyaan empiris pada tiap pasar.',
  'Uraian ini merupakan penafsiran ekonomi yang memotivasi pengelompokan, bukan mekanisme yang telah diidentifikasi dari regresi. Nilai perdagangan menggabungkan komponen harga dan volume. Keduanya tidak dapat dipisahkan karena file HS-6 tidak berisi kuantitas yang digunakan dalam run. Pembagian komoditas dan manufaktur membantu menguji heterogenitas rasio neraca, tetapi belum mengestimasi pass-through kurs ke harga ekspor atau elastisitas permintaan ekspor secara terpisah. Pengujian kanal input impor sengaja tidak dimasukkan.')
 graph_slide(d,'J-curve memerlukan fase awal memburuk dan fase berikutnya membaik',
  'Ilustrasi teoretis: bentuk kurva ini bukan hasil estimasi Indonesia.',
  a['theory_J'],'Penyesuaian kontrak dan volume dapat berlangsung pada waktu berbeda. Namun tidak semua respons yang akhirnya positif membentuk J-curve; fase awal yang memburuk juga harus terlihat.',
  'Paper mendefinisikan J-curve melalui pemburukan jangka pendek yang diikuti perbaikan jangka panjang. Grafik ilustratif hanya membantu menjelaskan urutan tersebut. Dalam data penelitian, ketidakpastian pada kedua fase tetap perlu diperiksa. Karena interval yang dipakai pointwise, pemilihan horizon tertentu sesudah melihat grafik tidak menjadi uji simultan yang sah. Analisis titik kurva selanjutnya diberi nama pemeriksaan visual-operasional agar tidak tertukar dengan pengujian formal paper.',
  'Sumber konsep: Bahmani-Oskooee & Fariditavana (2015/2016). Kurva ilustratif, bukan data.')
 table_slide(d,'Penelitian ini mengadaptasi paper, bukan menyalin seluruh spesifikasinya',
  'Definisi dan logika model dipertahankan; unit analisis serta panjang sampel berubah.',
  ['Komponen','Paper acuan','Implementasi Indonesia'],[
 ['Unit analisis','AS dengan enam mitra','Indonesia–seluruh Indonesia–seluruh dunia, sepuluh mitra, tujuh kelompok HS-6'],
 ['Outcome','Log rasio impor/ekspor','Definisi rasio yang sama'],
 ['Data','Kuartalan 1971Q1–2013Q3','Perdagangan mulai 2006; jendela makro bervariasi'],
 ['Panjang lag','Maksimum delapan lag first difference','AIC maksimum empat lag level; cap dua sensitivitas'],
 ['Permintaan luar negeri','Pendapatan setiap mitra','GDP mitra; agregat Indonesia memakai proksi tetap sepuluh mitra'],
 ['Inferensi','Bounds dan diagnostik dalam paper','Bounds finite-sample Stata; penyaringan tambahan'],
 ['Nonlinearitas','Partial sums apresiasi/depresiasi','Dekomposisi arah kurs yang sama']],
  'Paper menggunakan enam pasangan bilateral AS, yaitu Kanada, Prancis, Jerman, Italia, Jepang dan Inggris, pada sampel yang jauh lebih panjang. Pembatasan empat lag level dalam penelitian ini adalah penyesuaian terhadap sampel Indonesia yang lebih pendek dan tidak boleh disamakan dengan delapan lag first difference paper. Implementasi bounds memakai paket ardl 1.0.6 dan nilai kritis finite-sample yang tersedia. CUSUMSQ dalam proyek adalah aproksimasi Monte Carlo, bukan salinan tabel kritis paper.',
  'Sumber: paper pengguna, bagian metode dan hasil; master do-file Tio.',widths=[2.2,4.4,5.4],size=11.8)
 s=d.slide('ARDL memberi satu hubungan kurs untuk apresiasi dan depresiasi',
  'Model linier menjadi pembanding sebelum efek kedua arah dipisahkan.',
  'Sumber: Bahmani-Oskooee & Fariditavana; implementasi Stata Tio.',
  'Persamaan ini adalah bentuk jangka panjang untuk menjelaskan koefisien. Estimasi aktual tetap memakai dinamika ARDL dan representasi error correction. GDP domestik diharapkan berkaitan dengan permintaan impor, sedangkan aktivitas mitra berkaitan dengan permintaan ekspor, tetapi tanda empiris dapat berbeda karena nilai perdagangan memuat banyak komponen. Kurs yang naik adalah apresiasi. Pada outcome impor atas ekspor, koefisien kurs positif mengarah pada perbaikan ketika depresiasi, sedangkan koefisien negatif mengarah pada pemburukan.')
 mathbox(s,'lr_ardl',.9,1.9,11.45,1.05)
 st.text(s,.9,3.25,5.5,2.6,'Satu koefisien kurs merangkum hubungan jangka panjang untuk kedua arah perubahan. Respons apresiasi dan depresiasi dibatasi mempunyai bentuk yang simetris dalam log.',18)
 st.text(s,6.8,3.25,5.45,2.6,'Pembatasan ini berguna sebagai pembanding. Bila penyesuaian kontrak atau perilaku pasar berbeda menurut arah kurs, model linier dapat merangkum hubungan yang terlalu sederhana.',18)
 s=d.slide('NARDL memisahkan akumulasi apresiasi dan depresiasi',
  'Nonlinearitas berasal dari partial sums; bukan dari memasukkan volatilitas kurs.',
  'Sumber: persamaan dekomposisi dan NARDL paper; analysis_quarterly.dta.',
  'Partial sums mempertahankan seluruh urutan perubahan kurs dalam jendela kasus. Variabel depresiasi adalah akumulasi perubahan negatif sehingga nilainya tidak diberi tanda positif secara paksa. Koefisien apresiasi dan depresiasi kemudian dapat berbeda. Dalam penelitian ini tidak ada regressor volatilitas, sehingga perbedaan dua koefisien tidak boleh disebut bukti pengaruh volatilitas. Model nonlinear di sini juga tidak mengidentifikasi perubahan rezim struktural yang tidak dimodelkan.')
 mathbox(s,'partial',.88,1.8,11.55,1.10)
 mathbox(s,'lr_nardl',.88,3.15,11.55,.95)
 st.text(s,.9,4.6,5.4,1.65,'Depresiasi tetap berupa perubahan negatif. Karena itu, arah pengaruh harus diperoleh dari koefisien dan tanda guncangannya secara bersama.',16)
 st.text(s,6.8,4.6,5.4,1.65,'Pemisahan kedua arah memungkinkan asimetri, tetapi tidak mengharuskan asimetri ditemukan. Pembatasan kesamaan tetap diperiksa dengan uji Wald.',16)
 s=d.slide('Error correction menghubungkan penyesuaian awal dan hubungan level',
  'Representasi umum NARDL; koefisien tertentu dapat nol atau terikat sesuai lag terpilih.',
  'Sumber: ardl_helpers.do; Bahmani-Oskooee & Fariditavana; output koefisien Stata.',
  'Persamaan menunjukkan komponen level tertunda dan first difference. Panjang lag aktual dipilih dengan AIC dan tercantum untuk setiap model dalam atlas. Bentuk umum ini tidak berarti seluruh suku diestimasi bebas pada setiap spesifikasi; ketika lag suatu regressor nol, reparameterisasi error correction dapat mengandung pembatasan yang sesuai dengan persamaan level. Ekuivalensi fitted value dan residual antara model level dan ECM sudah diperiksa. Koefisien jangka panjang diperoleh melalui normalisasi, sehingga interpretasinya bergantung pada keberadaan hubungan level yang valid.')
 mathbox(s,'uecm',.8,1.7,11.7,2.45)
 mathbox(s,'lr_normalize',1.2,4.6,5.1,.72)
 st.text(s,6.85,4.6,5.3,1.85,'Normalisasi menghasilkan koefisien jangka panjang. Koefisien penyesuaian yang negatif saja belum cukup; hubungan level dan spesifikasi residual tetap harus diperiksa.',15.5)
 s=d.slide('Asimetri dan kointegrasi menjawab pertanyaan yang berbeda',
  'Uji perbedaan dua arah kurs tidak menggantikan pemeriksaan hubungan level.',
  'Sumber: estat ectest; uji Wald; diagnostic_summary.csv.',
  'Wald jangka panjang menguji kesamaan koefisien kedua partial sums. Uji jangka pendek membandingkan jumlah koefisien perubahan dalam parameterisasi yang digunakan. Bounds menilai keberadaan hubungan level dengan distribusi kritis yang tidak sama dengan uji F biasa. Penelitian memakai F dan t bersama, kemudian memeriksa joint-X untuk menghindari pembacaan hubungan level yang terdegenerasi. Risiko integrasi orde dua juga ditandai; gagal menolak unit root bukan bukti pasti integrasi orde dua.')
 st.text(s,.85,1.8,5.6,.4,'Kesamaan respons dua arah',17,'brown',True)
 mathbox(s,'asymmetry',.85,2.45,11.5,.85)
 st.text(s,.85,3.75,5.6,.4,'Keberadaan hubungan level',17,'brown',True)
 mathbox(s,'bounds',.85,4.35,7.3,.73)
 st.text(s,.87,5.65,11.4,.8,'Inferensi juga mempertimbangkan joint-X, akar dinamis, integrasi variabel dan derajat bebas residual. Penolakan satu uji tidak otomatis mengesahkan seluruh model.',15.5)
 s=d.slide('Tanda grafik diubah agar perbaikan neraca berada di atas nol',
  'Model tetap memakai impor/ekspor; hanya tampilan respons yang dibalik tandanya.',
  'Sumber: transformasi tepat dynamic_multipliers.csv; tidak ada estimasi ulang.',
  'Semua panel respons dalam deck menggunakan negatif respons model sehingga nilai positif menunjukkan perbaikan log ekspor atas impor. Interval ikut dibalik dengan menukar batas bawah dan atas setelah dikali negatif. Transformasi ini tepat secara aljabar dan tidak mengubah ketidakpastian. Besaran guncangan sama dalam log: kenaikan sepuluh persen pada indeks apresiasi berpasangan dengan penurunan sekitar sembilan koma nol sembilan persen, bukan penurunan tepat sepuluh persen. Poin log kali seratus bukan perubahan persentase surplus dolar.')
 mathbox(s,'outcome',.85,1.75,11.5,.78)
 mathbox(s,'display',.85,3.02,11.5,.83)
 mathbox(s,'shock',.85,4.34,11.5,.78)
 st.box(s,.68,5.76,11.96,.91,'beige')
 st.text(s,.88,5.92,11.5,.61,'Positif: rasio ekspor terhadap impor membaik. Negatif: memburuk. Satuan grafik adalah poin log kali seratus, bukan persentase perubahan surplus dalam dolar.',15,'dark',True)
 s=d.slide('Hanya sebagian model lolos seluruh penyaringan yang digunakan',
  'Model utama tetap dilaporkan seluruhnya; penyaringan tidak dipakai untuk menyembunyikan hasil.',
  'Sumber: analysis_validation_report.json; results_primary_models.csv.',
  'Dari 176 model utama, 95 menolak hipotesis tidak ada hubungan level menggunakan F dan t pada taraf lima persen. Syarat tambahan joint-X, kestabilan akar, risiko integrasi orde dua dan minimal lima belas derajat bebas menyisakan 62. Sebanyak 28 juga tidak ditolak oleh himpunan diagnostik yang digunakan. Jumlah ini bukan ukuran probabilitas model benar dan bukan validasi kausal. Penolakan diagnostik bersifat sinyal untuk meninjau spesifikasi, bukan alasan mekanis menghapus observasi atau memilih model yang mendukung hipotesis.')
 st.cards(s,[('176','Model utama','Agregat dan kelompok Indonesia'),
 ('95','F dan t bounds','Menolak tidak ada hubungan level'),
 ('62','Syarat level tambahan','Termasuk joint-X dan integrasi'),
 ('28','Level serta diagnostik','Tidak ditolak pada uji yang dipakai')],y=1.9,h=1.5)
 st.text(s,.88,4.0,5.3,2.1,'Signifikansi koefisien tidak cukup bila hubungan level belum didukung. Sebaliknya, model yang lolos diagnostik tetap belum mengidentifikasi sebab-akibat.',18)
 st.text(s,6.85,4.0,5.3,2.1,'Tabel, kurva dan atlas mempertahankan seluruh spesifikasi. Warna dan keterangan menunjukkan kekuatan bukti agar pembaca dapat membedakan hasil yang lebih atau kurang dapat ditafsirkan.',18)
 body_pair(d,'WORLD','Agregat Indonesia belum memberi hubungan jangka panjang yang kuat',
  'ARDL belum menolak tidak adanya hubungan level; NARDL masih inconclusive pada F/t bounds. Kurva menunjukkan kemungkinan penyesuaian, tetapi belum menjadi temuan jangka panjang yang mapan.')
 z=pair_for('WORLD');rows=[]
 for _,r in z.iterrows():
  rows.append([r.estimator,dec(r.lr_q_b if r.estimator=='ARDL' else r.lr_pos_b,3),
   '—' if r.estimator=='ARDL' else dec(r.lr_neg_b,3),prob(r.Dep_LR_p),prob(r.lr_asym_p),r.Bounds5])
 table_slide(d,'Signifikansi depresiasi pada NARDL agregat Indonesia belum menyelesaikan masalah level',
  'Koefisien nominal dan kelayakan hubungan jangka panjang perlu dibaca bersama.',
  ['Model','Kurs / apresiasi','Depresiasi','Prob. koefisien','Prob. asimetri','F/t bounds'],rows,
  'Pada NARDL agregat Indonesia, koefisien depresiasi positif dan probabilitas nominal berada di bawah lima persen. Wald juga menolak kesamaan dua koefisien. Namun p-value upper bound F sekitar 0,094 dan t sekitar 0,279, sehingga syarat F dan t pada lima persen tidak terpenuhi. CUSUMSQ juga memberi catatan stabilitas. Karena itu, membaca hanya bintang pada koefisien akan menghasilkan kesimpulan yang lebih kuat daripada yang didukung spesifikasi. ARDL agregat Indonesia tidak memiliki koefisien kurs yang signifikan dan tidak mendukung hubungan level.',
  'Sumber: WORLD_ARDL_AIC4; WORLD_NARDL_AIC4; koefisien dan bounds Stata.',
  widths=[1.2,2.1,1.6,2,1.9,3.2],size=12)
 body_pair(d,'WORLD_FULL','Perpanjangan sampel menjadi pemeriksaan ketahanan hasil agregat',
  'Sampel 2006+ dilaporkan sebagai sensitivitas terhadap window. Agregat Indonesia utama tetap memakai awal 2010 untuk pembandingan dengan run sebelumnya; data perdagangan baru seluruhnya berasal dari workbook HS-6.')

 graph_slide(d,'Respons bilateral tidak dapat dirangkum menjadi satu elastisitas nasional',
  'Koefisien jangka panjang dan interval nominal 95%; warna menunjukkan dukungan model.',
  a['forest_bilateral'],'Australia dan Malaysia memberi dukungan lebih baik pada NARDL utama. Hasil beberapa mitra lain tampak berlawanan arah, tetapi tidak selalu lolos syarat hubungan level atau diagnostik.',
  'Garis horizontal memperlihatkan ketepatan estimasi, bukan hanya tanda koefisien. Koefisien yang relevan untuk depresiasi adalah koefisien kurs pada ARDL dan koefisien partial sum negatif pada NARDL. Warna cokelat berarti syarat level dan diagnostik yang digunakan terpenuhi; emas berarti ada dukungan level tetapi catatan diagnostik; simbol kosong berarti syarat level belum lengkap. Perbedaan dua estimasi yang intervalnya berbeda belum merupakan uji langsung perbedaan antar negara. Jendela sampel juga tidak seragam.')
 body_pair(d,'BIL_AUS','Australia memperlihatkan pemburukan awal sebelum perbaikan',
  'NARDL Australia memenuhi penyaringan level dan diagnostik serta memperlihatkan pola J pada estimasi titik. Interval fase awal masih lebar, sehingga bentuk tersebut belum menjadi kepastian statistik pada kedua fase.')
 body_pair(d,'BIL_MYS','Malaysia mengarah pada perbaikan, tetapi dukungan signifikansinya terbatas',
  'NARDL Malaysia lolos penyaringan level dan diagnostik. Koefisien depresiasi signifikan secara nominal, tetapi tidak bertahan pada ambang 5% setelah koreksi BH dalam keluarga model bilateral.')
 ids=['BIL_CHN','BIL_JPN']
 path=plot_selected_nardl(ids,'responses_CHN_JPN',ncol=2)
 graph_slide(d,'Tanda negatif di Tiongkok dan Jepang belum cukup menjadi kesimpulan',
  'NARDL bilateral; panel lengkap ARDL–NARDL tersedia dalam atlas.',
  path,'Pada Jepang, koefisien depresiasi tampak signifikan secara nominal. Namun kedua pasangan ini belum memenuhi keseluruhan syarat level dan diagnostik; tanda negatif tidak otomatis menjadi bukti depresiasi merugikan.',
  '\n\n'.join(note_row(r) for _,r in PRIMARY[PRIMARY.series_id.isin(ids)&PRIMARY.estimator.eq('NARDL')].iterrows()))
 rest=['BIL_'+x for x in ['IND','KOR','SGP','THA','USA','VNM']]
 graph_slide(d,'Enam mitra lainnya memperlihatkan variasi bentuk dan ketepatan respons',
  'NARDL utama; skala vertikal setiap panel berbeda agar interval seluruhnya tetap terlihat.',
  plot_selected_nardl(rest,'responses_other_six',ncol=3),
  'Respons yang akhirnya positif tidak selalu membentuk J-curve. Respons yang tampak mendatar juga tidak membuktikan efek nol bila intervalnya lebar atau hubungan level belum didukung.',
  '\n\n'.join(note_row(r) for _,r in PRIMARY[PRIMARY.series_id.isin(rest)&PRIMARY.estimator.eq('NARDL')].iterrows()))
 rows=[]
 for iso in ISOS:
  r=PRIMARY[PRIMARY.series_id.eq('BIL_'+iso)&PRIMARY.estimator.eq('NARDL')].iloc[0]
  rows.append([COUNTRIES[iso],int(r.N),dec(r.lr_neg_b,3),prob(r.lr_neg_p),prob(r.Dep_LR_p_BH),
    prob(r.lr_asym_p),'Ya' if r.Levels_supported5 else 'Belum','Memadai' if r.Diagnostic_clean5 else 'Catatan'])
 table_slide(d,'Asimetri, signifikansi, dan kelayakan model tidak selalu sejalan',
  'Ringkasan NARDL sepuluh mitra; BH eksploratif dalam keluarga bilateral–NARDL.',
  ['Mitra','Kuartal','Depresiasi','Prob. nominal','Prob. BH','Prob. asimetri','Level','Diagnostik'],rows,
  'Australia dan Malaysia lolos penyaringan gabungan, tetapi hanya Australia mempertahankan signifikansi koefisien depresiasi di bawah lima persen setelah BH pada keluarga bilateral. India memiliki penolakan Wald asimetri tanpa dukungan level yang memadai. Jepang dan AS mempunyai probabilitas koefisien depresiasi nominal yang kecil, tetapi spesifikasinya belum memenuhi keseluruhan syarat. Contoh ini menunjukkan mengapa tabel satu kolom koefisien dan bintang tidak cukup untuk penelitian ini.',
  widths=[2.2,.8,1.3,1.4,1.1,1.4,1.2,1.7],size=10.8)
 graph_slide(d,'Pemisahan barang mengubah kesimpulan agregat Indonesia',
  'Tujuh kelompok HS-6 dunia; ARDL dan NARDL dibaca berdampingan.',
  a['forest_WLD'],'ARDL menunjukkan hubungan negatif pada komoditas total serta energi/tambang. Pada NARDL, dukungan dan ketepatan estimasi berubah. Besarnya interval bahan baku/penolong juga menandai hasil yang kurang presisi.',
  'ARDL komoditas total dan energi/tambang memenuhi syarat level serta diagnostik dalam baseline. Koefisien kurs keduanya negatif: dengan depresiasi sebagai penurunan kurs berorientasi apresiasi, tanda ini mengarah pada kenaikan impor relatif terhadap ekspor. NARDL tidak menghasilkan bukti yang sama kuat untuk efek depresiasi kelompok tersebut. Tanda positif barang konsumsi dalam NARDL disertai catatan diagnostik. Seluruh garis tetap ditampilkan, termasuk yang syarat levelnya belum lengkap. Perbandingan kelompok belum menjadi uji formal selisih elastisitas.')
 body_slide(d,'Hubungan negatif komoditas bertahan pada beberapa pembanding linier',
  'Namun model nonlinear belum mengonfirmasi kesimpulan yang sama kuatnya.',
  'Apa yang bertahan',
  'Pada ARDL agregat Indonesia, komoditas total dan energi/tambang mempunyai koefisien kurs negatif. Arah itu tetap muncul ketika maksimum lag dipersempit dan ketika harga BCOM ditambahkan sebagai kontrol.',
  'Apa yang masih membatasi',
  'Sejumlah sensitivitas gagal pada diagnostik tertentu. Pada NARDL, koefisien depresiasi kelompok tersebut belum signifikan dan dukungan model berubah menurut panjang lag. Hasilnya masih bergantung pada spesifikasi.',
  'Koefisien negatif model linier tidak perlu dikesampingkan hanya karena berbeda dari intuisi daya saing. Sebaliknya, hasil tersebut juga tidak boleh dipilih sebagai kesimpulan tunggal karena sesuai hipotesis. NARDL memungkinkan perbedaan arah kurs dan menghasilkan interval depresiasi yang lebih lebar. Perbedaan ini dapat berkaitan dengan tambahan parameter, variasi kurs yang terbatas dan heterogenitas komponen perdagangan. BCOM merupakan indeks harga luas, bukan harga masing-masing produk dan bukan instrumen eksogen. Karena itu, memasukkannya tidak dengan sendirinya membuktikan kanal harga global.',
  'Sumber: TYPE_WLD_commodity dan energy_mining; cap dua; sensitivitas PRICE_WLD.')
 body_pair(d,'TYPE_WLD_commodity','Komoditas total: pembacaan linier dan nonlinear belum sepenuhnya sejalan',
  'ARDL mengarah pada pemburukan neraca setelah depresiasi. NARDL memberi estimasi depresiasi yang kurang presisi dan belum memenuhi seluruh syarat level dalam baseline empat lag.')
 body_pair(d,'TYPE_WLD_energy_mining','Energi dan tambang: koefisien linier kuat, ketidakpastian nonlinear besar',
  'Arah negatif ARDL muncul pada beberapa pembanding. NARDL tidak memberi koefisien depresiasi yang signifikan; spesifikasi utama juga memiliki catatan heteroskedastisitas.')
 body_pair(d,'TYPE_WLD_manufacturing','Manufaktur nonkomoditas belum menunjukkan perbaikan yang dapat dipastikan',
  'Tanda titik NARDL mengarah pada perbaikan, tetapi interval dan dukungan hubungan level belum cukup. Data ini belum membenarkan kesimpulan bahwa manufaktur lebih sensitif daripada komoditas.')
 body_pair(d,'TYPE_WLD_consumption','Barang konsumsi memberi arah perbaikan, dengan catatan pada model nonlinear',
  'ARDL kelompok konsumsi lolos penyaringan utama. NARDL menunjukkan koefisien depresiasi positif, tetapi residual dan stabilitas memberi beberapa catatan yang membatasi pembacaan jangka panjang.')
 other=['TYPE_WLD_'+x for x in ['agriculture','intermediate','capital']]
 graph_slide(d,'Pertanian, bahan baku/penolong, dan modal belum memberi satu pola dunia',
  'NARDL utama; dua dimensi klasifikasi berbeda tetap dipisahkan.',
  plot_selected_nardl(other,'responses_other_world_goods',ncol=3),
  'Interval bahan baku/penolong jauh lebih lebar daripada kelompok lain. Kategori modal dan pertanian juga belum memenuhi seluruh syarat level pada NARDL utama; arah titik tidak menjadi kesimpulan final.',
  '\n\n'.join(note_row(r) for _,r in PRIMARY[PRIMARY.series_id.isin(other)&PRIMARY.estimator.eq('NARDL')].iterrows()))
 # Matrix color describes model qualification, while numeric cells retain the coefficient.
 fig,ax=plt.subplots(figsize=(11.6,4.4))
 z=PRIMARY[PRIMARY.scope.eq('goods')&PRIMARY.estimator.eq('NARDL')]
 values=np.zeros((7,11));labels=np.empty((7,11),dtype=object)
 for i,g in enumerate(GROUPS):
  for j,iso in enumerate(COUNTRIES):
   r=z[z.Group.eq(g)&z.ISO3.eq(iso)].iloc[0]
   values[i,j]=2 if r.Levels_supported5 and r.Diagnostic_clean5 else 1 if r.Levels_supported5 else 0
   labels[i,j]=dec(r.lr_neg_b,2)
 from matplotlib.colors import ListedColormap
 ax.imshow(values,cmap=ListedColormap(['#F0F0F0','#F0D7B4','#A5644E']),vmin=0,vmax=2,aspect='auto')
 for i in range(7):
  for j in range(11):ax.text(j,i,labels[i,j],ha='center',va='center',fontsize=9,color='white' if values[i,j]==2 else color('ink'))
 ax.set_xticks(range(11),list(COUNTRIES));ax.set_yticks(range(7),list(GROUPS.values()),fontsize=10)
 ax.tick_params(length=0);fig.tight_layout()
 matrix=figure(fig,'goods_partner_qualification_matrix')
 graph_slide(d,'Efek depresiasi berbeda menurut barang dan tujuan perdagangan',
  'Isi sel: koefisien depresiasi NARDL. Cokelat: level dan diagnostik; beige: level dengan catatan; abu-abu: level belum didukung.',
  matrix,'Matriks ini memetakan heterogenitas, bukan peringkat negara. Sel berwarna cokelat tetap dapat mempunyai koefisien yang tidak signifikan; kelayakan model dan ketepatan efek adalah dua hal berbeda.',
  'Matriks mencakup tujuh kelompok dan sebelas pasar termasuk dunia. Warna ditentukan oleh status hubungan level dan diagnostik, bukan oleh arah koefisien. Dengan begitu, pembaca dapat melihat bahwa beberapa koefisien besar berasal dari model yang belum memenuhi syarat level. Kelompok bertumpang tindih dan sampel waktu berbeda. Matriks ini tidak boleh ditafsirkan sebagai 77 eksperimen independen atau uji formal heterogenitas. Grafik interval per pasar tersedia dalam lampiran B.')
 body_pair(d,'TYPE_CHN_agriculture','Pertanian ke Tiongkok memberi contoh arah pemburukan yang lebih terukur',
  'NARDL kelompok ini lolos syarat level serta diagnostik. Koefisien depresiasi negatif dan tetap signifikan setelah BH, tetapi hasilnya berlaku untuk rasio neraca kelompok ini, bukan seluruh ekspor Indonesia.')
 examples=['TYPE_KOR_capital','TYPE_USA_consumption']
 graph_slide(d,'Sebagian kelompok justru memberi pola J yang lebih jelas',
  'NARDL barang modal–Korea dan konsumsi–AS; interval tetap pointwise.',
  plot_selected_nardl(examples,'responses_clearer_J_examples',ncol=2),
  'Kedua contoh menunjukkan fase awal di bawah nol dan akhir horizon di atas nol pada band pointwise. Pola ini lebih mendukung urutan J, tetapi belum menjadi uji simultan atau bukti kausal.',
  '\n\n'.join(note_row(r) for _,r in PRIMARY[PRIMARY.series_id.isin(examples)&PRIMARY.estimator.eq('NARDL')].iterrows()))
 c=CURVES[CURVES.model_id.isin(PRIMARY.model_id)];rows=[]
 for est,g in c.groupby('estimator'):
  isj=g.point_pattern.eq('Pola J pada estimasi titik');ok=g.Levels_supported5&g.Diagnostic_clean5
  rows.append([est,len(g),int(isj.sum()),int((isj&ok).sum()),int((isj&ok&g.phase_CI_separated).sum())])
 s=table_slide(d,'Bentuk J lebih sering terlihat daripada dukungan statistik dua fasenya',
  'Pemeriksaan visual-operasional; bukan pengganti pengujian formal paper.',
  ['Model','Seluruh seri','Pola J pada titik','J + level/diagnostik','Dua fase pada band pointwise'],rows,
  'Pola titik didefinisikan sebelum penghitungan deck: setidaknya satu respons negatif dalam horizon nol sampai empat, dan rata-rata respons positif pada horizon enam belas sampai dua puluh empat. Definisi ini bukan koefisien jangka panjang dan bukan uji yang dipraregistrasikan. Syarat interval menuntut ada fase awal dengan batas atas negatif serta batas bawah positif di kuartal ke-24. Pemilihan salah satu horizon awal mengandung pencarian, sehingga dua kasus yang lolos juga tidak menjadi uji simultan. Tumpang tindih kelompok dan pemilihan AIC membatasi pembacaan jumlah kasus.',
  'Sumber: jcurve_classification_all_516.csv; semua 176 model utama.',
  widths=[1.2,1.5,2.4,3.1,3.8],size=11.5)
 mathbox(s,'jcriterion',.95,5.7,11.4,.7)
 rows=[]
 for group in ['commodity','energy_mining']:
  for prefix,cap,label in [('TYPE',4,'Utama'),('TYPE',2,'Cap dua'),('PRICE',4,'Kontrol BCOM')]:
   r=ALL[ALL.series_id.eq(prefix+'_WLD_'+group)&ALL.estimator.eq('ARDL')&ALL.cap.eq(cap)].iloc[0]
   rows.append([GROUPS[group].replace('Komoditas ',''),label,dec(r.lr_q_b,3),prob(r.lr_q_p),
    'Ya' if r.Levels_supported5 else 'Belum','Memadai' if r.Diagnostic_clean5 else 'Catatan'])
 table_slide(d,'Kontrol harga tidak menghapus arah negatif komoditas pada ARDL',
  'Sensitivitas linier dunia; pemeriksaan ini belum mengidentifikasi kanal harga global.',
  ['Kelompok','Spesifikasi','Koefisien kurs','Prob. nominal','Level','Diagnostik'],rows,
  'Koefisien kurs linier komoditas total sekitar negatif satu koma tiga sampai satu koma lima; energi/tambang sekitar negatif dua sampai negatif dua koma tiga. Arah ini bertahan pada cap dua maupun tambahan BCOM. Namun syarat diagnostik tidak konsisten untuk seluruh varian, terutama model dengan kontrol harga. BCOM berpotensi menangkap kejutan global yang juga terkait kurs dan permintaan, bukan satu saluran kausal murni. NARDL dan seluruh sensitivitas tetap tersedia dalam atlas C. Tidak dilakukan pemilihan hanya satu kontrol yang menghasilkan tanda yang diinginkan.',
  widths=[3.0,2.1,1.8,1.8,1.2,2.1],size=12)
 rows=[]
 for mid in ['BIL_AUS_NARDL_AIC4','BIL_MYS_NARDL_AIC4','TYPE_CHN_agriculture_NARDL_AIC4','TYPE_WLD_commodity_ARDL_AIC4','TYPE_WLD_energy_mining_ARDL_AIC4']:
  r=PRIMARY[PRIMARY.model_id.eq(mid)].iloc[0]
  rows.append([human(r),r.estimator,prob(r.Dep_LR_p),prob(r.Dep_LR_p_BH)])
 table_slide(d,'Koreksi pengujian berganda mengubah sebagian pembacaan signifikansi',
  'Contoh pembacaan probabilitas nominal dan BH; bukan daftar seluruh hasil signifikan.',
  ['Seri','Model','Prob. nominal','Prob. BH'],rows,
  'BH dihitung terpisah dalam keluarga scope dan estimator pada model utama. Sebagai contoh, probabilitas nominal Malaysia berada di bawah lima persen, sedangkan nilai BH-nya sedikit di atas ambang tersebut. Pertanian Tiongkok tetap berada di bawah lima persen. Koreksi ini bersifat eksploratif karena model dipilih dengan AIC, kelompok saling bertumpang tindih dan spesifikasi sensitivitas juga diperiksa. BH tidak mengoreksi seluruh proses pencarian model dan tidak menggantikan syarat hubungan level.',
  widths=[6.3,1.4,2.15,2.15],size=12.5)
 graph_slide(d,'Diagnostik menunjukkan bahwa masalahnya tidak hanya ada pada signifikansi',
  'Jumlah penolakan pada taraf 5% di antara 176 spesifikasi utama.',
  a['diagnostics'],'Korelasi serial, bentuk fungsi, varians, distribusi residual dan stabilitas dapat membatasi inferensi. Model yang bermasalah tetap dilaporkan, dengan catatan yang berbeda dari model yang tidak ditolak.',
  'Penolakan diagnostik dihitung dari hasil yang tersedia. Tidak ditolaknya suatu uji berarti bukti sampel belum cukup untuk menolak hipotesis nol, bukan bahwa asumsi pasti benar. Model dengan sedikit kuartal dan banyak parameter mempunyai daya uji terbatas. Penanganan yang benar bukan menghapus observasi ekstrem secara otomatis, melainkan meninjau sumber, spesifikasi, perubahan struktur dan desain inferensi. Run ini mempertahankan spesifikasi yang sudah ditentukan agar hasil lengkap dapat dinilai pembaca.',
  'Sumber: diagnostic_summary.csv; setiap uji mempunyai hipotesis nol tersendiri.')
 graph_slide(d,'Stabilitas agregat Indonesia berbeda dari Australia dan Malaysia',
  'CUSUMSQ residual rekursif NARDL; band referensi Gaussian dengan 19.999 simulasi.',
  a['stability'],'Agregat Indonesia memberi catatan pada stabilitas varians rekursif. Australia dan Malaysia tidak ditolak oleh penyaringan utama, tetapi hasil tersebut tetap bersyarat pada spesifikasi dan kekuatan uji.',
  'CUSUM dan CUSUMSQ mempunyai konstruksi dan pertanyaan yang berbeda. CUSUM utama diekspor langsung dari Stata dan maksimum lintasannya telah dicocokkan dengan statistik yang tersimpan. Perhitungan independen cocok pada matriks awal full rank. Dua model kelompok Australia, yaitu modal dan konsumsi NARDL, mempunyai inisialisasi rank-deficient sehingga diberi catatan khusus; ini bukan model bilateral Australia yang ditampilkan di sini. CUSUMSQ menggunakan referensi Gaussian yang disimulasikan dengan seed tetap dan tidak diklaim sebagai tabel persis paper.',
  'Sumber: stability_paths.csv; stata_cusum_paths.csv; CUSUM_cross_implementation_check.csv.')
 table_slide(d,'Keterbatasan data tetap memengaruhi arti hasil penelitian',
  'Integritas pengolahan sudah diperiksa; keseragaman definisi ekonomi belum sempurna.',
  ['Isu','Dampak pada pembacaan'],[
 ['Revisi HS tidak dinyatakan','Konsensus kode lintas revisi; mixed/unclassified tetap dikeluarkan dari kelompok terkait.'],
 ['Perdagangan nominal','Harga dan volume belum dipisahkan; tidak menguji kuantitas ekspor.'],
 ['Permintaan luar negeri dunia','Proksi GDP sepuluh mitra dengan bobot tetap, bukan GDP global.'],
 ['CPI dan kurs','India CPI mulai 2013; Australia memuat interpolasi penyedia; celah AS/Vietnam dipertahankan.'],
 ['Vintage GDP dan konsep FX','Historis beberapa negara dan perbedaan compiler masih memiliki catatan audit.'],
 ['Bounds sensitivitas India','Tiga model BCOM India tidak mempunyai inferensi bounds finite-sample yang tersedia.'],
 ['Musiman dan endogenitas','Perdagangan belum disesuaikan musiman; ARDL tidak otomatis mengidentifikasi efek kausal.']],
  'Pemeriksaan sumber meliputi checksum raw, rekonsiliasi HS-6 terhadap TOTAL dengan toleransi pembulatan, kunci waktu, kelengkapan kuartal, konstruksi kurs dan konsistensi hasil estimasi. Semua itu diperlukan tetapi tidak cukup untuk mengesahkan seluruh seri sebagai konsep ekonomi yang seragam. Keterangan sumber lama tetap diarsipkan. Seri perdagangan baru tidak mewarisi klaim selisih GEM dunia yang berasal dari run lama. Tiga kegagalan finite-sample bounds terjadi pada sensitivitas India dengan BCOM; koefisiennya tetap tersedia dan tidak dipakai sebagai dukungan level.',
  'Sumber: audit data HS-6; audit_validitas_data_macro.md; delivery_validation.json.',
  widths=[3.1,8.9],size=11.5)
 body_slide(d,'Komposisi barang membantu menjelaskan heterogenitas, tetapi belum menentukan mekanismenya',
  'Pembahasan ekonomi membedakan hasil yang terukur dari alasan yang masih perlu diuji.',
  'Yang didukung oleh run ini',
  'Tidak ada satu respons yang mewakili seluruh pasar dan kelompok. Beberapa hasil linier komoditas mengarah pada pemburukan, sementara pasar atau barang tertentu menunjukkan perbaikan dan urutan penyesuaian yang menyerupai J.',
  'Yang belum dapat dipastikan',
  'Regresi belum memisahkan harga ekspor dari volume, belum menguji perbedaan koefisien antarkelompok secara langsung, dan belum menyelesaikan respons dua arah antara kurs dan neraca. Penjelasan harga global masih bersifat interpretasi.',
  'Motivasi awal mengenai komoditas tetap relevan karena struktur ekspor Indonesia memang beragam dan komoditas mempunyai pangsa besar. Akan tetapi, ketidakpekaan terhadap kurs tidak dapat disimpulkan dari koefisien yang tidak signifikan. Untuk mendukung klaim itu diperlukan interval yang cukup sempit atau pengujian ekuivalensi dengan batas ekonomi yang dijustifikasi. Hubungan negatif pada suatu model juga dapat berasal dari respons impor, perubahan komposisi atau kejutan bersama. Karena itu, pembahasan menghindari perubahan diam-diam dari hasil rasio neraca menjadi klaim tentang ekspor saja.')
 body_slide(d,'Hasil belum memberi dasar bahwa depresiasi merupakan jaminan perbaikan neraca',
  'Kesimpulan penelitian sementara berangkat dari heterogenitas dan ketidakpastian yang terlihat.',
  'Kesimpulan substantif',
  'Manfaat depresiasi tidak tampak seragam. Agregat Indonesia belum memberi hubungan level yang kuat; perbedaan mitra dan jenis barang mengandung informasi yang hilang dalam rata-rata agregat. Sebagian pola J muncul, tetapi dukungannya tidak merata.',
  'Batas kesimpulan',
  'Bukti ini tidak cukup untuk menyatakan depresiasi selalu merugikan, komoditas pasti tidak sensitif, atau harga global sudah terbukti sebagai penyebab. Temuan yang lebih kuat tetap perlu bertahan pada sampel, spesifikasi dan pengukuran yang lebih seragam.',
  'Implikasi analitisnya adalah bahwa pembahasan kurs perlu mempertimbangkan jenis barang dan tujuan perdagangan, bukan memakai satu angka nasional sebagai respons universal. Ini bukan rekomendasi target kurs atau simulasi kebijakan yang telah diidentifikasi secara kausal. Langkah penelitian berikutnya yang relevan mencakup harmonisasi revisi HS, penyelarasan window, pemeriksaan musiman, dan pemisahan nilai dari kuantitas apabila data tersedia. Kanal input impor tidak diaktifkan kembali dalam penelitian ini.')
 s=table_slide(d,'Sumber dan referensi memungkinkan setiap hasil ditelusuri kembali',
  'Data lokal pengguna, dokumentasi klasifikasi, dan implementasi ekonometrika.',
  ['Komponen','Rujukan'],[
 ['Model utama','Bahmani-Oskooee & Fariditavana (2015/2016), Nonlinear ARDL Approach and the J-Curve Phenomenon. DOI 10.1007/s11079-015-9369-5.'],
 ['ARDL Stata dan bounds','Kripfganz & Schneider; implementasi ardl 1.0.6. DOI 10.1177/1536867X231212434.'],
 ['Klasifikasi produk','UNSD HS–SITC–BEC correlations 2022; BEC Rev.5; kelompok komoditas A11 UNCTAD.'],
 ['Perdagangan dan harga','22 workbook Trade Map HS-6 pengguna; workbook indeks komoditas pengguna.'],
 ['Kontrol makro dan stabilitas','BIS dan World Bank GEM sesuai manifest; dokumentasi resmi Stata estat sbcusum.'],
 ['Reproduksi','Do-file 00–07; laporan 08–09; deck 10 dan renderer 11. Semua sumber grafik tercantum di speaker notes.']],
  'Paper pengguna tersimpan dalam input/reference/oskooee_replication. Dokumentasi BEC menjelaskan penggunaan SNA sebagai dimensi tersendiri: https://unstats.un.org/unsd/trade/classifications/bec.asp. Korespondensi resmi: https://unstats.un.org/unsd/classifications/Econ/. Kelompok komoditas: https://unctadstat.unctad.org/EN/Classifications/DimSitcRev3Products_DsibSpecialGroupings_Hierarchy.pdf. CUSUM: https://www.stata.com/manuals/tsestatsbcusum.pdf. Respons harga BCOM berasal dari file pengguna; tidak ada klaim memakai Investing.com. Deck memakai hasil yang sudah diestimasi, tidak merunning kembali model.',
  'Sumber primer dan file referensi lokal Tio; tautan lengkap tersedia dalam speaker notes.',
  widths=[3.1,8.9],size=11.4)
 guide=body_slide(d,'Panduan membaca atlas hasil lengkap',
  'Versi lengkap menyertakan seluruh respons 176 model utama dan 340 sensitivitas.',
  'Atlas utama dan koefisien',
  'Lampiran A memuat setiap seri utama dengan ARDL dan NARDL berdampingan. Lampiran B memperlihatkan grafik koefisien tujuh kelompok Indonesia–seluruh dunia dan sepuluh mitra, lengkap dengan interval dan status model.',
  'Atlas sensitivitas',
  'Lampiran C mencakup pembatasan lag, kontrol BCOM, window dunia 2006+, WPI India dan keluarga kurs GEM alternatif. Tidak ada spesifikasi yang dihilangkan karena tandanya berbeda.',
  'Setiap panel respons mempunyai sumbu dan intervalnya sendiri; skala vertikal tidak selalu sama antar panel. Halaman utama memberikan penafsiran, sedangkan atlas memungkinkan pembaca mengecek apakah penafsiran itu mewakili keseluruhan hasil. Bentuk kurva tidak otomatis menjadi bukti J-curve. Definisi guncangan, orientasi tanda, band pointwise dan ketidakpastian sesudah seleksi AIC berlaku untuk seluruh lampiran. LaTeX asli setiap rumus serta PDF vector disertakan dalam folder equations.')
 return guide

def atlas(d,guide,assets):
 coverage=[];sections={}
 sec=section(d,'A','Atlas respons model utama',
  'Seluruh 88 seri utama disajikan dengan ARDL dan NARDL berdampingan: satu Indonesia–seluruh dunia, sepuluh mitra, serta tujuh kelompok Indonesia–seluruh dunia dan tiap mitra. Semua panel menampilkan depresiasi dan apresiasi berikut band pointwise nominal 95%.')
 sections['A']=sec
 series=['WORLD']+['BIL_'+iso for iso in ISOS]+['TYPE_'+iso+'_'+g for iso in COUNTRIES for g in GROUPS]
 assert len(series)==88 and len(set(series))==88
 patterns=CURVES.set_index('model_id')
 for sid in series:
  z=pair_for(sid);r=z.iloc[0]
  notes='\n\n'.join(note_row(v)+f' Bounds F {dec(v.F_pss,4)}, statistik t {dec(v.t_pss,4)}, probabilitas upper bound F {prob(v.F_pI1)}, probabilitas upper bound t {prob(v.t_pI1)}, probabilitas joint-X {prob(v.lr_x_p)}.' for _,v in z.iterrows())
  s=d.slide('Atlas A | '+trade_label(r),
   'ARDL dan NARDL utama | positif berarti perbaikan; skala vertikal berbeda antar panel.',
   'Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.',notes)
  st.picture(s,pair_asset(z,sid),.67,1.65,12,3.45)
  rows=[model_table_row(v) for _,v in z.iterrows()]
  st.table(s,['Model','Kuartal','Lag','Koef. dep.','Prob.','Level','Diagnostik'],rows,
   x=.67,y=5.22,w=12,h=1.02,widths=[1.05,1.0,2.05,1.7,1.35,1.8,2.05],size=10.5)
  desc=' | '.join(v.estimator+': '+patterns.loc[v.model_id,'point_pattern'].lower() for _,v in z.iterrows())
  st.text(s,.8,6.43,11.8,.36,desc,11,'dark')
  add_navigation(s,guide)
  d.slides[-1].update(section='A',model_ids=z.model_id.tolist())
  coverage.extend({'slide':len(d.slides),'section':'A','model_id':mid} for mid in z.model_id)
 sec=section(d,'B','Atlas koefisien tujuh kelompok',
  'Setiap pasar mempunyai grafik interval ARDL dan NARDL. Grafik memisahkan tanda koefisien, ketepatan estimasi dan status model. Ketujuh kategori bertumpang tindih; perbedaan signifikansi belum menjadi uji beda koefisien.')
 sections['B']=sec
 for iso in COUNTRIES:
  z=PRIMARY[PRIMARY.scope.eq('goods')&PRIMARY.ISO3.eq(iso)]
  s=graph_slide(d,'Atlas B | Indonesia–'+('seluruh dunia' if iso=='WLD' else COUNTRIES[iso])+': kelompok barang',
   'Positif: arah perbaikan saat depresiasi. Simbol kosong: dukungan level belum lengkap.',
   assets['forest_'+iso],
   'Cokelat: level dan diagnostik. Emas: level dengan catatan diagnostik. Grafik menampilkan semua interval; hasil tidak dipotong agar tampak lebih presisi.',
   '\n\n'.join(note_row(v) for _,v in z.iterrows()),
   'Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.')
  add_navigation(s,guide)
  d.slides[-1].update(section='B',model_ids=z.model_id.tolist())
 sec=section(d,'C','Atlas respons sensitivitas',
  'Seluruh 340 estimasi pembanding dipertahankan: cap dua, BCOM, window dunia 2006+, WPI India, serta kurs GEM alternatif. Maksimum dua seri per halaman menjaga agar kurva dan interval tetap terbaca.')
 sections['C']=sec
 sens=ALL[~ALL.model_id.isin(PRIMARY.model_id)]
 names={'main':'Maksimum dua lag level','world_2006_sensitivity':'Agregat Indonesia 2006+',
 'price_control':'Kontrol harga BCOM','price_BCOM':'Kontrol harga BCOM','BCOM':'Kontrol harga BCOM',
 'india_wpi':'India: WPI alternatif','India_WPI':'India: WPI alternatif','gem_fx':'Keluarga kurs GEM'}
 sensitivity_pages=0
 for scenario,ss in sens.groupby('scenario',sort=True):
  cases=list(ss.groupby(['series_id','cap'],sort=True))
  for _,v in cases:assert set(v.estimator)=={'ARDL','NARDL'} and len(v)==2
  for start in range(0,len(cases),2):
   chunk=cases[start:start+2];sensitivity_pages+=1
   friendly=names.get(scenario,scenario.replace('_',' '))
   if ss.price_control.eq(1).all():friendly='Kontrol harga BCOM'
   elif ss.uses_WPI.eq(1).all():friendly='India: WPI alternatif'
   elif 'GEM' in str(ss.series_id.iloc[0]):friendly='Keluarga kurs GEM alternatif'
   notes='Skenario '+scenario+'.\n\n'+'\n\n'.join(note_row(v) for _,case in chunk for _,v in case.iterrows())
   s=d.slide('Atlas C | '+friendly,
    'Setiap baris: perdagangan Indonesia dengan mitra yang tertera. Kiri ARDL; kanan NARDL.',
    'Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.',notes)
   key=re.sub(r'[^a-zA-Z0-9_-]','_',scenario)+'_'+str(start//2+1)
   st.picture(s,sensitivity_grid(chunk,key),.67,1.68,12,4.78)
   rows=[v for _,case in chunk for _,v in case.iterrows()]
   if any(v.Bounds5=='Unavailable' for v in rows):
    text='Catatan: inferensi bounds finite-sample tidak tersedia untuk sebagian model India pada halaman ini.'
   else:
    text='Kelayakan level, diagnostik, rentang sampel dan lag setiap spesifikasi dijelaskan dalam speaker notes.'
   st.text(s,.8,6.56,11.8,.29,text,10.5,'dark')
   add_navigation(s,guide)
   ids=[v.model_id for v in rows]
   d.slides[-1].update(section='C',model_ids=ids)
   coverage.extend({'slide':len(d.slides),'section':'C','model_id':mid} for mid in ids)
 # Internal links are added after saving the main version.
 for i,key in enumerate(['A','B','C']):
  sh=st.box(guide,.87+i*4.03,6.56,3.8,.36,'brown')
  sh.click_action.target_slide=sections[key]
  tx=st.text(guide,1.0+i*4.03,6.59,3.5,.23,'Buka lampiran '+key,10,'white',True,PP_ALIGN.CENTER)
  tx.click_action.target_slide=sections[key]
 return coverage,sensitivity_pages
def canonical_template_parts(path):
 with ZipFile(TEMPLATE) as z1,ZipFile(path) as z2:
  parts=[x for x in z1.namelist() if x.endswith('.xml') and x.startswith(('ppt/theme/','ppt/slideMasters/','ppt/slideLayouts/'))]
  return {x:etree.tostring(etree.fromstring(z1.read(x)),method='c14n')==etree.tostring(etree.fromstring(z2.read(x)),method='c14n') for x in parts}
def build():
 load()
 files=[T/'results_primary_models.csv',T/'results_all_models.csv',D/'dynamic_multipliers.csv',
  ROOT/'intermediate/Trade_Total_Quarter.csv',ROOT/'intermediate/Trade_Goods_Quarter.csv',
  ROOT/'intermediate/HS6_Classification.csv',D/'case_registry.csv',D/'stability_paths.csv',
  ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv',D/'delivery_validation.json',TEMPLATE]
 before={str(p.relative_to(ROOT)):sha(p) for p in files}
 render_equations()
 a,f=prepare_assets()
 d=st.Deck(TEMPLATE);guide=main_slides(d,a,f)
 main_count=len(d.p.slides)
 for v in d.slides:v.setdefault('section','Utama');v.setdefault('model_ids',[])
 main_path=OUT/'Depresiasi_Rupiah_HS6_Tio_20261117_Utama.pptx'
 d.p.core_properties.subject='Penelitian HS-6 | statistik deskriptif, ARDL, NARDL dan J-curve'
 d.p.save(main_path)
 coverage,sens_pages=atlas(d,guide,a)
 full_path=OUT/'Depresiasi_Rupiah_HS6_Tio_20261117_Lengkap.pptx'
 d.p.save(full_path)
 cover=pd.DataFrame(coverage)
 assert len(cover)==516 and cover.model_id.nunique()==516
 assert set(cover.model_id)==set(ALL.model_id)
 assert set(cover[cover.section.eq('A')].model_id)==set(PRIMARY.model_id)
 cover.to_csv(OUT/'model_response_slide_index.csv',index=False)
 after={str(p.relative_to(ROOT)):sha(p) for p in files}
 assert before==after,'Source data changed during presentation build'
 canon=canonical_template_parts(full_path);assert all(canon.values())
 notes='\n\n'.join('## '+str(v['slide']).zfill(3)+'. '+v['title']+'\n\n'+v['notes'] for v in d.slides)
 (OUT/'slide_notes.md').write_text(notes,encoding='utf-8')
 index=pd.DataFrame([{'Slide':v['slide'],'Bagian':v.get('section','Pembatas'),'Judul':v['title'],
   'Model':';'.join(v.get('model_ids',[]))} for v in d.slides])
 index.to_csv(OUT/'slide_index.csv',index=False,encoding='utf-8-sig')
 report={'status':'BUILT_PENDING_RENDER','main_slides':main_count,'full_slides':len(d.p.slides),
  'primary_model_response_panels':176,'sensitivity_model_response_panels':340,'sensitivity_atlas_pages':sens_pages,
  'all_516_model_responses_in_full_deck':True,'each_model_has_both_shock_directions':True,
  'response_display':'Exact sign reversal: 100*change log(X/M), not estimated outcome log(M/X)',
  'shock':'q +/- ln(1.10); no claim of symmetric arithmetic 10 percent shocks',
  'uncertainty':'Nominal pointwise delta-method 95% intervals after AIC selection',
  'J_classification':'Exploratory visual-operational; not a formal joint J-curve test',
  'latex_equations':len(FORMULAS),'latex_engine':'pdfLaTeX / TeX Live 2025',
  'equation_format':'Genuine LaTeX -> PDF/SVG, PNG fallback; SVG embedded in PPTX',
  'font_policy':'Original Arial Nova cover; Arial body; TeX math fonts for equations',
  'template':str(TEMPLATE),'template_sha256':sha(TEMPLATE),
  'all_master_layout_theme_parts_preserved':all(canon.values()),'template_xml_parts_preserved':len(canon),
  'input_files_unchanged':before==after,'input_sha256':before,
  'files':{'main_pptx':main_path.name,'full_pptx':full_path.name},
  'pptx_sha256':{main_path.name:sha(main_path),full_path.name:sha(full_path)},
  'source_code':'script/10_build_research_ppt.py; script/python/presentation_style.py'}
 (OUT/'deck_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
 (OUT/'README.md').write_text("""# Presentasi penelitian HS-6

Utama.pptx berisi pembahasan penelitian. Lengkap.pptx memuat pembahasan yang sama, ditambah seluruh respons 176 model utama dan 340 sensitivitas serta grafik koefisien per pasar.

Cover, foto, master, font dan palet mengikuti template pengguna. Teks dan tabel utama dapat diedit. Rumus dirender dengan pdfLaTeX dan ditanam sebagai SVG dengan PNG fallback; sumber LaTeX, PDF vector dan SVG tersedia dalam equations/. Grafik berasal dari hasil Stata yang telah ada, bukan estimasi baru.

Grafik respons memakai perubahan log rasio ekspor/impor agar nilai positif berarti perbaikan. Ini pembalikan tanda tepat dari outcome model log impor/ekspor. Interval ikut ditransformasi. Guncangan kedua arah simetris dalam log, bukan dalam persen aritmetika. Pola J eksploratif tidak sama dengan uji kausal atau uji simultan.

slide_index.csv memuat daftar isi. model_response_slide_index.csv memetakan setiap model ke halaman atlas. slide_notes.md memuat pembahasan dan sumber setiap slide. assets/ memuat data deskriptif dan grafik PNG/PDF. deck_validation.json memuat checksum, kelengkapan model, pelestarian template dan pemeriksaan render.

Reproduksi: jalankan script/10_build_research_ppt.py, kemudian script/11_render_research_ppt.py. Paket Python mengikuti lingkungan proyek. Tidak ada dataset atau hasil estimasi yang diganti saat membuat deck.
""",encoding='utf-8')
 print(json.dumps({k:report[k] for k in ['status','main_slides','full_slides','all_516_model_responses_in_full_deck','latex_equations','all_master_layout_theme_parts_preserved']},indent=2),flush=True)
if __name__=='__main__':build()
