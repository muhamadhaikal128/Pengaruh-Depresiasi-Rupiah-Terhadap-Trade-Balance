"""Finalize the human-readable report, artifact indexes and delivery checks."""
from pathlib import Path
import hashlib,json,platform
import pandas as pd
from PIL import Image
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
ROOT=Path(__file__).resolve().parents[1]
T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee';F=ROOT/'output/figures/oskooee';G=ROOT/'output/gph/oskooee'

def md(df):
    def cell(x):return '' if pd.isna(x) else str(x).replace('|','/')
    return '| '+' | '.join(map(str,df.columns))+' |\n|'+ '|'.join(['---']*len(df.columns))+'|\n'+'\n'.join('| '+' | '.join(cell(x) for x in row)+' |' for row in df.itertuples(index=False,name=None))

def main():
    s=pd.read_csv(T/'results_primary_models.csv');allm=pd.read_csv(T/'results_all_models.csv')
    reg=pd.read_csv(D/'case_registry.csv');u=pd.read_csv(D/'HS4_estimation_eligibility.csv',dtype={'HS_Code':str})
    vr=json.loads((D/'analysis_validation_report.json').read_text('utf-8'))
    assert len(s)==62 and len(allm)==174 and vr['status']=='PASS'
    required=[]
    for model in s.model_id:
        required.extend([T/(model+'_coefficients.png'),F/(model+'_multipliers.png'),F/(model+'_stability.png'),F/(model+'_residuals.png'),
                         G/(model+'_cusum.gph'),G/(model+'_multipliers.gph'),G/(model+'_cusumsq.gph'),G/(model+'_residuals.gph')])
    for p in required:assert p.is_file() and p.stat().st_size>0,p
    for p in list(T.glob('*.png'))+list(F.glob('*.png')):
        with Image.open(p) as im:im.verify()
    cols=['model_id','estimator','N','Estimation_Start','Estimation_End','lag_order','lr_q_b','lr_q_p','lr_pos_b','lr_pos_p','lr_neg_b','lr_neg_p','Dep_LR_p_BH','lr_asym_p','Bounds5','Levels_supported5','Diagnostic_Flags']
    compact=s[cols];compact.to_csv(T/'primary_compact.csv',index=False,float_format='%.8g')
    wb=load_workbook(T/'Oskooee_Results.xlsx')
    for name in ['Readme','Primary_compact']:
        if name in wb:del wb[name]
    ws=wb.create_sheet('Primary_compact',0)
    for row in dataframe_to_rows(compact.astype(object).where(pd.notna(compact),None),index=False,header=True):ws.append(row)
    ws.freeze_panes='C2';ws.auto_filter.ref=ws.dimensions
    rd=wb.create_sheet('Readme',0)
    for line in ['ARDL and NARDL adaptation of Bahmani-Oskooee & Fariditavana, DOI 10.1007/s11079-015-9369-5.',
                 'Outcome y=ln(imports/exports). q up=appreciation. NEG is depreciation. Negative response of y means improvement.',
                 'Primary: 62 baseline estimates. All_models: 174 including lag/source/price sensitivities.',
                 'Bounds5 and Levels_supported5 must be reviewed before interpreting long-run coefficients.',
                 'Classical OLS post-AIC p-values are nominal. Diagnostic flags and source caveats remain material.',
                 'Foreign demand for world model is a top10 fixed-weight proxy, not observed global GDP.',
                 'HS4 individual series were screened, not all estimated. Import-input hypothesis is ON HOLD.',
                 'Read Tio/notes/hasil_ardl_nardl_oskooee.md and output/diagnostics/oskooee/diagnostic_summary.csv.']:rd.append([line])
    rd.column_dimensions['A'].width=120;wb.save(T/'Oskooee_Results.xlsx');wb.close()
    w=s[s.scope.eq('aggregate')]
    good=s[s.Levels_supported5&s.Diagnostic_clean5]
    worldtable=w[['estimator','N','lag_order','lr_q_b','lr_pos_b','lr_neg_b','lr_asym_p','Bounds5','Diagnostic_Flags']].copy()
    for c in ['lr_q_b','lr_pos_b','lr_neg_b','lr_asym_p']:worldtable[c]=worldtable[c].map(lambda x:'' if pd.isna(x) else f'{x:.4f}')
    goodtable=good[['model_id','N','lr_q_b','lr_neg_b','Dep_LR_p','Dep_LR_p_BH']].copy()
    for c in ['lr_q_b','lr_neg_b','Dep_LR_p','Dep_LR_p_BH']:goodtable[c]=goodtable[c].map(lambda x:'' if pd.isna(x) else f'{x:.4f}')
    flagcounts={c:int(s[c].lt(.05).sum()) for c in ['bg4_p','hetero_p','reset_p','JB_p','ARCH4_p','CUSUMSQ_p_MC']}
    overview=s.groupby(['scope','estimator']).agg(Models=('model_id','size'),Levels_supported5=('Levels_supported5','sum'),Diagnostics_clean5=('Diagnostic_clean5','sum')).reset_index()
    report=f'''# Hasil ARDL/NARDL: Indonesia, mitra dagang, dan jenis barang

Tanggal run: 17 November 2026. Analisis dikerjakan di Tio; file mentah dan folder Haikal tidak diubah. Hipotesis dependensi input impor/TiVA **ditangguhkan** sesuai instruksi.

## Hasil utama dan tempat mulai membaca

**174 model telah diestimasi di Stata: 62 utama dan 112 sensitivitas.** Pemeriksaan ekuivalensi ECM-levels dan prediksi OLS independen lulus untuk seluruh model. Lulus pemeriksaan komputasi bukan berarti semua model mendukung kointegrasi atau bebas masalah diagnostik.

- [Workbook hasil lengkap](../output/tables/oskooee/Oskooee_Results.xlsx): Readme, ringkasan pendek, semua koefisien, diagnostik dan sampel.
- [Gambar tabel agregat dunia](../output/tables/oskooee/01_world_results_1.png).
- [Gambar tabel sepuluh mitra, halaman 1](../output/tables/oskooee/02_partner_results_1.png).
- [Gambar tabel jenis barang, halaman 1](../output/tables/oskooee/03_goods_results_1.png).
- [Grafik respons dinamis agregat NARDL](../output/figures/oskooee/WORLD_NARDL_AIC4_multipliers.png).
- [Grafik selisih ekspor-impor Indonesia-dunia](../output/figures/oskooee/world_net_trade_balance.png).
- [Ringkasan diagnostik semua model](../output/diagnostics/oskooee/diagnostic_summary.csv).
- [Master do-file](../script/00_master.do) dan [do-file estimasi lengkap](../script/13_run_oskooee_models.do).

## 1. Cakupan

Model utama terdiri atas satu seri Indonesia-dunia, sepuluh seri bilateral, dan dua kelompok jenis barang (komoditas/nonkomoditas) untuk masing-masing sepuluh mitra. Setiap seri diestimasi secara linear ARDL dan nonlinear NARDL: 31 seri x 2 model = 62.

Jenis barang memakai klasifikasi konservatif UNCTAD A11 yang sebelumnya dibangun. Heading mixed dan unclassified tetap disimpan dalam dataset sumber tetapi tidak dipaksa ke salah satu kelompok. Model jenis barang ini **mencakup sepuluh mitra, bukan seluruh dunia**; perdagangan HS dunia belum tersedia untuk membangun kelompok dunia yang setara.

Hasil penyaringan HS4 individual: {int(u.PreEstimation_Eligible.sum()):,} dari {len(u):,} seri HS4-mitra mempunyai minimal 48 kuartal lengkap berurutan dan kelas biner yang jelas. Daftar [kelayakan awal](../output/diagnostics/oskooee/HS4_estimation_eligibility.csv) belum berarti seluruh seri tersebut sudah diestimasi/lolos unit-root dan diagnostik. Run ini memusatkan estimasi pada kelompok jenis barang.

## 2. Paper, persamaan, dan arah tanda

Referensi: Bahmani-Oskooee & Fariditavana, *Nonlinear ARDL Approach and the J-Curve Phenomenon*, online 2015, Open Economies Review 27 (2016), 51-70; DOI [10.1007/s11079-015-9369-5](https://doi.org/10.1007/s11079-015-9369-5). PDF pengguna disalin ke input/reference/oskooee_replication/ dan dibaca langsung.

Paper menggunakan **ln(M/X)**, bukan log selisih ekspor-impor. Karena selisih X-M dapat negatif, outcome paper tidak diganti diam-diam dengan ln(X-M). Nilai X-M tetap tersedia dan digambarkan sebagai neraca perdagangan nominal.

Model jangka panjang dasar:

```text
y_t = a + b_d ln(GDP_IDN)_t + b_f ln(GDP_mitra)_t + b_q ln(REX)_t + u_t
y_t = ln(M_t / X_t)
```

Untuk menyesuaikan konvensi paper, **REX naik berarti apresiasi**. Kurs riil bilateral pada data semula naik berarti depresiasi, sehingga log-nya dibalik tanda. REER BIS agregat sudah naik berarti apresiasi. POS adalah jumlah perubahan log REX positif (apresiasi); NEG adalah jumlah perubahan negatif (depresiasi). NEG adalah nilai bertanda negatif, bukan besaran depresiasi positif.

NARDL mengganti ln(REX) dengan POS dan NEG dalam ECM. GDP Indonesia dan mitra tetap dalam log indeks level riil. Kedua model memakai intercept tanpa deterministic trend, dengan representasi ECM periode t-1 (`ec1`). Konstanta jangka panjang yang dinormalisasi ikut ditampilkan pada tabel gambar dan file koefisien tambahan.

**Interpretasi tanda:** koefisien LR NEG positif dikalikan perubahan NEG negatif menghasilkan penurunan ln(M/X), yakni perbaikan trade balance. Respons positif pada grafik y berarti perburukan, respons negatif berarti perbaikan. Wald LR menguji kesamaan koefisien POS dan NEG, bukan kesamaan koefisien dengan tanda berlawanan.

Model trade balance tidak mengidentifikasi perubahan ekspor secara terpisah: rasio dapat berubah karena impor, ekspor, atau keduanya. Hasilnya tidak boleh langsung disebut bukti kausal depresiasi menurunkan/meningkatkan ekspor.

## 3. Perbedaan yang dijelaskan dari paper

Paper memakai sekitar 171 kuartal dan maksimum delapan lag variabel first difference. Sampel kita jauh lebih pendek. Run utama memakai pencarian **AIC dengan maksimum empat lag ARDL levels** (maksimum tiga lag first difference dalam ECM), disertai sensitivitas maksimum dua lag. Ini adaptasi metode, bukan reproduksi persis batas lag dan periode paper. Pemilihan lag dilakukan pada sampel holdback maksimum yang sama untuk ARDL/NARDL di setiap batas lag; sensitivitas cap 2 dan cap 4 memiliki jumlah observasi efektif berbeda dan bukan kompetisi AIC lintas sampel.

Bounds test memakai critical values finite-sample Kripfganz-Schneider melalui paket ardl 1.0.6. Critical value mengikuti k, N dan banyaknya komponen short-run masing-masing model. Ringkasan keputusan 5% mempertimbangkan **F dan t bounds**, lalu pemeriksaan tambahan signifikansi bersama regressor X, stabilitas akar AR, risiko I(2), dan residual df. Statistik F-only 10% ala pembacaan historis paper tetap disimpan, tetapi tidak dijadikan pengganti pemeriksaan tersebut.

Secara khusus, koefisien ECM negatif dengan p-value t biasa tidak sendirian membuktikan kointegrasi bila bounds tidak mendukung. P-value dan interval LR adalah delta-method dan nominal sesudah seleksi AIC; tidak mengoreksi seluruh ketidakpastian pemilihan model. Kolom Dep_LR_p_BH menyediakan koreksi eksploratif Benjamini-Hochberg untuk koefisien depresiasi, per scope-estimator pada model utama. Itu bukan koreksi seleksi lag atau bukti kausal.

## 4. Sampel dan kendala sumber

- Agregat utama memakai window tersedia **2010Q1-2026Q1**, N estimasi 61 setelah holdback empat lag. Tahun 2006-2009 belum harmonis antar sumber impor dunia; seluruh periode 2006+ tetap diestimasi sebagai sensitivitas yang ditandai. Akhir window 2026Q1 berasal dari keterbatasan GDP sebagian mitra pada indeks permintaan asing.
- Permintaan asing dunia memakai **indeks GDP sepuluh mitra berbobot ekspor tetap 2006-2008**, bukan GDP seluruh dunia. REX agregat memakai REER, sehingga model dunia merupakan adaptasi proksi terhadap spesifikasi bilateral paper.
- India baseline CPI baru dimulai 2013Q1; data sebelum 2013 memakai WPI dan hanya masuk sensitivitas tersendiri. Model utama India tidak memperlakukan WPI sebagai CPI.
- CPI AS kosong pada Oktober 2025 dan kurs BIS Vietnam kosong Agustus 2025. Dipakai rentang lengkap terpanjang (AS sampai 2025Q3, Vietnam sampai 2025Q2), bukan menghapus celah kemudian merapatkan waktu.
- CPI Australia bulanan merupakan interpolasi oleh penyedia; data awal GDP Indonesia/India/Vietnam serta beda konsep kurs Thailand/Vietnam masih mempunyai catatan audit. Seri GEM penuh digunakan sebagai sensitivitas THA/VNM/KOR, bukan penambal satu bulan BIS.
- Window antarmitra berbeda. Perbedaan koefisien antarmitra tidak otomatis hanya berasal dari karakter ekonomi mitranya.
- Nol perdagangan HS4 tetap nol di sumber. Untuk ln(M/X), kuartal dengan salah satu arus nol tidak dipaksa mempunyai rasio log, dan tidak digunakan log(1+nilai) sebagai jalan pintas.

Lihat [audit validitas makro](audit_validitas_data_macro.md), [registry sampel](../output/diagnostics/oskooee/case_registry.csv), dan catatan klasifikasi HS4 untuk rincian.

## 5. Diagnostik dan validasi

- Unit-root: ADF dengan pemilihan lag BIC 0-4 pada sampel seleksi yang sama, PP bandwidth 4, level serta first difference; ADF level dengan trend memakai lag hasil seleksi intercept. POS/NEG juga diperiksa. Kegagalan kedua uji first difference menolak unit root pada 10% ditandai I(2) belum dapat disingkirkan, bukan dinyatakan pasti I(2). Tidak ada model utama yang mendapat flag tersebut pada run ini; daya uji sampel pendek tetap terbatas.
- Kointegrasi/levels: F dan t bounds finite-sample, joint-X test dan akar AR; keputusan lengkap tersimpan.
- Residual: BG lag 1/4, Breusch-Pagan/Cook-Weisberg, RESET satu fitted-squared term pada UECM, Jarque-Bera, dan ARCH lag 4.
- Stabilitas: CUSUM recursive resmi Stata. CUSUMSQ dihitung dari recursive forecast residuals dengan band simultan referensi Gaussian finite-sample, **19.999 simulasi** dan seed tetap. Ini diagnostik Monte Carlo aproksimasi, bukan klaim memakai tabel CUSUMSQ paper persis. Grafik Python dan .gph menyebut metode referensinya.
- Ekuivalensi: levels dan ECM diuji pada sampel identik; residual RSS sesuai toleransi relatif 1e-7 x max(1,RSS). Prediksi Stata diperiksa kembali menggunakan solusi least-squares Python. Semua 174 lolos dan tidak ada rank deficiency.
- Checksum dataset input tetap sama sesudah analisis.

Pada 62 model utama, penolakan diagnostik 5% adalah: BG4={flagcounts['bg4_p']}, heteroskedastisitas={flagcounts['hetero_p']}, RESET={flagcounts['reset_p']}, JB={flagcounts['JB_p']}, ARCH4={flagcounts['ARCH4_p']}, CUSUMSQ={flagcounts['CUSUMSQ_p_MC']}. Ini pengujian berulang yang dapat memberi false alarm; model tidak dihapus hanya agar terlihat bersih. Covariance OLS klasik tetap mengikuti run dasar; bila diagnostik ditolak, p-value biasa memerlukan kehati-hatian dan spesifikasi/robustness lanjutan.

**27/62** menolak no-level-relation melalui F/t bounds pada 5%; setelah syarat tambahan, **18/62** memperoleh flag levels supported. Hanya **7/62** sekaligus tidak ditolak pada seluruh diagnostik yang dicantumkan dalam flag gabungan. Flag tersebut adalah penyaringan transparan, bukan sertifikat model benar.

{md(overview)}

Kendala khusus: `PRICE_IND_commodity_NARDL_AIC4` memiliki 49 observasi dan 25 parameter. Paket bounds mensyaratkan minimal dua kali banyaknya parameter; critical value finite-sample tidak tersedia. Koefisien tetap dicatat, tetapi Bounds5=Unavailable dan tidak dipakai sebagai dukungan LR. Kegagalan ini ada pada model sensitivitas kontrol BCOM, bukan pada baseline India.

## 6. Membaca hasil awal

### Indonesia-dunia

{md(worldtable)}

Kedua baseline agregat **belum mendukung levels relationship pada 5%**. NARDL menunjukkan Wald asimetri nominal sekitar 0,007, tetapi koefisien jangka panjang belum layak dijadikan kesimpulan kuat karena bounds tidak mendukung; NARDL juga mendapat penolakan CUSUMSQ. ECT t biasa yang signifikan tidak menghapus keterbatasan ini.

### Mitra dan jenis barang

Hasil dengan flag levels dan diagnostik gabungan yang lebih mendukung:

{md(goodtable)}

Australia memberi koefisien q/NEG positif pada model bilateral; tanda tersebut sesuai perbaikan trade balance ketika depresiasi, bersyarat pada spesifikasi dan proksi data. Pada kelompok komoditas beberapa koefisien depresiasi tidak signifikan, termasuk model yang lolos diagnostik. **Tidak signifikan bukan bukti efek nol atau bukti bahwa harga global sepenuhnya menentukan ekspor.** Koefisien negatif yang tidak signifikan juga tidak membuktikan depresiasi merugikan.

Belum boleh menyatakan hipotesis komoditas terbukti hanya karena satu kelompok signifikan dan kelompok lain tidak. Perbedaan sensitivitas harus diuji secara langsung dengan memperhitungkan kovarians estimasi kedua kelompok; run ini melaporkan model kelompok dan sensitivitas harga tanpa mengklaim uji lintas-kelompok tersebut sudah dilakukan. Bukti J-curve memerlukan pola awal memburuk dan kemudian membaik yang didukung hubungan jangka panjang; grafik saja atau satu koefisien lag signifikan tidak cukup.

## 7. File dan reproduksi

| Folder | Keluaran |
|---|---|
| input/reference/oskooee_replication/ | PDF sumber, ekstraksi teks, paket ardl yang dipakai dan provenance |
| intermediate/ | Oskooee_Quarterly_Analysis.csv dan oskooee/analysis_quarterly.dta |
| script/ | 00_master.do, 00_run_oskooee.ps1, 12_prepare_oskooee_models.py, 13_run_oskooee_models.do, 14_report_oskooee_results.py, 15_export_oskooee_graphs.do, 16_finalize_oskooee_report.py |
| output/tables/oskooee/ | CSV/DTA, workbook, tabel koefisien lengkap setiap model utama dan ringkasan, seluruhnya juga PNG/PDF |
| output/figures/oskooee/ | Respons dinamis +/-ln(1.10), fitted/residual, stabilitas, forest plots, neraca nominal; PNG/PDF |
| output/gph/oskooee/ | Grafik Stata editable untuk CUSUM, CUSUMSQ, multiplier dan residual |
| output/diagnostics/oskooee/ | Log, unit-root, bounds/residual/stability summaries, desain numerik, covariance, .ster levels, screening HS4 dan validasi |
| notes/ | Catatan hasil ini dan catatan audit sumber |

File .ster menyimpan persamaan ARDL levels yang ekuivalen; tabel ECM ternormalisasi disimpan terpisah dan do-file membangunnya ulang. Dynamic multiplier intervals adalah pointwise delta-method 95% dengan uncertainty parameter model terpilih, bukan confidence band simultan lintas horizon. Respons ditampilkan sebagai 100 x perubahan ln(M/X), bukan langsung persen perubahan ekspor.

Dari direktori Tio, jalankan `powershell -ExecutionPolicy Bypass -File script/00_run_oskooee.ps1` untuk pipeline data -> Stata -> laporan -> native graphs. Parameter PythonExe, StataExe, PythonPackages dapat diubah sesuai instalasi. `00_master.do` menjalankan bagian estimasi Stata dari dataset yang telah disiapkan. Paket Python tercantum dalam requirements_oskooee.txt; cache dan temporary diarahkan ke drive proyek karena C sempit. Wrapper menjalankan pemeriksaan akhir/pembuatan catatan melalui skrip 16. Jika sumber makro atau klasifikasi diperbarui, bangun ulang tahap 03 -> 06 -> 04 -> 07 -> 08 terlebih dahulu agar panel kelompok konsisten; tahap TiVA tidak dijalankan dalam analisis ini.

Jangan menimpa hasil final yang ingin dipertahankan tanpa menyalinnya ke archive/versi_tertentu terlebih dahulu. Run ini adalah hasil analisis awal; versi lama data mentah tidak dipindahkan atau diubah.

Rujukan implementasi bounds: [Kripfganz-Schneider, Stata Journal 2023](https://doi.org/10.1177/1536867X231212434), dokumentasi paket ardl yang disimpan. CUSUM: [manual Stata](https://www.stata.com/manuals/tsestatsbcusum.pdf).
'''
    (ROOT/'notes/hasil_ardl_nardl_oskooee.md').write_text(report,encoding='utf-8')
    (T/'README.md').write_text('''# ARDL/NARDL results

Start with [Oskooee_Results.xlsx](Oskooee_Results.xlsx) or [world summary image](01_world_results_1.png).

- 01_world_results_*.png/pdf: baseline world table.
- 02_partner_results_*.png/pdf: ten partner models.
- 03_goods_results_*.png/pdf: commodity/noncommodity groups.
- 04_sensitivity_results_*.png/pdf: every sensitivity estimate.
- *_coefficients.png/pdf: complete short-run/long-run coefficient table per primary model.
- primary_compact.csv: short summary; results_all_models.csv: all 174.
- coefficients_ecm_with_LR_constant.csv includes the derived normalized long-run intercept.

Read [the interpretation and caveats](../../../notes/hasil_ardl_nardl_oskooee.md). Significance is not a substitute for bounds and diagnostics.
''',encoding='utf-8')
    (F/'README.md').write_text('''# Analysis graphs

- [World net trade balance](world_net_trade_balance.png): exports minus imports, USD billion.
- [World NARDL responses](WORLD_NARDL_AIC4_multipliers.png).
- [World NARDL stability](WORLD_NARDL_AIC4_stability.png).
- forest_bilateral.png/pdf and forest_goods.png/pdf: all main NARDL depreciation coefficients with nominal intervals.
- Every primary model has *_multipliers, *_residuals and *_stability in PNG/PDF.

Negative dynamic response of ln(M/X) means improvement. See notes before interpreting LR responses. Native editable versions are in output/gph/oskooee/.
''',encoding='utf-8')
    provenance={'paper_original':r'C:\Users\Administrator\Downloads\bahmani-oskooee2015.pdf',
       'paper_sha256':hashlib.sha256((ROOT/'input/reference/oskooee_replication/bahmani-oskooee2015.pdf').read_bytes()).hexdigest(),
       'Stata':'19.5 IC (installed executable StataMP-64.exe; runtime flavor observed in probe)',
       'ardl_version':'1.0.6, 06feb2023, Kripfganz-Schneider',
       'python_version':platform.python_version(),'input_import_mechanism':'ON_HOLD'}
    (ROOT/'input/reference/oskooee_replication/provenance.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
    cusumcheck=pd.read_csv(D/'CUSUM_cross_implementation_check.csv')
    assert cusumcheck.difference.max()<2e-5
    delivery={'cusum_cross_implementation_max_difference':float(cusumcheck.difference.max()),'status':'PASS','required_primary_artifacts_checked':len(required),
        'tables_png':len(list(T.glob('*.png'))),'figures_png':len(list(F.glob('*.png'))),
        'native_gph':len(list(G.glob('*.gph'))),'all_png_files_verified':True,
        'models':174,'primary_models':62,'HS4_screened':len(u),'HS4_preeligible':int(u.PreEstimation_Eligible.sum()),
        'not_claimed':['All HS4 individually estimated','World goods groups estimated','Causal export effect established','All diagnostic tests passed']}
    (D/'delivery_validation.json').write_text(json.dumps(delivery,indent=2),encoding='utf-8')
    print(json.dumps(delivery,indent=2))

if __name__=='__main__':main()
