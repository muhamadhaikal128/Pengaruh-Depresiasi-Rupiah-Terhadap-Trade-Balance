"""Classify observed HS4 using UNCTAD A11 and official direct UNSD correlations.
Run offline; --download restores missing pinned raw sources from the request file.
"""
from pathlib import Path
from collections import defaultdict
import argparse, hashlib, json, re
import pandas as pd
import xlrd
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'
RAW=ROOT/'input/raw/hs_commodity_classification_20261117'
YEARS=[1992,1996,2002,2007,2012,2017,2022]
CLASSES=['commodity','noncommodity','mixed','unclassified']


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def csvout(df,p): df.to_csv(p,index=False,float_format='%.12g',encoding='utf-8')

def normalized(v):
    if v is None:return ''
    return str(v).strip().replace('.','')

def sitc_group(s):
    if not re.fullmatch(r'\d{3,5}',s):return 'unclassified','Unallocated_or_no_SITC'
    if s[0] in '01' or s.startswith('22') or s[0]=='4':return 'commodity','Food_beverages_tobacco_oils'
    if s.startswith(('27','28','68','667','971')):return 'commodity','Ores_metals_precious_stones_gold'
    if s[0]=='2':return 'commodity','Agricultural_raw_materials'
    if s[0]=='3':return 'commodity','Fuels'
    if s[0] in '5678':return 'noncommodity','Manufactured_goods'
    return 'unclassified','Unallocated_or_special_transactions'

def consensus(values):
    s=set(values)
    return next(iter(s)) if len(s)==1 else 'mixed' if s else 'unclassified'

def table_rows(path,kind,year):
    if path.suffix=='.xls':
        w=xlrd.open_workbook(path)
        s=next(x for x in w.sheets() if kind.lower() in x.name.lower())
        hi,si=({1992:(3,4),1996:(2,3),2002:(2,3),2007:(3,4),2012:(2,3)}[year]
               if kind=='Correlation' else
               {1992:(3,4),1996:(3,4),2002:(3,4),2007:(2,3),2012:(2,3)}[year])
        for i in range(s.nrows):
            row=s.row_values(i);h,t=normalized(row[hi]),normalized(row[si])
            if re.fullmatch(r'\d{6}',h):yield h,t,s.name,i+1
        w.release_resources()
    else:
        w=load_workbook(path,read_only=True,data_only=True)
        s=next(x for x in w if kind.lower() in x.title.lower())
        for i,row in enumerate(s.iter_rows(values_only=True),1):
            h,t=normalized(row[0]),normalized(row[1])
            if re.fullmatch(r'\d{6}',h):yield h,t,s.title,i
        w.close()

def sources(download=False):
    requests=json.loads((Path(__file__).parent/'hs_classification_source_requests.json').read_text('utf-8'))
    RAW.mkdir(parents=True,exist_ok=True)
    for r in requests:
        p=RAW/r['filename']
        if not p.exists():
            if not download:raise FileNotFoundError(f'{p}; run with --download')
            import httpx
            resp=httpx.get(r['url'],timeout=120,follow_redirects=True);resp.raise_for_status()
            assert hashlib.sha256(resp.content).hexdigest()==r['sha256'],f'Changed remote source: {r["filename"]}'
            p.write_bytes(resp.content)
        assert sha(p)==r['sha256'],r['filename']
    return requests

def build():
    universe=defaultdict(set)
    w=load_workbook(RAW/'unsd_correlations_2022.xlsx',read_only=True,data_only=True)
    rows=w.active.iter_rows(values_only=True);next(rows)
    for row in rows:
        for y,v in zip(YEARS,row[:7]):
            h=normalized(v)
            if re.fullmatch(r'\d{6}',h):universe[y].add(h)
    w.close()
    detail=[];conversions={};byedition=[]
    for year in YEARS:
        p=next(RAW.glob(f'HS{year}_SITC3.*'))
        corr=list(table_rows(p,'Correlation',year));conv=list(table_rows(p,'Conversion',year))
        assert len(corr)>4000 and len(conv)>4000,(year,len(corr),len(conv))
        seen=set()
        for h,s,sheet,row in corr:
            if (h,s) in seen:continue
            seen.add((h,s));c,g=sitc_group(s)
            detail.append({'HS_Edition':year,'HS6':h,'HS_Code':h[:4],'SITC3':s or 'UNMAPPED',
                'Commodity_Class':c,'Commodity_Subgroup':g,'Source_File':p.name,
                'Source_Sheet':sheet,'Source_Row':row})
        mapped={h for h,s in seen}
        for h in universe[year]-mapped:
            detail.append({'HS_Edition':year,'HS6':h,'HS_Code':h[:4],'SITC3':'UNMAPPED',
                'Commodity_Class':'unclassified','Commodity_Subgroup':'Unallocated_or_no_SITC',
                'Source_File':'unsd_correlations_2022.xlsx','Source_Sheet':'HS SITC BEC','Source_Row':None})
        for h,s,sheet,row in conv:conversions.setdefault((year,h[:4]),set()).add(sitc_group(s)[0])
    detail=pd.DataFrame(detail).sort_values(['HS_Edition','HS_Code','HS6','SITC3']).reset_index(drop=True)
    for (year,h),g in detail.groupby(['HS_Edition','HS_Code'],sort=True):
        byedition.append({'HS_Edition':year,'HS_Code':h,
            'Commodity_Class':consensus(g.Commodity_Class),
            'Commodity_Class_Conversion':consensus(conversions.get((year,h),set())),
            'N_HS6':g.HS6.nunique(),'N_SITC3':g.SITC3.nunique(),
            'SITC3_Groups':';'.join(sorted({s[:3] for s in g.SITC3})),
            'Possible_Classes':';'.join(sorted(set(g.Commodity_Class))),
            'Commodity_Subgroups':';'.join(sorted(set(g.Commodity_Subgroup)))})
    ed=pd.DataFrame(byedition)
    lookup=pd.read_csv(MID/'HS_Lookup.csv',dtype={'HS_Code':str})
    assert lookup.HS_Code.str.fullmatch(r'\d{4}').all() and not lookup.HS_Code.duplicated().any()
    mapping=[]
    for _,r in lookup.iterrows():
        g=ed[ed.HS_Code.eq(r.HS_Code)];types=set(g.Commodity_Class)
        # A mixed revision remains mixed, even if all other editions are pure.
        c=consensus(types)
        groups=sorted({s for cell in g.SITC3_Groups for s in cell.split(';')})
        subgroups=sorted({s for cell in g.Commodity_Subgroups for s in cell.split(';')})
        result={'HS_Code':r.HS_Code,'Product':r.Product,'Commodity_Class':c,
            'Commodity_Flag':1 if c=='commodity' else 0 if c=='noncommodity' else None,
            'Binary_Sample':c in ['commodity','noncommodity'],
            'Commodity_Subgroups':';'.join(subgroups),'SITC3_Groups':';'.join(groups),
            'Available_HS_Editions':';'.join(str(int(y)) for y in g.HS_Edition),
            'HS2022_Present':bool(g.HS_Edition.eq(2022).any()),
            'Legacy_Only_Code':len(g)>0 and not g.HS_Edition.eq(2022).any(),
            'Within_Edition_Mixed':bool(g.Commodity_Class.eq('mixed').any()),
            'Across_Edition_Disagreement':len(types)>1,
            'Class_Conversion_Consensus':consensus(g.Commodity_Class_Conversion),
            'Definition':'UNCTAD A11: SITC3 0+1+2+3+4+68+667+971',
            'Revision_Basis':'Consensus across direct HS1992-2022 correlations; source edition unconfirmed'}
        for y in YEARS:
            a=g[g.HS_Edition.eq(y)]
            result[f'Class_HS{y}']=a.Commodity_Class.iloc[0] if len(a) else ''
        mapping.append(result)
    mapping=pd.DataFrame(mapping);mapping['Commodity_Flag']=mapping.Commodity_Flag.astype('Int64')
    # Economic anchor cases and critical exclusions are independent of output size.
    by=mapping.set_index('HS_Code')
    for h in ['0901','1511','2701','2709','7502']:assert by.loc[h,'Commodity_Class']=='commodity',h
    for h in ['6109','7202','8703']:assert by.loc[h,'Commodity_Class']=='noncommodity',h
    assert by.loc['9999','Commodity_Class']=='unclassified'
    assert by.loc['7108','Commodity_Class']=='mixed','HS7108 includes monetary gold outside SITC'
    assert mapping.Commodity_Flag.notna().eq(mapping.Binary_Sample).all()
    assert len(mapping)==len(lookup)
    return mapping,ed,detail

def workbook(mapping,ed,summary):
    wb=Workbook();wb.remove(wb.active)
    frames={'HS4_Classification':mapping,'Summary':summary,
            'HS4_By_Edition':ed,
            'Mixed_Review':mapping[mapping.Commodity_Class.eq('mixed')],
            'Unclassified':mapping[mapping.Commodity_Class.eq('unclassified')]}
    for name,df in frames.items():
        ws=wb.create_sheet(name)
        for row in dataframe_to_rows(df.astype(object).where(pd.notna(df),None),index=False,header=True):ws.append(row)
        ws.freeze_panes='C2';ws.auto_filter.ref=ws.dimensions
        for cell in ws[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='1F3864')
        ws.column_dimensions['A'].width=16;ws.column_dimensions['B'].width=65
    ws=wb.create_sheet('Readme');ws.append(['See Tio/notes/klasifikasi_komoditas_hs4.md. Mixed/unclassified are not binary 0.'])
    target=MID/'HS4_Commodity_Classification.xlsx';temp=target.with_suffix('.tmp.xlsx');wb.save(temp);wb.close();temp.replace(target)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--download',action='store_true');args=ap.parse_args()
    manifest=sources(args.download)
    mapping,ed,detail=build()
    counts=mapping.Commodity_Class.value_counts().reindex(CLASSES,fill_value=0).rename_axis('Commodity_Class').reset_index(name='N_HS4')
    outputs={'HS4_Commodity_Classification.csv':mapping,'HS4_Classification_By_Edition.csv':ed,
        'HS6_SITC3_Commodity_Crosswalk.csv':detail,'HS4_Commodity_Classification_Summary.csv':counts}
    for c in CLASSES:
        p=MID/'hs_classified'/c;p.mkdir(parents=True,exist_ok=True)
        outputs[str(Path('hs_classified')/c/'HS4_List.csv')]=mapping[mapping.Commodity_Class.eq(c)]
    for name,df in outputs.items():
        p=MID/name;temp=p.with_suffix('.tmp.csv');csvout(df,temp);temp.replace(p)
    workbook(mapping,ed,counts)
    report={'status':'PASS','definition':'UNCTAD A11','hs4_count':len(mapping),
        'class_counts':dict(zip(counts.Commodity_Class,counts.N_HS4.astype(int))),
        'all_available_editions_consensus':True,'hs_source_edition_confirmed':False,
        'all_unknown_and_mixed_retained':True,'lookup_sha256':sha(MID/'HS_Lookup.csv'),
        'classification_sha256':sha(MID/'HS4_Commodity_Classification.csv'),
        'raw_sources_sha256_checked':len(manifest),'source_revision_caveat':'No temporal HS harmonisation is asserted.'}
    (MID/'HS4_Classification_Validation_Report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2),flush=True)
    print('REVIEW CODES:',mapping.loc[~mapping.Binary_Sample,['HS_Code','Commodity_Class']].to_dict('records'),flush=True)

if __name__=='__main__':main()
