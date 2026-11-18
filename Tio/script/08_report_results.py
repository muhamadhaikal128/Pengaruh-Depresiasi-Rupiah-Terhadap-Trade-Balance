"""Report the current HS6 rebuild, using the independently checked ECM engine."""
from pathlib import Path
import importlib.util,json,hashlib,os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font,PatternFill
ROOT=Path(__file__).resolve().parents[1]
T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee'
def md(df):
 def cell(v):return '' if pd.isna(v) else str(v).replace('|','/')
 return '| '+' | '.join(df.columns)+' |\n|'+'|'.join(['---']*len(df.columns))+'|\n'+'\n'.join('| '+' | '.join(cell(v) for v in r)+' |' for r in df.itertuples(index=False,name=None))
def main():
 path=ROOT/'script/python/09_report_engine.py'
 spec=importlib.util.spec_from_file_location('engine',path);engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
 if os.environ.get('OSKOOEE_REPORT_ONLY')!='1':engine.main()
 else:assert json.loads((D/'analysis_validation_report.json').read_text('utf-8'))['status']=='PASS'
 # Current trade series replaces the old GEM world series; do not carry its discrepancy label.
 world_data=pd.read_csv(ROOT/'intermediate/Trade_Total_Quarter.csv')
 world_data=world_data[world_data.ISO3.eq('WLD')].copy()
 tradecols=['Exports_USDk','Imports_USDk','Trade_Balance_USDk','Ln_Imports_Exports']
 desc=world_data[tradecols].describe().T.reset_index(names='Variable')
 desc.to_csv(T/'descriptive_world.csv',index=False,float_format='%.12g')
 display=desc.copy()
 for col in display.columns[1:]:display[col]=display[col].map(lambda v:'' if pd.isna(v) else f'{v:,.3f}')
 engine.table_image(display,'Indonesia-World | quarterly descriptive statistics','00_descriptive_world',
  'Trade in USD thousand; log ratio dimensionless. Available complete quarters, before macro-variable sample restrictions.',fontsize=8)
 fig,ax=engine.plt.subplots(figsize=(11,4.5))
 import numpy as np
 x=np.arange(len(world_data))
 ax.plot(x,world_data.Trade_Balance_USDk/1e6,color='#1b4f72')
 ax.axhline(0,color='gray',lw=.8)
 ax.axvspan(0,15,color='#e5ab62',alpha=.25,label='2006-2009: extended-sample sensitivity')
 ticks=np.arange(0,len(world_data),8)
 ax.set_xticks(ticks,world_data.Quarter.iloc[ticks],rotation=30)
 ax.set(ylabel='USD billion',title='Indonesia-World | exports minus imports')
 ax.legend()
 fig.savefig(ROOT/'output/figures/oskooee/world_net_trade_balance.png',dpi=200,bbox_inches='tight')
 fig.savefig(ROOT/'output/figures/oskooee/world_net_trade_balance.pdf',bbox_inches='tight');engine.plt.close(fig)
 s=pd.read_csv(T/'results_primary_models.csv');a=pd.read_csv(T/'results_all_models.csv')
 groups=pd.read_csv(ROOT/'intermediate/Goods_Groups.csv');order={k:i+1 for i,k in enumerate(groups.Group)}
 labels=groups.set_index('Group').Label.to_dict()
 cols=['model_id','ISO3','Group','label','estimator','N','Estimation_Start','Estimation_End','lag_order',
   'lr_q_b','lr_q_p','lr_pos_b','lr_pos_p','lr_neg_b','lr_neg_p','Dep_LR_p_BH','lr_asym_p',
   'Bounds5','Levels_supported5','Diagnostic_Flags']
 compact=s[cols];compact.to_csv(T/'primary_compact.csv',index=False,float_format='%.10g')
 forest=s[s.scope.eq('goods')].copy()
 forest['Order']=forest.Group.map(order);forest['Label']=forest.Group.map(labels)
 for dest,ardl,nardl in [('Estimate','lr_q_b','lr_neg_b'),('Lo95','lr_q_lo95','lr_neg_lo95'),('Hi95','lr_q_hi95','lr_neg_hi95')]:
  forest[dest]=forest[ardl].where(forest.estimator.eq('ARDL'),forest[nardl])
 forest['Supported']=forest.Levels_supported5.astype(int);forest['Clean']=forest.Diagnostic_clean5.astype(int)
 forest[['model_id','ISO3','Group','Label','Order','estimator','Estimate','Lo95','Hi95','Supported','Clean']].to_csv(T/'Forest_Goods_Data.csv',index=False,float_format='%.12g')
 # Render the same seven-group coefficient data used by the native Stata GPH.
 from matplotlib.lines import Line2D
 for (iso,est),frame in forest.groupby(['ISO3','estimator']):
  frame=frame.sort_values('Order');fig,ax=engine.plt.subplots(figsize=(11,6.3))
  for i,row in enumerate(frame.itertuples()):
   color='#A5644E' if row.Supported and row.Clean else '#C17529' if row.Supported else '#777777'
   ax.plot([row.Lo95,row.Hi95],[i,i],color=color,lw=1.8)
   ax.scatter([row.Estimate],[i],s=55,edgecolor=color,facecolor=color if row.Supported else 'white',zorder=3)
  ax.axvline(0,color='#B23B2E',lw=1);ax.set_yticks(range(len(frame)),frame.Label);ax.invert_yaxis()
  ax.set_title('Efek jangka panjang per kelompok: '+('Indonesia–dunia' if iso=='WLD' else iso)+' | '+est,fontweight='bold')
  ax.set_xlabel('Koefisien '+('NEG' if est=='NARDL' else 'q')+' jangka panjang; CI nominal 95%')
  ax.grid(axis='x',color='#E5DFDA',lw=.6);ax.set_axisbelow(True)
  handles=[Line2D([],[],marker='o',linestyle='None',color='#A5644E',label='Levels + diagnostik'),
   Line2D([],[],marker='o',linestyle='None',color='#C17529',label='Levels; caveat diagnostik'),
   Line2D([],[],marker='o',linestyle='None',color='#777777',markerfacecolor='white',label='Levels belum didukung')]
  fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.57,.08),ncol=3,frameon=False,fontsize=8)
  fig.text(.03,.015,'y = ln(M/X); q naik = apresiasi. Koefisien positif: arah perbaikan saat depresiasi.\nKelompok bertumpang tindih. Tanpa dukungan levels, koefisien belum menjadi hubungan LR yang mapan.',fontsize=9)
  fig.subplots_adjust(left=.34,right=.98,top=.90,bottom=.23)
  prefix=ROOT/'output/figures/oskooee'/f'forest_{iso}_{est}_goods'
  fig.savefig(str(prefix)+'.png',dpi=220,bbox_inches='tight');fig.savefig(str(prefix)+'.pdf',bbox_inches='tight');engine.plt.close(fig)
 wb=load_workbook(T/'Oskooee_Results.xlsx')
 for name in ['Readme','Primary_compact','Goods_groups','Descriptive_world']:
  if name in wb:del wb[name]
 for name,frame in [('Primary_compact',compact),('Goods_groups',groups),('Descriptive_world',desc)]:
  ws=wb.create_sheet(name,0)
  for row in dataframe_to_rows(frame.astype(object).where(pd.notna(frame),None),index=False,header=True):ws.append(row)
  ws.freeze_panes='C2';ws.auto_filter.ref=ws.dimensions
  for c in ws[1]:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='A5644E')
 rd=wb.create_sheet('Readme',0)
 for line in [f'HS6 rebuild: {len(s)} primary and {len(a)-len(s)} sensitivity estimates, computed in Stata.',
  'Trade Map source: 22 workbooks, monthly Jan2006-Aug2026; all product totals plus seven overlapping goods groups.',
  'Outcome ln(M/X), q up=appreciation; NEG is a negative cumulative depreciation change.',
  'Goods models cover World and each of the ten partners. World foreign demand is a fixed-weight top10 GDP proxy.',
  'Groups are not a mutually exclusive partition. BEC consumption/intermediate/capital overlap commodity categories.',
  'HS revisions are not declared in the workbook; conservative code-level consensus across official correlations is used.',
  'Ambiguous/unclassified commodity and BEC codes are retained and audited, not forced into a binary category.',
  'Import-input dependency/TiVA mechanism is excluded. Intermediate goods classification does not measure imported content.',
  'Levels support, diagnostics and sample coverage must be checked before interpreting LR coefficients.',
  'Post-AIC p-values/intervals are nominal; exploratory BH is within scope-estimator. Overlapping groups are not independent.',
  'Official Stata CUSUM paths are used. Two AUS NARDL initial matrices are singular; independent initialization differs and these models carry a diagnostic caveat.',
  'Previous work is archived in archive/v1_20261117_before_hs6_rebuild/.']:rd.append([line])
 rd.column_dimensions['A'].width=130;wb.save(T/'Oskooee_Results.xlsx');wb.close()
 overview=s.groupby(['scope','estimator']).agg(Models=('model_id','size'),Levels_supported5=('Levels_supported5','sum'),Diagnostics_clean5=('Diagnostic_clean5','sum')).reset_index()
 world=s[s.scope.eq('aggregate')][['estimator','N','lag_order','lr_q_b','lr_pos_b','lr_neg_b','lr_asym_p','Bounds5','Diagnostic_Flags']].copy()
 for c in ['lr_q_b','lr_pos_b','lr_neg_b','lr_asym_p']:world[c]=world[c].map(lambda v:'' if pd.isna(v) else f'{v:.4f}')
 good=s[s.Levels_supported5&s.Diagnostic_clean5][['model_id','N','lr_q_b','lr_neg_b','Dep_LR_p','Dep_LR_p_BH']].copy()
 for c in ['lr_q_b','lr_neg_b','Dep_LR_p','Dep_LR_p_BH']:good[c]=good[c].map(lambda v:'' if pd.isna(v) else f'{v:.4f}')
 val=json.loads((D/'analysis_validation_report.json').read_text('utf-8'))
 text=f'''# Hasil penelitian HS-6: ARDL dan NARDL

Run17November2026. Estimasi dilakukan di Stata; data mentah tidak diedit. Pekerjaan sebelumnya diarsipkan ke `archive/v1_20261117_before_hs6_rebuild/`. Kanal dependensi ekspor terhadap input impor/TiVA dikeluarkan dari run ini.

## Mulai membaca

- [Workbook lengkap](../output/tables/oskooee/Oskooee_Results.xlsx), [ringkasan CSV](../output/tables/oskooee/primary_compact.csv).
- [Master do-file](../script/00_master.do); estimator dibagi menjadi 03 agregat, 04 mitra, 05 kelompok, 06 unit root, dan 07 ekspor. Residual, bounds dan CUSUM berada dalam ardl_helpers.do.
- [Registry sampel](../output/diagnostics/oskooee/case_registry.csv), [diagnostik lengkap](../output/diagnostics/oskooee/diagnostic_summary.csv).
- Tabel koefisien setiap model utama tersedia sebagaiPNG/PDF di output/tables/oskooee/. Grafik dinamis, residual dan stabilitas ada di output/figures/oskooee/; versiStata editable di output/gph/oskooee/.

**{len(s)} model utama dan {len(a)-len(s)} sensitivitas telah diestimasi**, total{len(a)}. Model utama: satu agregat dunia, sepuluh bilateral, serta tujuh kelompok untuk dunia dan masing-masing sepuluh mitra; masing-masing ARDL dan NARDL.

## Data dan klasifikasi

Nilai perdagangan bersumber dari22workbookTradeMapHS-6 pengguna, Januari2006–Agustus2026, satuanUSD ribu. Kuartal mensyaratkan tiga bulan lengkap. KolomTOTAL dipakai untuk agregat/bilateral; kelompok dibentuk dariHS-6. Selisih penjumlahan produk terhadapTOTAL dievaluasi terhadap batas pembulatan perbaris, tidak dipaksa nol.

Tujuh kelompok:

{md(groups)}

Manufaktur nonkomoditas dan kelompok komoditas mengikuti UNCTAD A11 berbasis SITC3. Pertanian/pangan mencakup pangan, minuman, tembakau, minyak nabati serta bahan mentah pertanian; energi/tambang mencakup bahan bakar, mineral/bijih, logam nonferrous dan kategori komoditas mineral terkait padaA11. Barang konsumsi, intermediate dan modal mengikuti dimensi penggunaanSNA padaBEC5. **Kelompok saling tumpang tindih dan tidak boleh dijumlahkan sebagai pangsa total.** Barang modal termasuk ternak pembiakan atau produk investasi lain bilaBEC mengklasifikasikannya demikian; bukan hanya mesin.

Workbook tidak menyatakan revisiHS yang digunakan untuk setiap sel. Karena kode lama dan baru muncul dalam satu daftar, klasifikasi utama memakai konsensus konservatif perHS-6 di antara revisi yang relevan pada korespondensiUNSD. Kode yang berubah kelas atau bercampur tetapmixed/unclassified. Ini lebih rinci daripadaHS-4, tetapi bukan klaim semua masalah revisi waktu sudah selesai. Lihat output/diagnostics/data/Classification_Coverage.csv. KlasifikasiBEC tidak menunjukkan kandungan input impor eksportir.

## Metode dan interpretasi

Adaptasi Bahmani-Oskooee & Fariditavana, DOI10.1007/s11079-015-9369-5. Outcome **y=ln(M/X)**, bukanln(X−M) dan bukan persamaan ekspor tersendiri. X−M tetap dipakai untuk statistik deskriptif. qnaik=apresiasi; untuk bilateral tanda logRER dibalik. NARDL memisahkan POS dan NEG. NEG merupakan akumulasi perubahan negatif; koefisienNEG positif menunjukkan arah perbaikan neraca ketika depresiasi.

AIC maksimum4laglevels, cap2sebagai sensitivitas; intercept tanpa tren, ECMt−1. World baseline mulai2010 untuk mempertahankan pembandingan dengan run sebelumnya;2006+ sebagai sensitivitas. GDP dalam logindekslevelriil, bukan pertumbuhan. Permintaan dunia adalah proksiPDB10mitra berbobot ekspor2006–2008 yang dihitung ulang dari workbook baru, bukan PDBglobal.

Bounds finite-sample menggunakan F dan t; levels_supported5 juga memeriksa joint-X, akar dinamis, risikoI(2) serta minimal 15 derajat bebas residual. ADF/PP memeriksa level dan firstdifference. Diagnostik meliputi BG, BP, RESET, JB, ARCH, CUSUM dan CUSUMSQ. CUSUMSQ menggunakan band simultan referensiGaussian19.999simulasi, seedtetap, aproksimasi. Pemeriksaan prediksi OLS independen dan ekuivalensi ECM–levels dilakukan untuk setiap model.

P-value/CI nominal setelah pemilihanAIC. BH merupakan koreksi eksploratif dalam keluarga scope-estimator; bukan koreksi seleksi lag. Model kelompok bertumpang tindih, sehingga tidak menjadi bukti independen. Signifikan pada satu kelompok dan tidak signifikan pada kelompok lain bukan uji beda koefisien.

## Ringkasan hasil

Untuk agregat dunia, ARDL dan NARDL utama belum memenuhi syarat hubungan level pada taraf 5%. Karena itu, tanda atau signifikansi koefisien LR saja belum menjadi kesimpulan jangka panjang.

Pada NARDL bilateral, Australia dan Malaysia lolos penyaringan hubungan level serta diagnostik utama dan mempunyai koefisien NEG positif. Hubungan ini mengarah pada perbaikan neraca saat depresiasi, dengan syarat model yang digunakan. Signifikansi nominal tetap perlu dibaca bersama kolom BH dan hasil sensitivitas; bukan bukti kausal.

Pada tujuh kelompok dunia, tidak ada NARDL yang sekaligus lolos syarat level dan seluruh penyaringan diagnostik. Kelompok konsumsi dan energi/tambang mempunyai dukungan level, tetapi juga catatan diagnostik. Hasil ini belum cukup untuk menyimpulkan bahwa komoditas secara umum tidak sensitif terhadap kurs.

Pada ARDL linier dunia, komoditas total (q = -1,3546) dan energi/tambang (q = -2,0399) lolos penyaringan level serta diagnostik dan mempunyai koefisien q negatif. Dengan q naik berarti apresiasi, tanda ini mengarah pada memburuknya rasio neraca saat depresiasi. Arah negatif bertahan pada cap dua dan kontrol BCOM, tetapi beberapa sensitivitas mempunyai masalah diagnostik. Pada NARDL, koefisien NEG terkait belum signifikan secara nominal dan dukungan model berubah menurut lag. Temuan ini bergantung pada spesifikasi, bukan bukti kausal yang sudah mapan.

Koefisien tidak signifikan tidak membuktikan efek nol. Perbedaan signifikansi antara manufaktur dan komoditas juga bukan uji langsung perbedaan sensitivitas kedua kelompok. Model di sini menguji rasio impor/ekspor, sehingga tidak memisahkan respons ekspor dari respons impor.

{md(overview)}

F/tbounds5% menolak no-levelrelation pada **{val['primary_bounds5_rejections']}/{len(s)}** model; **{val['primary_levels_supported5']}/{len(s)}** lolos syarat tambahan levels; **{val['primary_levels_and_diagnostics_supported5']}/{len(s)}** juga tidak ditolak dalam flag diagnostik gabungan. Ini penyaringan, bukan sertifikat kebenaran atau identifikasi kausal.

### Indonesia–dunia

{md(world)}

### Model dengan dukungan levels dan flag diagnostik lebih mendukung

{md(good)}

Seluruh model tetap dilaporkan, termasuk yang tidak mendukung kointegrasi atau mempunyai masalah diagnostik. Grafik LR untuk model tanpa dukungan levels tidak boleh dipakai sebagai kesimpulan LR yang mapan. Grafik respons tidak otomatis membuktikanJ-curve.

## Batas data yang tetap berlaku

- India baselineCPI mulai2013;WPI hanya sensitivitas terpisah. CPI Australia bulanan berasal dari interpolasi penyedia.
- ASCPI Oktober2025 dan VietnamFX Agustus2025 kosong. Sampel mengikuti rentang lengkap terpanjang; celah tidak dirapatkan.
- GDP sebagian mitra berakhir2026Q1; proksi permintaan dunia mengikuti batas tersebut. Perbedaan window memengaruhi perbandingan antarmitra.
- HistorisGDP Indonesia/India/Vietnam dan konsepFX Thailand/Vietnam mempunyai catatan vintage/sumber. Data Trade Map baru belum direkonsiliasi penuh dengan seri nasional independen; rekonsiliasi HS6 terhadap TOTAL adalah pemeriksaan internal.
- HargaBCOM merupakan kontrol sensitivitas, bukan identifikasi kausal pengaruh harga global.
- File baru berisi nilai perdagangan; run ini tidak menguji eksporvolume atau dependensi inputimpor.
- Referensi audit lama dipertahankan di input/reference/ dan seluruh keluaran sebelumnya ada diarchive/.

## Pemeriksaan CUSUM

Kurva CUSUM utama diekspor langsung melalui opsi generate() pada estat sbcusum, dari UECM dengan lag dan sampel terpilih. Maksimum kurva harus mereproduksi statistik Stata untuk seluruh 176 model utama. [Dokumentasi resmi Stata](https://www.stata.com/manuals/tsestatsbcusum.pdf).

Matriks awal TYPE_AUS_capital_NARDL_AIC4 dan TYPE_AUS_consumption_NARDL_AIC4 belum full rank. Perhitungan independen Python menunda inisialisasi sampai full rank sehingga statistiknya berbeda. Kurva resmi Stata dipertahankan, perbedaan dicatat dalam CUSUM_cross_implementation_check.csv, dan kedua model diberi caveat serta tidak diberi label diagnostik bersih. Pada model dengan matriks awal full rank, kesesuaian independen tetap diwajibkan dengan toleransi numerik.

Run neraca perdagangan ini tidak dengan sendirinya membuktikan hipotesis tentang ekspor saja. Seluruh hasil merupakan asosiasi kondisional; belum mengidentifikasi efek kausal depresiasi.

## Reproduksi

`script/00_run.ps1` menjalankan 01_build_panel.py -> 00_master.do (Stata) -> 06_cusum_paths.do -> 08_report_results.py -> 07_export.do graphs -> 09_validate_results.py. Do-file Stata utama berada langsung di script/; helper Python berada di script/python/. Raw workbook dipertahankan identik dengan file pengguna.
'''
 for old,new in [('Run17November2026','Run 17 November 2026'),('total{','total {'),('total'+str(len(a)),'total '+str(len(a))),('sebagaiPNG','sebagai PNG'),('versiStata','versi Stata'),('22workbookTradeMapHS-6','22 workbook Trade Map HS-6'),('Januari2006','Januari 2006'),('satuanUSD','satuan USD'),('kolomTOTAL','kolom TOTAL'),('KolomTOTAL','Kolom TOTAL'),('dariHS-6','dari HS-6'),('terhadapTOTAL','terhadap TOTAL'),('mengikutiUNCTADA11 berbasisSITC3','mengikuti UNCTAD A11 berbasis SITC3'),('padaA11','pada A11'),('penggunaanSNA padaBEC5','penggunaan SNA pada BEC5'),('bilaBEC','bila BEC'),('revisiHS','revisi HS'),('perHS-6','per HS-6'),('korespondensiUNSD','korespondensi UNSD'),('tetapmixed','tetap mixed'),('daripadaHS-4','daripada HS-4'),('KlasifikasiBEC','Klasifikasi BEC'),('DOI10.','DOI 10.'),('bukanln','bukan ln'),('qnaik','q naik'),('logRER','log RER'),('koefisienNEG','koefisien NEG'),('maksimum4laglevels','maksimum 4 lag levels'),('cap2sebagai','cap 2 sebagai'),('ECMt−1','ECM t−1'),('mulai2010','mulai 2010'),(';2006+','; 2006+'),('logindekslevelriil','log indeks level riil'),('proksiPDB10mitra','proksi PDB 10 mitra'),('ekspor2006','ekspor 2006'),('PDBglobal','PDB global'),('risikoI(2)','risiko I(2)'),('firstdifference','first difference'),('referensiGaussian19.999simulasi','referensi Gaussian 19.999 simulasi'),('seedtetap','seed tetap'),('pemilihanAIC','pemilihan AIC'),('F/tbounds5%','F/t bounds 5%'),('no-levelrelation','no-level relation'),('membuktikanJ-curve','membuktikan J-curve'),('baselineCPI','baseline CPI'),('mulai2013;WPI','mulai 2013; WPI'),('ASCPI Oktober2025','AS CPI Oktober 2025'),('VietnamFX Agustus2025','Vietnam FX Agustus 2025'),('berakhir2026Q1','berakhir 2026Q1'),('HistorisGDP','Historis GDP'),('konsepFX','konsep FX'),('dunia2006','dunia 2006'),('denganWDI','dengan WDI'),('HargaBCOM','Harga BCOM'),('eksporvolume','ekspor volume'),('inputimpor','input impor'),('diarchive/','di archive/'),('KodeStata','Kode Stata'),('kodeStata','kode Stata'),('helperPython','helper Python'),('Rawworkbook','Raw workbook')]:text=text.replace(old,new)
 for old,new in [('dari22', 'dari 22'), ('Agustus2026', 'Agustus 2026'), ('perbaris', 'per baris'), ('maxlag', 'maxlag'), ('minimal15', 'minimal 15')]:text=text.replace(old,new)
 (ROOT/'notes/hasil_ardl_nardl_hs6.md').write_text(text,encoding='utf-8')
 (T/'README.md').write_text('# Hasil run HS-6\n\nMulai dari Oskooee_Results.xlsx atau primary_compact.csv. Semua koefisien model utama tersedia PNG/PDF; diagnostik dan p-value nominal setelah seleksi AIC tetap harus diperhatikan. Tujuh kelompok bukan partisi eksklusif.\n',encoding='utf-8')
 print('HS6_REPORT_COMPLETE',len(s),len(a),flush=True)
if __name__=='__main__':main()
