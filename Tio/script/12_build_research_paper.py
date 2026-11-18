"""Create an elaborative Indonesian working paper from existing Stata results."""
from pathlib import Path
import json,hashlib,math,re,subprocess,shutil,textwrap
import numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/paper';A=OUT/'assets';TB=OUT/'tables'
for p in [OUT,A,TB]:p.mkdir(parents=True,exist_ok=True)
T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee'
S=pd.read_csv(T/'results_primary_models.csv');ALL=pd.read_csv(T/'results_all_models.csv')
DM=pd.read_csv(D/'dynamic_multipliers.csv')
TOTAL=pd.read_csv(ROOT/'intermediate/Trade_Total_Quarter.csv')
GOODS=pd.read_csv(ROOT/'intermediate/Trade_Goods_Quarter.csv')
REG=pd.read_csv(D/'case_registry.csv')
CURVES=pd.read_csv(ROOT/'output/presentation/assets/jcurve_classification_all_516.csv')
ISO={'WLD':'seluruh dunia','AUS':'Australia','CHN':'Tiongkok','IND':'India','JPN':'Jepang',
 'KOR':'Korea Selatan','MYS':'Malaysia','SGP':'Singapura','THA':'Thailand','USA':'Amerika Serikat','VNM':'Vietnam'}
G={'manufacturing':'Manufaktur nonkomoditas','consumption':'Barang konsumsi','agriculture':'Pertanian dan pangan',
 'intermediate':'Bahan baku/penolong','capital':'Barang modal','commodity':'Komoditas total','energy_mining':'Energi dan tambang'}
GC={g:'G'+str(i+1) for i,g in enumerate(G)}
COL={'brown':'#A5644E','dark':'#4E3B30','gold':'#C17529','blue':'#2F5D8C','gray':'#777777','beige':'#F2E8E1','grid':'#E5DFDA'}
plt.rcParams.update({'font.family':'Arial','font.size':10,'mathtext.fontset':'cm',
 'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#B8ACA3',
 'figure.facecolor':'white','savefig.facecolor':'white','pdf.fonttype':42})
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def esc(v):
 s=str(v)
 repl={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
 s=''.join(repl.get(c,c) for c in s)
 return s.replace('–','--').replace('—','---').replace('−',r'\(-\)')
def num(v,n=3):
 if pd.isna(v):return '--'
 return f'{float(v):,.{n}f}'.replace(',','|').replace('.',',').replace('|','.')
def pv(v):
 if pd.isna(v):return '--'
 return r'\(<0{,}001\)' if v<.001 else num(v,3)
def coeff(r):
 k='lr_q' if r.estimator=='ARDL' else 'lr_neg'
 return r[k+'_b'],r[k+'_lo95'],r[k+'_hi95'],r[k+'_p']
def case(sid):return S[S.series_id.eq(sid)].sort_values('estimator')
def status(r):return 'L+D' if r.Levels_supported5 and r.Diagnostic_clean5 else 'L' if r.Levels_supported5 else '--'
def risk(r):
 words=[]
 if r.Bounds5!='Reject no-level relation':words.append('F/t bounds belum menolak')
 if not pd.isna(r.lr_x_p) and r.lr_x_p>=.05:words.append('joint-X belum menolak')
 if r.I2_not_ruled_out:words.append('risiko integrasi orde dua')
 if not r.Dynamic_stable:words.append('akar tidak stabil')
 if r.df_r<15:words.append('derajat bebas kurang dari 15')
 if not r.Diagnostic_clean5:words.append('catatan diagnostik residual/stabilitas')
 return '; '.join(words) or 'tidak ada penolakan pada penyaringan yang digunakan'
def save(fig,name):
 fig.savefig(A/(name+'.pdf'),bbox_inches='tight',pad_inches=.06)
 fig.savefig(A/(name+'.png'),dpi=180,bbox_inches='tight',pad_inches=.06)
 plt.close(fig)
def grid(ax,axis='y'):ax.grid(axis=axis,color=COL['grid'],lw=.55);ax.set_axisbelow(True)
def response(ax,r,title=None):
 z=DM[DM.model_id.eq(r.model_id)].copy();assert len(z)==50
 for direction,label,col in [('depreciation','Depresiasi','brown'),('appreciation','Apresiasi','blue')]:
  a=z[z.direction.eq(direction)].sort_values('horizon_quarters')
  ax.plot(a.horizon_quarters,-a.effect_logpoints,color=COL[col],lw=1.65,label=label)
  ax.fill_between(a.horizon_quarters,-a.upper95_logpoints,-a.lower95_logpoints,color=COL[col],alpha=.14,lw=0)
 ax.axhline(0,color=COL['gray'],lw=.65);ax.set_xlim(0,24);ax.set_xticks([0,4,8,12,16,20,24])
 ax.set_xlabel('Kuartal setelah guncangan',fontsize=9)
 ax.set_ylabel(r'$100\,\Delta\ln(X/M)$',fontsize=11)
 ax.set_title(title or r.estimator+' | '+status(r),loc='left',fontsize=10,fontweight='bold')
 ax.legend(frameon=False,ncol=2,fontsize=8,loc='best');grid(ax)
def pairplot(sid,name=None):
 z=case(sid);assert len(z)==2
 fig,axes=plt.subplots(2,1,figsize=(6.2,4.65))
 for ax,(_,r) in zip(axes,z.iterrows()):response(ax,r,r.estimator+' | '+('level + diagnostik' if status(r)=='L+D' else 'level; catatan diagnostik' if status(r)=='L' else 'dukungan level belum lengkap'))
 fig.tight_layout(h_pad=1.7);save(fig,name or 'response_'+sid)
def figs():
 w=TOTAL[TOTAL.ISO3.eq('WLD')].copy();w['Year']=w.Quarter.str[:4].astype(int)
 annual=w.groupby('Year')[['Exports_USDk','Imports_USDk','Trade_Balance_USDk']].sum(min_count=4).loc[2006:2025]/1e6
 annual.rename(columns=lambda c:c.replace('USDk','USDbn')).to_csv(A/'indonesia_annual_trade_USDbn.csv')
 fig,ax=plt.subplots(2,1,figsize=(6.2,4.1),sharex=True,gridspec_kw={'height_ratios':[1.5,1]})
 ax[0].plot(annual.index,annual.Exports_USDk,color=COL['brown'],lw=1.8,label='Ekspor Indonesia')
 ax[0].plot(annual.index,annual.Imports_USDk,color=COL['dark'],lw=1.6,label='Impor Indonesia')
 ax[0].legend(frameon=False,fontsize=8);ax[0].set_ylabel('USD miliar');grid(ax[0])
 ax[1].bar(annual.index,annual.Trade_Balance_USDk,color=COL['brown']);ax[1].axhline(0,color=COL['gray'],lw=.6)
 ax[1].set_ylabel('Neraca, USD miliar');ax[1].set_xticks([2006,2010,2014,2018,2022,2025]);grid(ax[1]);fig.tight_layout();save(fig,'indonesia_annual')
 pairplot('WORLD')
 for iso in list(ISO)[1:]:pairplot('BIL_'+iso)
 for g in ['commodity','energy_mining','manufacturing','consumption']:pairplot('TYPE_WLD_'+g)
 for sid in ['TYPE_CHN_agriculture','TYPE_KOR_capital','TYPE_USA_consumption']:pairplot(sid)
 # Bilateral long-run intervals, plotted in their estimated coefficient orientation.
 z=S[S.scope.eq('bilateral')&S.estimator.eq('NARDL')].set_index('ISO3').loc[list(ISO)[1:]].reset_index()
 fig,ax=plt.subplots(figsize=(6.2,4.2))
 for i,r in z.iterrows():
  c=COL['brown'] if status(r)=='L+D' else COL['gold'] if status(r)=='L' else COL['gray']
  ax.plot([r.lr_neg_lo95,r.lr_neg_hi95],[i,i],color=c,lw=1.6)
  ax.scatter([r.lr_neg_b],[i],s=30,edgecolor=c,facecolor=c if r.Levels_supported5 else 'white',zorder=3)
 ax.axvline(0,color=COL['dark'],lw=.7);ax.set_yticks(range(10),[ISO[x] for x in z.ISO3],fontsize=9);ax.invert_yaxis()
 ax.set_xlabel(r'Koefisien jangka panjang $\beta_-$');grid(ax,'x');fig.tight_layout();save(fig,'bilateral_forest')
 fig,axs=plt.subplots(2,1,figsize=(6.2,6.4))
 for ax,est in zip(axs,['ARDL','NARDL']):
  z=S[S.ISO3.eq('WLD')&S.scope.eq('goods')&S.estimator.eq(est)].set_index('Group').loc[list(G)].reset_index()
  for i,r in z.iterrows():
   b,lo,hi,p=coeff(r);c=COL['brown'] if status(r)=='L+D' else COL['gold'] if status(r)=='L' else COL['gray']
   ax.plot([lo,hi],[i,i],color=c,lw=1.6)
   ax.scatter([b],[i],s=28,edgecolor=c,facecolor=c if r.Levels_supported5 else 'white',zorder=3)
  ax.axvline(0,color=COL['dark'],lw=.7);ax.set_yticks(range(7),[G[x] for x in z.Group],fontsize=8.5);ax.invert_yaxis()
  ax.set_title(est,loc='left',fontsize=11,fontweight='bold');ax.set_xlabel(r'$\beta_q$' if est=='ARDL' else r'$\beta_-$',fontsize=12);grid(ax,'x')
 fig.tight_layout(h_pad=2.4);save(fig,'world_goods_forest')
 z=pd.read_csv(D/'stability_paths.csv')
 fig,ax=plt.subplots(2,1,figsize=(6.2,4.8))
 for a,mid,label in zip(ax,['WORLD_NARDL_AIC4','BIL_AUS_NARDL_AIC4'],['Indonesia–seluruh dunia','Indonesia–Australia']):
  q=z[z.model_id.eq(mid)];x=1960+q.tq/4
  a.fill_between(x,q.lower,q.upper,color=COL['beige']);a.plot(x,q.expected,':',color=COL['gray'])
  a.plot(x,q.CUSUMSQ,color=COL['brown'],lw=1.6);a.set_title(label,fontsize=10,loc='left');a.set_ylim(-.03,1.03);grid(a)
 fig.tight_layout(h_pad=1.8);save(fig,'stability')
 # Two NARDL examples used to explain pointwise two-phase evidence.
 fig,axs=plt.subplots(2,1,figsize=(6.2,4.65))
 for ax,sid,label in zip(axs,['TYPE_KOR_capital','TYPE_USA_consumption'],['Indonesia--Korea: barang modal','Indonesia--AS: konsumsi']):
  r=case(sid);r=r[r.estimator.eq('NARDL')].iloc[0]
  response(ax,r,label)
 fig.tight_layout(h_pad=1.7);save(fig,'J_examples')

def table(name,heads,rows,widths=None,long=False,size='small'):
 n=len(heads)
 spec=''.join('p{'+str(w)+r'\linewidth}' for w in widths) if widths else 'l'+'r'*(n-1)
 env='longtable' if long else 'tabular'
 txt=[r'{\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.18}\\'+size if False else '{\\'+size+r'\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.15}',
  r'\begin{'+env+'}{'+spec+'}',r'\toprule',
  ' & '.join(r'\textbf{'+esc(h)+'}' for h in heads)+r'\\',r'\midrule']
 if long:
  txt +=[r'\endfirsthead',r'\toprule',' & '.join(r'\textbf{'+esc(h)+'}' for h in heads)+r'\\',r'\midrule',r'\endhead',
   r'\midrule\multicolumn{'+str(n)+r'}{r}{\footnotesize Bersambung ke halaman berikutnya}\\\endfoot',
   r'\bottomrule\endlastfoot']
 txt += [' & '.join(str(x) for x in r)+r'\\' for r in rows]
 if not long:txt.append(r'\bottomrule')
 txt +=[r'\end{'+env+'}','}']
 (TB/(name+'.tex')).write_text('\n'.join(txt),encoding='utf-8')
def tables():
 d=pd.read_csv(ROOT/'output/presentation/assets/descriptive_world_estimation_sample.csv')
 rows=[[esc(r[0]),str(int(r[1]))]+[num(v,2) for v in r[2:]] for r in d.itertuples(index=False,name=None)]
 table('descriptives',['Variabel','N','Rerata','SD','Min.','Maks.'],rows,widths=[.32,.045,.12,.12,.12,.12])
 rows=[]
 for iso in list(ISO)[1:]:
  r=S[S.series_id.eq('BIL_'+iso)&S.estimator.eq('NARDL')].iloc[0]
  rows.append([esc(ISO[iso]),str(int(r.N)),esc(r.Estimation_Start+'--'+r.Estimation_End),
    num(r.lr_neg_b),pv(r.lr_neg_p),pv(r.Dep_LR_p_BH),status(r)])
 table('bilateral',['Mitra','N','Rentang','Koef. dep.','p','BH','Status'],rows,widths=[.17,.045,.20,.12,.09,.09,.07])
 rows=[]
 for g in G:
  for est in ['ARDL','NARDL']:
   r=S[S.series_id.eq('TYPE_WLD_'+g)&S.estimator.eq(est)].iloc[0];b,lo,hi,p=coeff(r)
   rows.append([GC[g],est,num(b),f'[{num(lo)}; {num(hi)}]',pv(p),pv(r.Dep_LR_p_BH),status(r)])
 table('goods_world',['Kel.','Model','Koef.','CI nominal 95%','p','BH','Status'],rows,widths=[.05,.105,.10,.25,.10,.10,.07])
 rows=[]
 for g in ['commodity','energy_mining']:
  for prefix,cap,label in [('TYPE',4,'Utama'),('TYPE',2,'Cap 2'),('PRICE',4,'BCOM')]:
   r=ALL[ALL.series_id.eq(prefix+'_WLD_'+g)&ALL.estimator.eq('ARDL')&ALL.cap.eq(cap)].iloc[0]
   rows.append([GC[g],label,str(int(r.N)),num(r.lr_q_b),pv(r.lr_q_p),status(r)])
 table('sensitivity',['Kel.','Varian','N','Koef. kurs','p','Status'],rows,widths=[.08,.20,.08,.20,.15,.12])
 c=CURVES[CURVES.model_id.isin(S.model_id)];rows=[]
 for est,g in c.groupby('estimator'):
  jj=g.point_pattern.eq('Pola J pada estimasi titik');ok=g.Levels_supported5&g.Diagnostic_clean5
  rows.append([est,len(g),int(jj.sum()),int((jj&ok).sum()),int((jj&ok&g.phase_CI_separated).sum())])
 table('jcounts',['Model','Seri','J titik','J + L+D','Dua fase CI'],rows,widths=[.18,.12,.15,.21,.23])
 rows=[]
 for _,r in S[S.scope.eq('aggregate')].iterrows():
  rows.append([r.estimator,num(r.F_pss),num(r.t_pss),pv(r.F_pI1),pv(r.t_pI1),pv(r.lr_x_p),esc(r.Bounds5)])
 table('world_bounds',['Model','F','t','p F(I1)','p t(I1)','p joint-X','Keputusan'],rows,widths=[.10,.08,.08,.10,.10,.12,.22])
 # Complete reporting: all models retained, including unsupported levels.
 for filename,frame in [('all_primary',S),('all_sensitivity',ALL[~ALL.model_id.isin(S.model_id)])]:
  rows=[]
  for _,r in frame.sort_values(['scenario','ISO3','Group','series_id','estimator','cap']).iterrows():
   b,lo,hi,p=coeff(r)
   scenario='L2' if r.cap==2 else 'P' if r.price_control else 'W06' if r.series_id=='WORLD_FULL' else 'WPI' if r.uses_WPI else 'FX' if str(r.series_id).startswith('GEM_') else 'U'
   rows.append([r.ISO3,GC.get(r.Group,'G0'),r.estimator,str(int(r.N)),scenario,
    num(b),pv(p),pv(r.Dep_LR_p_BH) if filename=='all_primary' else '--',status(r)])
  table(filename,['Mitra','Kel.','Model','N','Var.','Koef.','p','BH','Status'],rows,
   widths=[.075,.05,.09,.04,.05,.10,.085,.085,.075],long=True,size='footnotesize')
 (A/'result_reading_index.csv').write_text(S[['model_id','ISO3','Group','estimator','N','Levels_supported5','Diagnostic_clean5','Dep_LR_p','Dep_LR_p_BH']].to_csv(index=False),encoding='utf-8')
def macrofile():
 w=TOTAL[TOTAL.ISO3.eq('WLD')&TOTAL.Quarter.str.startswith('2025')][['Exports_USDk','Imports_USDk','Trade_Balance_USDk']].sum()/1e6
 c=pd.read_csv(ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv')
 c=c[c.ISO3.eq('WLD')&c.Flow.eq('Export')&c.Year.eq(2025)&c.Classification.eq('Commodity_Class')].set_index('Class')
 au=S[S.model_id.eq('BIL_AUS_NARDL_AIC4')].iloc[0]
 shock=-np.log(1.1);delta=-au.lr_neg_b*shock;percentage=100*np.expm1(delta)
 vals={'WorldExports':num(w.Exports_USDk,2),'WorldImports':num(w.Imports_USDk,2),'WorldNet':num(w.Trade_Balance_USDk,2),
 'CommodityShare':num(c.loc['commodity','Value_Share_pct'],1),'ManufacturingShare':num(c.loc['noncommodity','Value_Share_pct'],1),
 'AusBeta':num(au.lr_neg_b,4),'AusResponse':num(100*delta,2),'AusRatioPct':num(percentage,2),
 'AusBetaMath':num(au.lr_neg_b,4).replace(',','{,}'),'AusResponseMath':num(100*delta,2).replace(',','{,}')}
 (OUT/'numbers.tex').write_text('\n'.join(chr(92)+'newcommand{'+chr(92)+k+'}{'+v+'}' for k,v in vals.items()),encoding='utf-8')
 (A/'numbers.json').write_text(json.dumps(vals,indent=2),encoding='utf-8')
def figure_tex(name,caption,label,width=r'\linewidth',height=None):
 opt='width='+width+(',height='+height+',keepaspectratio' if height else '')
 return r'\begin{figure}[!htbp]\centering\includegraphics['+opt+']{assets/'+name+r'.pdf}\caption{'+caption+r'}\label{fig:'+label+r'}\end{figure}'+'\n'

CASE_DISCUSSION={
'AUS':"""Australia menjadi contoh yang lebih mendukung perbaikan rasio neraca saat depresiasi. ARDL dan NARDL sama-sama memenuhi penyaringan level dan diagnostik. Koefisien depresiasi NARDL tetap signifikan setelah BH dalam keluarga bilateral, sedangkan Wald kesamaan apresiasi dan depresiasi tidak ditolak pada lima persen. Pemakaian NARDL karena itu tidak berarti asimetri pasti ditemukan.

Estimasi titik NARDL mempunyai pemburukan awal lalu perbaikan. Band awal masih melintasi nol, sehingga urutan J tidak terkonfirmasi sama kuat pada dua fase. Pernyataan yang lebih tepat adalah adanya pola J pada titik yang didukung kelayakan model, dengan ketidakpastian fase awal. Ini berbeda dari menyatakan depresiasi pasti menurunkan neraca pada kuartal pertama.""",
'CHN':"""Besarnya nilai perdagangan dengan Tiongkok tidak membuat koefisiennya otomatis paling presisi atau paling dapat ditafsirkan. Kedua model bilateral utama belum memenuhi syarat level lengkap. Pada NARDL terdapat catatan korelasi serial; pada ARDL CUSUM ditolak. Arah negatif belum dapat dipakai sebagai bukti jangka panjang bahwa depresiasi merugikan seluruh perdagangan Indonesia dengan Tiongkok.

Hasil kelompok pertanian dengan Tiongkok kemudian memberi gambaran yang lebih terukur. Perbedaan hasil total dan kelompok menandai peran agregasi, tetapi belum merupakan uji bahwa kedua koefisiennya berbeda secara statistik. Defisit bilateral yang besar pada statistik tahunan juga tidak mengidentifikasi sebab akibat dari perubahan kurs.""",
'IND':"""India memakai sampel yang lebih pendek karena baseline menggunakan CPI mulai 2013. Dengan tambahan partial sums dan lag, ruang informasi per parameter menjadi terbatas. Koefisien depresiasi NARDL negatif tetapi intervalnya lebar; bounds belum mendukung level. Penolakan Wald asimetri tidak mengatasi masalah tersebut.

Model NARDL tidak ditolak pada penyaringan residual yang dipakai, sedangkan ARDL mempunyai catatan korelasi serial dan RESET. Ini contoh model yang residualnya tampak lebih mendukung tetapi hubungan levelnya belum memenuhi syarat. WPI menyediakan sensitivitas terpisah dengan konsep harga serta rentang yang berbeda; ia tidak diperlakukan sebagai CPI murni untuk memperpanjang baseline.""",
'JPN':"""Jepang memperlihatkan mengapa probabilitas koefisien saja dapat menyesatkan. Koefisien depresiasi NARDL negatif dan signifikan nominal maupun BH dalam keluarga bilateral. F upper bound menolak pada lima persen, tetapi t upper bound belum melewati ambang yang sama. Penyaringan hubungan level lengkap karena itu belum terpenuhi.

Selain itu, ARCH dan normalitas residual memberi catatan. Hasil ini tidak dihapus dari pelaporan, tetapi bobot penafsirannya berbeda dari kasus yang mendukung level dan diagnostik. Tanda negatif menjadi indikasi yang memerlukan peninjauan spesifikasi, bukan kesimpulan kausal mengenai respons ekspor Indonesia ke Jepang.""",
'KOR':"""NARDL Korea menghasilkan koefisien depresiasi positif dengan ketidakpastian yang cukup besar. Dukungan level belum lengkap, dan korelasi serial, RESET serta CUSUM memberi catatan. ARDL lebih dekat ke nol tetapi juga belum mendukung level. Kedua hasil belum menetapkan bahwa efek nasional pada mitra ini kecil ataupun positif secara pasti.

Pada kelompok modal, NARDL mempunyai pola J yang lebih jelas dan lolos penyaringan utama. Kontras ini menunjukkan bahwa hasil agregat mitra dapat menyembunyikan respons kelompok tertentu. Kelompok modal tetap tidak mewakili semua ekspor ke Korea, dan band jalurnya masih bersifat pointwise.""",
'MYS':"""Malaysia menunjukkan perbedaan yang nyata antara spesifikasi linier dan nonlinear. ARDL mempunyai dukungan level tetapi koefisien kursnya negatif, tidak signifikan pada lima persen, serta mempunyai catatan RESET dan CUSUM. NARDL memberi koefisien depresiasi positif, dukungan level dan diagnostik yang lebih baik, serta penolakan asimetri.

Probabilitas depresiasi NARDL sekitar 0,024 secara nominal, tetapi BH sekitar 0,059. Dengan demikian, klaim signifikansinya berubah menurut apakah pengujian berganda diperhitungkan. Respons yang cenderung membaik tidak harus diberi nama J-curve apabila fase awal yang memburuk tidak muncul. Temuan ini mendukung pembacaan perbaikan kondisional dengan ketahanan signifikansi yang terbatas.""",
'SGP':"""Pada Singapura, F dan t bounds dapat menolak sementara joint-X tidak mendukung. Keputusan level lengkap karena itu tetap belum lolos. ARDL juga memberi contoh bahwa diagnostik yang tidak ditolak tidak cukup bila komponen level regressor belum terdukung. NARDL menambahkan catatan korelasi serial.

Koefisien depresiasi NARDL dekat nol dalam titik dibandingkan beberapa mitra lain, tetapi intervalnya tetap harus dibaca sebelum menyebut ketidakpekaan. Run ini tidak melakukan uji ekuivalensi efek kecil. Hasil yang paling dapat dipertahankan adalah belum adanya hubungan jangka panjang yang cukup didukung pada spesifikasi utama.""",
'THA':"""Thailand berbeda dari banyak pasangan karena kedua model memenuhi syarat level operasional. Namun ARCH dan CUSUMSQ ditolak, dengan tambahan CUSUM pada NARDL. Dukungan kointegrasi dan kestabilan residual karena itu tidak bergerak bersama. Koefisien positif NARDL juga belum signifikan secara nominal.

Kurs Thailand mempunyai catatan perbedaan konsep antarcompiler. Keluarga GEM dijalankan penuh sebagai sensitivitas, bukan digunakan untuk menambal satu observasi baseline. Perbandingan sumber tetap perlu memperhatikan apakah window dan definisinya sama. Sampai isu tersebut diperiksa lebih jauh, koefisien tidak dibaca sebagai efek kebijakan yang telah stabil.""",
'USA':"""AS menghasilkan koefisien depresiasi NARDL yang positif dan signifikan nominal maupun BH. F dan t bounds juga menolak. Namun joint-X sekitar 0,060 belum melewati ambang lima persen, sehingga syarat level tambahan tidak terpenuhi. CUSUMSQ dan normalitas residual memberi catatan lain.

Sampel berhenti pada 2025Q3 akibat kekosongan CPI Oktober 2025 pada keluarga utama. Kelompok konsumsi dengan AS mempunyai dukungan berbeda dan memperlihatkan pola J yang lebih jelas. Hal tersebut tidak menyelesaikan kekurangan model total, karena agregasi barang dan persamaan yang diuji berbeda.""",
'VNM':"""Vietnam mempunyai catatan varians dan stabilitas yang cukup luas. NARDL memberikan koefisien depresiasi negatif yang tidak signifikan, sedangkan t bounds belum mendukung keputusan level. ARDL juga belum memenuhi seluruh syarat dan menolak beberapa diagnostik. Koefisien tidak dipilih hanya karena arahnya sesuai atau bertentangan dengan hipotesis.

Kekosongan kurs Agustus 2025 memotong jendela utama yang lengkap pada 2025Q2. Prosedur tidak merapatkan kuartal setelah celah dan menganggapnya berurutan. Alternatif GEM tetap merupakan sensitivitas dengan konsep sumber yang mungkin berbeda. Keterbatasan itu memengaruhi perbandingan Vietnam dengan mitra yang berakhir lebih akhir."""
}
def bilateral_text():
 p=[r'\section{Hasil bilateral sepuluh mitra}\label{sec:bilateral}',
 r'\subsection{Perbedaan arah dan dukungan model}',
 'Hasil bilateral membedakan satu hubungan agregat menjadi sepuluh pengalaman pasar. Tabel berikut memakai koefisien depresiasi NARDL dan window setelah holdback. Australia dan Malaysia memenuhi penyaringan level serta diagnostik utama, tetapi signifikansi keduanya tidak sama tahan terhadap BH. Model lain tetap dilaporkan walaupun mempunyai koefisien besar atau probabilitas kecil tanpa dukungan level lengkap.',
 r'\begin{table}[!htbp]\centering\caption{Ringkasan NARDL bilateral Indonesia}\input{tables/bilateral.tex}\label{tab:bilateral}\end{table}',
 figure_tex('bilateral_forest','Koefisien depresiasi bilateral NARDL. Warna cokelat menunjukkan L+D, emas L, dan simbol kosong dukungan level belum lengkap. Semua negara pada sumbu adalah mitra Indonesia.','bilateralforest'),
 'Perbedaan antarmitra belum merupakan uji formal selisih koefisien pada sampel sama. India berawal lebih akhir, sedangkan AS dan Vietnam berakhir lebih awal. Regresi yang berbeda juga mengendalikan GDP dan kurs bilateral yang berbeda. Uraian tiap mitra berikut menghubungkan angka, status dan grafik agar penafsiran tidak bergantung pada satu kolom bintang.']
 for iso,discussion in CASE_DISCUSSION.items():
  z=case('BIL_'+iso);r=z[z.estimator.eq('NARDL')].iloc[0]
  b,lo,hi,pv0=coeff(r)
  overview=(f"NARDL Indonesia--{esc(ISO[iso])} memakai {int(r.N)} kuartal pada {r.Estimation_Start}--{r.Estimation_End}. "
   f"Koefisien depresiasi {num(b)}, CI nominal 95\\% [{num(lo)}; {num(hi)}], probabilitas nominal {pv(pv0)}, dan BH {pv(r.Dep_LR_p_BH)}. "
   f"Probabilitas asimetri jangka panjang {pv(r.lr_asym_p)}. Pemeriksaan yang membatasi: {esc(risk(r))}.")
  p +=[r'\clearpage\subsection{Indonesia--'+esc(ISO[iso])+'}',overview,discussion,
    figure_tex('response_BIL_'+iso,'Respons perdagangan Indonesia--'+esc(ISO[iso])+r'. Positif berarti perbaikan rasio ekspor/impor. Band pointwise nominal 95\%; skala kedua panel berbeda.','bil'+iso)]
 (OUT/'sections/05_bilateral.tex').write_text('\n\n'.join(p),encoding='utf-8')
def build():
 inputs=[T/'results_primary_models.csv',T/'results_all_models.csv',T/'coefficients_ecm_with_LR_constant.csv',
 D/'dynamic_multipliers.csv',D/'stability_paths.csv',D/'analysis_validation_report.json',
 ROOT/'intermediate/Trade_Total_Quarter.csv',ROOT/'intermediate/Trade_Goods_Quarter.csv',
 ROOT/'intermediate/HS6_Classification.csv',D/'case_registry.csv',
 ROOT/'output/diagnostics/data/Classification_Coverage_By_Year.csv',
 ROOT/'output/presentation/scope_audit_indonesia.json',ROOT/'output/presentation/assets/jcurve_classification_all_516.csv',
 ROOT/'output/presentation/assets/descriptive_world_estimation_sample.csv']
 before={str(p.relative_to(ROOT)):sha(p) for p in inputs}
 assert len(S)==176 and len(ALL)==516 and ALL.model_id.is_unique
 import logging
 logging.getLogger('fontTools').setLevel(logging.ERROR)
 figs();tables();macrofile();bilateral_text()
 # Fix a wording shortcut; all figures and models remain centered on Indonesia.
 q=OUT/'sections/07_diagnostics.tex';s=q.read_text('utf-8').replace('Dunia agregat Indonesia','Agregat perdagangan Indonesia');q.write_text(s,encoding='utf-8')
 exe='C:/Users/Administrator/AppData/Roaming/TinyTeX/bin/windows/pdflatex.exe'
 for run in range(3):
  result=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','-no-shell-escape','paper.tex'],
   cwd=OUT,capture_output=True,text=True,encoding='utf-8',errors='replace')
  (OUT/f'compile_pass_{run+1}.txt').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
  if result.returncode:raise RuntimeError('LaTeX compilation failed; inspect '+str(OUT/f'compile_pass_{run+1}.txt'))
 pdf=OUT/'Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio.pdf'
 shutil.copy2(OUT/'paper.pdf',pdf)
 after={str(p.relative_to(ROOT)):sha(p) for p in inputs};assert before==after
 doc=fitz.open(pdf);text='\n'.join(page.get_text() for page in doc)
 assert '2011Q1' in text and '2026Q1' in text and 'Indonesia' in text
 assert '??' not in text and 'TODO' not in text
 log=(OUT/'paper.log').read_text('utf-8',errors='replace')
 overflow=[v for v in log.splitlines() if 'Overfull' in v]
 warnings=[v for v in log.splitlines() if 'undefined' in v.lower() or 'LaTeX Error' in v]
 outside=[]
 for i,page in enumerate(doc,1):
  for block in page.get_text('dict')['blocks']:
   if 'lines' not in block:continue
   x0,y0,x1,y1=block['bbox']
   if x0<15 or x1>page.rect.width-15 or y0<12 or y1>page.rect.height-12:outside.append({'page':i,'bbox':[x0,y0,x1,y1]})
 previews=OUT/'previews';previews.mkdir(exist_ok=True)
 for i,page in enumerate(doc):
  pix=page.get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False);pix.save(previews/f'page_{i+1:03d}.png')
 try:font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)
 except OSError:font=ImageFont.load_default()
 for start in range(0,len(doc),12):
  sheet=Image.new('RGB',(4*225+20,3*340+15),'#EDEDED');draw=ImageDraw.Draw(sheet)
  for k,i in enumerate(range(start,min(start+12,len(doc)))):
   with Image.open(previews/f'page_{i+1:03d}.png') as im:
    im.thumbnail((210,300));thumb=im.copy().convert('RGB')
   x=15+(k%4)*225;y=10+(k//4)*340
   sheet.paste(thumb,(x,y));draw.text((x+3,y+307),str(i+1),fill='#4E3B30',font=font)
  sheet.save(OUT/f'contact_{start//12+1:02d}.png')
 (OUT/'paper_text.txt').write_text(text,encoding='utf-8')
 ALL.to_csv(A/'all_516_models_source.csv',index=False)
 report={'status':'PASS' if not overflow and not warnings and not outside else 'REVIEW_REQUIRED',
  'pdf':pdf.name,'pages':len(doc),'estimated_text_words':len(text.split()),'figures':len(re.findall(r'\\newlabel\{fig:',(OUT/'paper.aux').read_text('utf-8'))),'figure_assets_generated':len(list(A.glob('*.pdf'))),
  'primary_models_reported':176,'sensitivity_models_reported':340,
  'all_516_estimates_in_appendix':True,'reestimated_models':False,'reporter':'Indonesia',
  'goods_scope':'Seven HS6-based categories; not individual-code regressions',
  'latex_equations':True,'input_files_unchanged':before==after,'input_sha256':before,
  'pdf_sha256':sha(pdf),'overfull_boxes':overflow,'undefined_reference_or_error_warnings':warnings,'text_outside_page_margin':outside,
  'source_files':['paper.tex','numbers.tex','sections/','tables/','script/12_build_research_paper.py'],
  'references_verified':'Primary publisher metadata and official UNSD/Stata; user-supplied paper and local classification source',
  'inference':'Nominal post-AIC; conditional associations; visual J classification exploratory'}
 (OUT/'paper_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
 (OUT/'README.md').write_text("""# Naskah penelitian elaboratif

Mulai dari Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio.pdf. Ini naskah kerja berbasis hasil Stata run 17 November 2026, bukan artikel jurnal yang telah melalui peer review.

paper.tex, sections/, numbers.tex dan tables/ adalah sumber LaTeX yang dapat diedit. assets/ memuat grafik PDF vector, PNG dan data tabel. Lampiran mempertahankan 176 model utama dan 340 sensitivitas. Semua perdagangan adalah milik Indonesia; model barang adalah tujuh kategori hasil klasifikasi HS-6.

Reproduksi: jalankan script/12_build_research_paper.py dengan paket Python proyek dan pdfLaTeX lokal. Pertahankan sumber paper.tex serta sections/ di folder ini. Generator menarik angka dari keluaran Stata tanpa mengestimasi ulang model. paper_validation.json mencatat checksum, kelengkapan dan pemeriksaan tata letak.

Untuk belajar: mulai dengan definisi rasio dan orientasi kurs; baca hasil agregat, uraian tiap mitra dan kelompok; lalu bandingkan pola titik dengan diagnostik serta sensitivitas. Seluruh respons 516 model juga tersedia dalam PPT lengkap.
""",encoding='utf-8')
 print(json.dumps({k:report[k] for k in ['status','pdf','pages','estimated_text_words','figures','input_files_unchanged','overfull_boxes','undefined_reference_or_error_warnings']},indent=2),flush=True)
 doc.close()
if __name__=='__main__':build()
