"""Compact human-readable delivery report for the Comtrade data ingestion."""
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.styles import Font,PatternFill

ROOT=Path(__file__).resolve().parents[1]
AUD=ROOT/'output/diagnostics/comtrade_hs6'
MID=ROOT/'intermediate/comtrade_hs6'
TAB=ROOT/'output/tables/comtrade_hs6'
FIG=ROOT/'output/figures/comtrade_hs6'
plt.rcParams.update({'font.family':'Arial','font.size':11,'axes.spines.top':False,'axes.spines.right':False})

def main():
    TAB.mkdir(parents=True,exist_ok=True);FIG.mkdir(parents=True,exist_ok=True)
    report=json.loads((AUD/'Validation_Report.json').read_text(encoding='utf-8'))
    manifest=json.loads((ROOT/'input/raw/un_comtrade_hs6_20261117/download_manifest.json').read_text(encoding='utf-8'))
    quality=pd.read_csv(AUD/'Weight_quantity_coverage.csv')
    month=quality[quality.Frequency.eq('M')].copy()
    summary=month.groupby(['ISO3','Flow']).agg(Product_Month_Rows=('Product_Rows','sum'),
        Positive_Weight_Rows=('Positive_Weight_Rows','sum'),Estimated_Weight_Rows=('Estimated_Weight_Rows','sum'),
        Usable_Quantity_Rows=('Usable_Quantity_Rows','sum'),Trade_Value_USD=('Trade_Value_USD','sum'),
        Value_With_Weight_USD=('Value_With_Weight_USD','sum'),Value_Estimated_Weight_USD=('Value_Estimated_Weight_USD','sum')).reset_index()
    summary['Weight_Value_Coverage_pct']=100*summary.Value_With_Weight_USD/summary.Trade_Value_USD
    summary['Usable_Quantity_Row_pct']=100*summary.Usable_Quantity_Rows/summary.Product_Month_Rows
    summary['Estimated_Weight_Value_pct']=100*summary.Value_Estimated_Weight_USD/summary.Trade_Value_USD
    summary.to_csv(TAB/'Weight_quantity_summary.csv',index=False)
    calendar=pd.read_csv(AUD/'Monthly_availability_calendar.csv')
    gaps=calendar[(calendar.Period>=report['first_month'])&(calendar.Period<=report['last_month'])&~calendar.Available_In_Comtrade_Metadata]
    pre=calendar[(calendar.Period<report['first_month'])&~calendar.Available_In_Comtrade_Metadata]
    coverage=calendar.assign(Year=calendar.Date.str[:4].astype(int)).groupby('Year').Available_In_Comtrade_Metadata.sum()
    annual=pd.read_csv(AUD/'Annual_vs_monthly_HS6_sums.csv')
    recon=pd.read_csv(AUD/'HS6_vs_TOTAL_reconciliation.csv')
    previous=pd.read_csv(AUD/'Comtrade_vs_previous_bilateral_monthly.csv')
    worldprev=pd.read_csv(AUD/'Comtrade_vs_previous_world_annual.csv')
    # Compatibility with the initial in-flight build: these annual fields were
    # already converted to USD; give their columns the correct unit labels.
    legacy={'Exports_USDk':'Exports_Previous_GEM_USD','Imports_USDk':'Imports_Previous_GEM_USD'}
    if any(c in worldprev for c in legacy):
        worldprev=worldprev.rename(columns=legacy)
        worldprev.to_csv(AUD/'Comtrade_vs_previous_world_annual.csv',index=False,float_format='%.17g')
    classifications=pd.read_csv(MID/'HS6_Commodity_Classification_By_Edition.csv',dtype={'HS6':str})
    classsum=classifications.groupby(['HS_Edition_Year','Commodity_Class']).size().reset_index(name='HS6_Codes')
    dictionary=pd.DataFrame([
        ['ISO3','Mitra dagang; WLD berarti seluruh dunia','Kode negara'],
        ['Period / Date / Quarter','Periode sumber; bulan YYYYMM / YYYY-MM; kuartal YYYYQn','Waktu'],
        ['HS_Edition / HS_Edition_Year','Revisi HS asli sumber; bagian dari identitas produk','Kode / tahun revisi'],
        ['HS6','Kode produk enam digit; simpan sebagai teks agar nol depan tetap ada','Kode produk'],
        ['Flow','X = ekspor Indonesia; M = impor Indonesia','Arus perdagangan'],
        ['Trade_Value_USD','Nilai perdagangan nominal; kolom kuartalan utama memerlukan tiga bulan nyata','USD'],
        ['Trade_Value_USDk','Trade_Value_USD dibagi 1.000','Ribu USD'],
        ['Net_Weight_kg','Berat bersih; kuartalan utama memerlukan cakupan berat yang memenuhi syarat','kg'],
        ['Quantity / Quantity_Unit_Code','Kuantitas tambahan dan kode satuan sumber; angka 0 dengan unit -1 tidak berarti volume nol yang valid','Satuan sumber'],
        ['Net_Weight_Estimated / _Any','Penanda penyedia mengestimasi berat; Any untuk setidaknya satu bulan','Boolean'],
        ['Quantity_Estimated / _Any','Penanda kuantitas tambahan diestimasi','Boolean'],
        ['Weight_Usable','Berat positif yang dapat menjadi penyebut unit value','Boolean'],
        ['Quantity_Usable','Kuantitas positif dengan kode satuan valid','Boolean'],
        ['Unit_Value_USD_per_kg','Nilai dibagi berat; bukan indeks harga murni','USD / kg'],
        ['NMonths_Source_Rows','Jumlah bulan dengan baris produk asli pada kuartal itu','0 sampai 3'],
        ['Complete_Product_Quarter','Tiga baris produk-bulan nyata dan tiga bulan dataset tersedia','Boolean'],
        ['Observed_*','Jumlah dari observasi tersedia, termasuk kuartal yang belum lengkap','Sesuai variabel'],
        ['Commodity_Class / Commodity_Flag','UNCTAD A11: komoditas 1, nonkomoditas 0, mixed/unknown tetap missing pada flag','Kategori / biner'],
        ['Is_Reported / Is_Aggregate','Metadata kompilasi HS dari sumber; agregasi bukan otomatis estimasi nilai','Boolean'],
        ['Positive_Both_Flows_With_Macro','Kedua arus positif dan kontrol makro tersedia; bukan sertifikat kelayakan model','Boolean'],
        ['Foreign_Activity_Top10_FixedWeight_Index','Proksi permintaan asing 10 mitra untuk WLD; bukan PDB dunia','Indeks'],
        ['RER_Bilateral_Index_2015mean100','Kurs riil bilateral pada panel makro lama: naik berarti depresiasi','Indeks'],
        ['REER_BIS_broad','Kurs riil efektif BIS: naik berarti apresiasi; arah berbeda dari RER bilateral','Indeks'],
        ['Export_* / Import_*','Variabel arus pada tabel dua arus; prefiks menunjukkan arah perdagangan','Sesuai variabel'],
    ],columns=['Variable','Definition','Unit'])
    dictionary.to_csv(MID/'Data_Dictionary.csv',index=False,encoding='utf-8-sig')
    readme=pd.DataFrame([
        ['Status',report['status']],['Source','UN Comtrade, reporter Indonesia, original HS editions'],
        ['Monthly available',f"{report['first_month']}–{report['last_month']}; {report['monthly_periods']} months"],
        ['Annual available',f"{report['annual_first']}–{report['annual_last']}; annual only"],
        ['Internal gaps',', '.join(gaps.Date)],['Requested months unavailable before first',len(pre)],
        ['Monthly HS6 rows',report['monthly_rows']],['Annual HS6 rows',report['annual_rows']],
        ['HS6 vs TOTAL max absolute pct',report['max_abs_HS6_vs_TOTAL_pct']],
        ['Native HS editions harmonized',False],['Original research panels unchanged',report['original_panels_unchanged']],
        ['Models reestimated',False],['Absent product-months converted to zero',False],
        ['Annual data disaggregated',False],['Quantity unit rule','Same unit within product/partner/HS edition/quarter'],
        ['Units','Values: USD; net weight: kg; quantity: source unit code'],
        ['USA','Comtrade trade area842 includes Puerto Rico and US Virgin Islands'],
        ['India','Comtrade699, not historical code356'],
        ['Interpretation','Unit values can change with composition/quality and are not pure price indexes'],
    ],columns=['Item','Explanation'])
    target=TAB/'Comtrade_HS6_Data_Audit.xlsx'
    with pd.ExcelWriter(target,engine='openpyxl') as writer:
        for sheet,df in [('Readme',readme),('Definitions',dictionary),('Weight_quantity',summary),('Monthly_calendar',calendar),
            ('HS6_vs_TOTAL',recon),('Annual_vs_Monthly',annual),('Previous_monthly',previous),
            ('Previous_world_annual',worldprev),('Classifications',classsum)]:
            df.to_excel(writer,sheet_name=sheet,index=False)
    wb=load_workbook(target)
    for ws in wb:
        ws.freeze_panes='B2';ws.auto_filter.ref=ws.dimensions
        for cell in ws[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='A5644E')
        for col in ws.columns:
            length=max(len(str(c.value)) if c.value is not None else 0 for c in list(col)[:200])
            ws.column_dimensions[col[0].column_letter].width=min(70,max(14,length+2))
    wb.save(target);wb.close()
    fig,ax=plt.subplots(figsize=(10.8,3.2));ax.bar(coverage.index,coverage,color='#A5644E')
    ax.axhline(12,color='#6B6B6B',lw=1,ls=':');ax.set_ylim(0,13);ax.set_ylabel('Months available in metadata')
    ax.set_xlabel('Year');ax.set_xticks(list(range(2006,2027,2)));ax.set_title('Indonesia: monthly HS6 availability in the downloaded vintage')
    fig.tight_layout();fig.savefig(FIG/'monthly_availability.png',dpi=200);fig.savefig(FIG/'monthly_availability.pdf');plt.close(fig)
    order=sorted(summary.ISO3.unique());x=np.arange(len(order))
    fig,ax=plt.subplots(figsize=(10.8,3.5))
    for offset,flow,col,label in [(-.17,'X','#A5644E','Exports'),(.17,'M','#4E3B30','Imports')]:
        v=summary[summary.Flow.eq(flow)].set_index('ISO3').reindex(order)
        ax.bar(x+offset,v.Weight_Value_Coverage_pct,.32,color=col,label=label)
    ax.set_xticks(x,order);ax.set_ylim(0,105);ax.set_ylabel('Trade value with positive net weight (%)')
    ax.legend(frameon=False,loc='upper left',bbox_to_anchor=(1.01,1))
    ax.set_title('Weight coverage; each partner and World shown separately')
    fig.tight_layout();fig.savefig(FIG/'net_weight_coverage.png',dpi=200);fig.savefig(FIG/'net_weight_coverage.pdf');plt.close(fig)
    world=summary[summary.ISO3.eq('WLD')]
    weight_lines='\n'.join(f"- {('Ekspor' if r.Flow=='X' else 'Impor')}: {r.Weight_Value_Coverage_pct:.2f}% nilai perdagangan mempunyai berat bersih positif; {r.Usable_Quantity_Row_pct:.2f}% baris mempunyai kuantitas dengan kode satuan valid; {r.Estimated_Weight_Value_pct:.2f}% nilai terkait baris dengan flag berat estimasi." for r in world.itertuples())
    note=f'''# Data HS-6 UN Comtrade: cakupan, kualitas, dan penggabungan

Tanggal penyusunan: 17 November 2026. Data baru disimpan terpisah; hasil model dan PPT lama belum dihitung ulang.

## Hasil unduhan

- Permintaan mulai2006. Data bulanan yang tercantum/terambil pada vintage ini: **{report['first_month']}–{report['last_month']}**, {report['monthly_periods']} bulan; **{report['monthly_rows']:,} baris** produk–mitra–arus–bulan.
- Data tahunan pelengkap: **{report['annual_first']}–{report['annual_last']}**, **{report['annual_rows']:,} baris**. Data ini tetap tahunan, tidak dibagi menjadi bulan atau kuartal.
- Bulan kosong di tengah cakupan: **{', '.join(gaps.Date)}**. Periode2006 sampai sebelumDesember2012 tidak tersedia pada unduhan bulanan ini. Oktober2026 belum tercantum saat diambil.
- Reporter: Indonesia. Sepuluh mitra sesuai penelitian ditambah World (seluruh mitra). World jangan dijumlahkan lagi dengan sepuluh mitra karena akan menghitung perdagangan dua kali.
- India memakai kode Comtrade699; AS memakai wilayah perdagangan842 (termasuk PuertoRiko dan USVirginIslands). Definisi tersimpan di manifest.

## Berat dan kuantitas

Angka berikut memakai perdagangan Indonesia–dunia saja agar tidak menggandakan total dunia dengan bilateral:

{weight_lines}

Berat bersih dalam kg tidak sama dengan kuantitas tambahan dalam unit produk. Nilai nol, missing, kode satuan tidak valid dan flag estimasi dipertahankan. Pada file bulanan/tahunan, angka0 pada Quantity dengan kode satuan-1 bukan observasi volume nol yang valid; gunakan flag Quantity_Usable dan Weight_Usable. Unit value dihitung perproduk–mitra–periode dan hanya jika penyebut positif. Ia masih dapat berubah karena kualitas/komposisi dalam HS-6, sehingga bukan indeks harga murni. Menjumlahkan kg dari seluruh jenis produk tidak membentuk ukuran volume ekspor yang sebanding secara ekonomi.

## Lokasi file

- Raw respons API: `input/raw/un_comtrade_hs6_20261117/`; manifest berisi parameter, waktu, jumlah baris dan checksum tanpa APIkey.
- [Workbook audit](../output/tables/comtrade_hs6/Comtrade_HS6_Data_Audit.xlsx).
- [Panel total kuartalan + makro](../intermediate/comtrade_hs6/Trade_Total_Quarter_Macro.csv).
- [Panel total bulanan + makro](../intermediate/comtrade_hs6/Trade_Total_Month_Macro.csv).
- [Total tahunan](../intermediate/comtrade_hs6/Trade_Total_Annual.csv).
- Panel produk bulanan: `intermediate/comtrade_hs6/monthly/` (CSV.GZ, dipartisi perkuartal).
- Panel produk kuartalan: `intermediate/comtrade_hs6/quarterly/`; format long dan dua arus + GDP/kurs/CPI/harga komoditas.
- Panel produk tahunan: `intermediate/comtrade_hs6/annual/`.
- [Indeks file/checksum](../intermediate/comtrade_hs6/File_Index.csv).
- [Klasifikasi komoditas HS-6 menurut revisi](../intermediate/comtrade_hs6/HS6_Commodity_Classification_By_Edition.csv).
- [Deskripsi produk menurut revisi](../intermediate/comtrade_hs6/HS6_Product_Codebook_By_Edition.csv) dan [kamus variabel](../intermediate/comtrade_hs6/Data_Dictionary.csv).
- Audit rinci: `output/diagnostics/comtrade_hs6/`.

## Aturan pengolahan

1. Data asli tidak diedit; respons JSON/CSV dikompresi lossless. Probe awal tidak masuk manifest produksi dan tidak dipakai untuk panel.
2. Nilai USD dibagi1.000 hanya pada kolom USDk. Pengecekan dilakukan terhadap TOTAL Comtrade dengan reporter, mitra, arus dan periode yang sama.
3. Kunci menyertakan revisi HS asli. **Belum ada harmonisasi HS antarwaktu**; kode identik antarversi tidak otomatis dianggap produk identik. Ini wajib diperhatikan sebelum model produk jangka panjang.
4. Kelas komoditas memakai korespondensi langsung HS-6–SITC3 perrevisi dan definisi UNCTAD A11. Kategori campuran/tidak terklasifikasi dipertahankan, tidak diberi labelnonkomoditas secara paksa.
5. Ketidakhadiran baris produk–bulan tidak diubah otomatis menjadi nol. `Observed_*` kuartalan menyimpan jumlah baris yang tersedia; kolom utama kuartalan mensyaratkan tiga baris produk–bulan nyata. Kuantitas tambahan juga mensyaratkan satuan konsisten.
6. GDP hanya digabungkan sebagai variabel kuartalan; tidak diinterpolasi menjadi GDP bulanan. Makro lama tetap mempunyai catatan audit sebelumnya, termasuk CPI/FX yang kosong dan proksi permintaan dunia.
   Arah RER bilateral lama: naik=depresiasi. REER BIS dunia: naik=apresiasi. Transformasi tanda untuk model paper belum dilakukan pada panel data ini.
7. Pengecekan integritas bukan pengesahan semua sumber sudah harmonis. Selisih dengan dataset lama dilaporkan, tidak dihilangkan dengan rescaling.

## Status validasi

- Status: **{report['status']}**.
- Maksimum absolut selisih jumlahHS-6 vsTOTAL: **{report['max_abs_HS6_vs_TOTAL_pct']:.8f}%**; {report['HS6_vs_TOTAL_rows_over_0p01pct']} baris melebihi ambang review0,01%.
- Panel penelitian lama: checksum tidak berubah.
- Perbandingan tahunan2006–2009 menunjukkan Comtrade dekat dengan GEM; ini belum merekonsiliasi selisih historis terhadap WDI pada audit sebelumnya.
- Ekspor–impor HS-6 bulanan lengkap sejak2006: **belum tersedia** dari unduhan ini. Untuk memperpanjang seri volume, cari sumber pelengkap BPS/TradeMap dengan definisi dan revisiHS yang dapat direkonsiliasi.
- Kelengkapan makro, harmonisasiHS, penyaringan seri dan desain identifikasi masih perlu ditangani sebelum estimasi baru. Tidak ada klaim hipotesis telah diuji dengan data baru.

## Reproduksi

Jalankan skrip19 (unduh/resume),20 (panel/audit),21 (workbook/laporan), serta22 (kamus deskripsi publik) dari folder `script/`. Key dibaca dari `.env.comtrade` lokal yang diabaikanGit; jangan menaruh key pada argumen commandline, log, URL tersimpan atau raw.

Rujukan primer: [API UN Comtrade](https://comtradeplus.un.org/en/api-docs), [metadata kolom](https://comtradeplus.un.org/en/reference-tables?table=dataitem), [kuota](https://comtradeplus.un.org/en/subscriptions), dan [klasifikasi UNSD](https://unstats.un.org/unsd/classifications/Econ).
'''
    for old,new in [('mulai2006','mulai 2006'),('Periode2006','Periode 2006'),('sebelumDesember2012','sebelum Desember 2012'),('Oktober2026','Oktober 2026'),('Comtrade699','Comtrade 699'),('perdagangan842','perdagangan 842'),('PuertoRiko','Puerto Riko'),('USVirginIslands','US Virgin Islands'),('APIkey','API key'),('perproduk','per produk'),('perkuartal','per kuartal'),('dibagi1.000','dibagi 1.000'),('perrevisi','per revisi'),('labelnonkomoditas','label nonkomoditas'),('jumlahHS-6 vsTOTAL','jumlah HS-6 vs TOTAL'),('review0,01%','review 0,01%'),('sejak2006','sejak 2006'),('revisiHS','revisi HS'),('harmonisasiHS','harmonisasi HS'),('skrip19','skrip 19'),('),20','), 20'),('),21','), 21'),('diabaikanGit','diabaikan Git'),('commandline','command line')]:note=note.replace(old,new)
    for old,new in [('angka0','angka 0'),('satuan-1','satuan -1'),('tahunan2006','tahunan 2006'),('serta22','serta 22')]:
        note=note.replace(old,new)
    (ROOT/'notes/data_hs6_un_comtrade.md').write_text(note,encoding='utf-8')
    report['internal_month_gaps']=gaps.Date.tolist();report['delivery_workbook']=str(target.relative_to(ROOT))
    (AUD/'Validation_Report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'workbook':str(target),'internal_gaps':gaps.Date.tolist(),
        'world_weight_quantity_summary':world.to_dict('records')},ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()
