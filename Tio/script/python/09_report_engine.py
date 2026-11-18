"""Validate Stata ARDL/NARDL fits, compute multipliers/diagnostics and publish figures.
No TiVA/input-import regressors. All inferential qualifications remain explicit.
"""
from pathlib import Path
import os,json,hashlib,re,math,warnings,gc
warnings.filterwarnings("ignore",message="acorr_lm currently returns",category=FutureWarning)
ROOT=Path(__file__).resolve().parents[2]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'output/diagnostics/oskooee/mplcache'))
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.diagnostic import het_arch
from statsmodels.stats.multitest import multipletests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

T=ROOT/'output/tables/oskooee';D=ROOT/'output/diagnostics/oskooee';F=ROOT/'output/figures/oskooee'
for p in [T,D,F]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Arial','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
MC={}

def csv(df,path):df.to_csv(path,index=False,float_format='%.12g',encoding='utf-8')
def savefig(fig,name):
    if os.environ.get('OSKOOEE_SKIP_EXISTING_PLOTS')=='1' and (F/(name+'.png')).exists() and (F/(name+'.pdf')).exists():
        plt.close(fig);gc.collect();return
    fig.savefig(F/(name+'.png'),dpi=200,bbox_inches='tight')
    fig.savefig(F/(name+'.pdf'),bbox_inches='tight');plt.close(fig);gc.collect()
def read_dta(path):return pd.read_stata(path,convert_categoricals=False,convert_dates=False)
def coef_var(term):return term.split('.')[-1]
def lag(term):
    if term.startswith('L.') or term.startswith('L1.'):return 1
    m=re.match(r'L(\d+)\.',term)
    return int(m.group(1)) if m else 0

def multiplier(b,terms,v,shock,H=24):
    phi={lag(t):b[i] for i,t in enumerate(terms) if coef_var(t)=='y' and lag(t)>0}
    bx={lag(t):b[i] for i,t in enumerate(terms) if coef_var(t)==v}
    ans=np.zeros(H+1)
    for h in range(H+1):
        ans[h]=sum(a*ans[h-j] for j,a in phi.items() if h>=j)+shock*sum(a for j,a in bx.items() if j<=h)
    return ans

def recursive(y,X):
    n,k=X.shape;start=k
    while start<n and np.linalg.matrix_rank(X[:start])<k:start+=1
    if n-start<10:return None
    w=[]
    for i in range(start,n):
        A=X[:i];z=y[:i];b=np.linalg.lstsq(A,z,rcond=None)[0]
        # pinv is stable for the trending GDP design; the model rank is checked separately.
        inv=np.linalg.pinv(A.T@A,rcond=1e-14)
        scale=1+X[i]@inv@X[i]
        if scale<=0:return None
        w.append((y[i]-X[i]@b)/np.sqrt(scale))
    return start,np.array(w)

def cumsq_ref(n):
    if n not in MC:
        rng=np.random.default_rng(20261117+n)
        a=rng.standard_normal((19999,n))**2
        curve=np.cumsum(a,axis=1)/a.sum(axis=1)[:,None]
        sup=np.max(np.abs(curve-np.arange(1,n+1)/n),axis=1)
        MC[n]=(np.quantile(sup,.95),sup)
    return MC[n]

def table_image(df,title,name,footer='',fontsize=9):
    a=df.copy().fillna('')
    height=max(2.8,.34*(len(a)+2)+1.2)
    fig,ax=plt.subplots(figsize=(max(12,1.65*len(a.columns)),height));ax.axis('off')
    ax.set_title(title,loc='left',fontsize=14,fontweight='bold',pad=20)
    tab=ax.table(cellText=a.astype(str).values,colLabels=a.columns,cellLoc='center',loc='upper center',colWidths=([.26]+[.74/(len(a.columns)-1)]*(len(a.columns)-1)) if a.columns[0]=='Series' else None)
    tab.auto_set_font_size(False);tab.set_fontsize(fontsize);tab.scale(1,1.5)
    for (r,c),cell in tab.get_celld().items():
        cell.set_edgecolor('#d6dee8')
        if r==0:cell.set_facecolor('#183b56');cell.set_text_props(color='white',weight='bold')
        elif r%2==0:cell.set_facecolor('#eef3f8')
    fig.text(.02,.025,footer,fontsize=8,va='bottom')
    fig.savefig(T/(name+'.png'),dpi=200,bbox_inches='tight')
    fig.savefig(T/(name+'.pdf'),bbox_inches='tight');plt.close(fig);gc.collect()

def fmt(x,d=3):return '' if pd.isna(x) else f'{x:.{d}f}'
def main():
    reg=pd.read_csv(D/'case_registry.csv')
    # Stata summary scalars may be float-stored; official path agreement uses 1e-6.
    official_paths=pd.read_csv(D/'stata_cusum_paths.csv')
    official_by_model={key:g.set_index('tq') for key,g in official_paths.groupby('model_id')}
    s=read_dta(T/'model_summary.dta');ec=read_dta(T/'coefficients_ecm.dta')
    lev=read_dta(T/'coefficients_levels.dta');cov=read_dta(T/'covariance_levels.dta')
    unit=read_dta(D/'unit_root_tests.dta');fail=read_dta(D/'model_failures.dta')
    expected=int((reg.status=='ESTIMATE').sum()*2+(reg.scenario.eq('main')&reg.status.eq('ESTIMATE')).sum()*2)
    assert not s.model_id.duplicated().any()
    if len(s)!=expected:raise AssertionError(f'Expected {expected} fits, got {len(s)}. Review model_failures.csv')
    assert fail.empty or fail.stage.eq('bounds_test').all(),fail.to_dict('records')
    assert s.rank_full.eq(1).all()
    s=s.merge(reg,on=['series_id','scope','scenario'],how='left',validate='many_to_one')
    for key in ['ect','lr_yd','lr_yf','lr_q','lr_pos','lr_neg','lr_cp']:
        var={'ect':'y','lr_yd':'yd','lr_yf':'yf','lr_q':'q','lr_pos':'pos','lr_neg':'neg','lr_cp':'cp'}[key]
        eq='ADJ:' if key=='ect' else 'LR:'
        a=ec[ec.term.str.startswith(eq)&ec.term.map(coef_var).eq(var)][['model_id','b','se','p','lo95','hi95']]
        a=a.rename(columns={x:key+'_'+x for x in a if x!='model_id'})
        assert not a.model_id.duplicated().any()
        s=s.merge(a,on='model_id',how='left',validate='one_to_one')
    s['lag_order']=''
    s['Diagnostic_Flags']=''
    s['I2_not_ruled_out']=False
    s['Recursive_initial_rank_deficient']=False
    details=[];dyn=[];squares=[];checks=[];constant_rows=[]
    for index,row in s.iterrows():
        model=row.model_id
        a=lev[lev.model_id.eq(model)].sort_values('idx');terms=a.term.tolist();b=a.b.to_numpy(float)
        cv=cov[cov.model_id.eq(model)];V=cv.pivot(index='i',columns='j',values='covariance').to_numpy(float)
        design=read_dta(D/'models'/f'{model}_design.dta')
        xx=sorted([x for x in design if re.fullmatch(r'X\d+',x)],key=lambda x:int(x[1:]))
        X=design[xx].to_numpy(float);y=design.y.to_numpy(float)
        assert X.shape[1]==len(b)==V.shape[0]
        fit=X@b;res=y-fit
        assert row.level_RSS_diff<=1e-7*max(1,float(res@res)),model
        np.testing.assert_allclose(res,design.residual,rtol=1e-5,atol=2e-7)
        independent=np.linalg.lstsq(X,y,rcond=None)[0]
        np.testing.assert_allclose(X@independent,fit,rtol=1e-5,atol=2e-7)
        checks.append({'model_id':model,'max_fitted_difference_python_stata':float(np.max(np.abs(X@independent-fit))),
                       'design_condition_number':float(np.linalg.cond(X))})
        phi={lag(t):b[i] for i,t in enumerate(terms) if coef_var(t)=='y' and lag(t)>0}
        roots=np.roots([1]+[-phi.get(j,0) for j in range(1,max(phi)+1)])
        rootmax=float(np.max(np.abs(roots)));s.loc[index,'max_AR_root']=rootmax
        pord=max(phi);lagspec=[pord]
        den=1-sum(phi.values());ci=terms.index('_cons');con=b[ci]/den
        gradient=np.zeros(len(b));gradient[ci]=1/den
        for jj,tt in enumerate(terms):
            if coef_var(tt)=='y' and lag(tt)>0:gradient[jj]=b[ci]/den**2
        cse=np.sqrt(max(0,float(gradient@V@gradient)))
        ct=con/cse if cse>0 else np.nan;cprob=2*stats.t.sf(abs(ct),row.df_r)
        ccrit=stats.t.ppf(.975,row.df_r)
        constant_rows.append({'model_id':model,'term':'LR:_cons','b':con,'se':cse,'t':ct,'p':cprob,'lo95':con-ccrit*cse,'hi95':con+ccrit*cse})
        for v in ['yd','yf']+(['q'] if row.estimator=='ARDL' else ['pos','neg'])+(['cp'] if row.price_control else []):
            lagspec.append(max([lag(t) for t in terms if coef_var(t)==v],default=0))
            calculated=sum(b[i] for i,t in enumerate(terms) if coef_var(t)==v)/(1-sum(phi.values()))
            target=row.get('lr_'+v+'_b',np.nan)
            if not pd.isna(target):np.testing.assert_allclose(calculated,target,rtol=1e-5,atol=1e-6)
        s.loc[index,'lag_order']='('+','.join(str(x) for x in lagspec)+')'
        jb=stats.jarque_bera(res);s.loc[index,'JB_p']=jb.pvalue
        try:s.loc[index,'ARCH4_p']=het_arch(res,nlags=4,ddof=X.shape[1])[1]
        except Exception:s.loc[index,'ARCH4_p']=np.nan
        initial_rank=int(np.linalg.matrix_rank(X[:X.shape[1]]))
        s.loc[index,'Recursive_initial_rank_deficient']=initial_rank<X.shape[1]
        checks[-1].update({'initial_recursive_rank':initial_rank,'K':X.shape[1]})
        rr=recursive(y,X)
        if rr is not None:
            start,w=rr;n=len(w);tau=np.arange(1,n+1)/n
            path=np.cumsum(w*w)/np.sum(w*w);stat=float(np.max(np.abs(path-tau)))
            crit,sim=cumsq_ref(n);pv=(1+np.count_nonzero(sim>=stat))/(1+len(sim))
            s.loc[index,'CUSUMSQ_stat']=stat;s.loc[index,'CUSUMSQ_p_MC']=pv
            s.loc[index,'CUSUMSQ_cv95_MC']=crit;s.loc[index,'recursive_start']=start
            stdev=np.std(w,ddof=1)
            cs=np.cumsum(w)/stdev/np.sqrt(n)
            bounds=.9479006054*(1+2*tau)
            official_model=official_by_model.get(model)
            if official_model is not None:
                assert abs(official_model.official_stat.iloc[0]-row.cusum)<1e-6,model
                official_max=np.max(np.abs(official_model.CUSUM)/(1+2*official_model.cusum_expected))
                assert abs(official_max-row.cusum)<1e-6,model
            for j in range(n):
                squares.append({'model_id':model,'tq':int(design.tq.iloc[start+j]),'CUSUMSQ':path[j],
                    'expected':tau[j],'lower':max(0,tau[j]-crit),'upper':min(1,tau[j]+crit),
                    'Python_CUSUM':cs[j],'CUSUM':float(official_model.loc[int(design.tq.iloc[start+j]),'CUSUM']) if official_model is not None else cs[j],
                    'CUSUM_source':'Stata estat sbcusum' if official_model is not None else 'Independent full-rank initialization',
                    'CUSUM_scale_df':1,'cusum_lower':float(official_model.loc[int(design.tq.iloc[start+j]),'cusum_lower']) if official_model is not None else -bounds[j],
                    'cusum_upper':float(official_model.loc[int(design.tq.iloc[start+j]),'cusum_upper']) if official_model is not None else bounds[j]})
        maincase=row.scenario=='main' and row.cap==4
        if maincase:
            xs=design.tq.to_numpy();dates=[str(pd.Period('1960Q1',freq='Q')+int(v)) for v in xs]
            fig,ax=plt.subplots(2,1,figsize=(10,6),sharex=True)
            ax[0].plot(xs,y,label='Actual ln(M/X)',color='#1b4f72');ax[0].plot(xs,fit,label='Fitted',color='#cb6b2b',alpha=.8)
            ax[0].legend();ax[0].set_title(model+' | fitted values and residuals')
            ax[1].axhline(0,color='gray',lw=.8);ax[1].plot(xs,res,color='#1b4f72');ax[1].set_ylabel('Residual')
            ticks=np.linspace(0,len(xs)-1,6,dtype=int);ax[1].set_xticks(xs[ticks],np.array(dates)[ticks]);savefig(fig,model+'_residuals')
            if rr is not None:
                z=pd.DataFrame(squares[-len(w):]);fig,ax=plt.subplots(1,2,figsize=(12,4))
                cz=official_model.reset_index() if official_model is not None else z
                ax[0].plot(cz.tq,cz.CUSUM,color='#1b4f72');ax[0].plot(cz.tq,cz.cusum_lower,'--',color='#bb4444');ax[0].plot(cz.tq,cz.cusum_upper,'--',color='#bb4444')
                ax[0].set_title('Recursive CUSUM | Stata statistic='+fmt(row.cusum))
                ax[1].plot(z.tq,z.CUSUMSQ,color='#1b4f72');ax[1].plot(z.tq,z.expected,':',color='gray')
                ax[1].fill_between(z.tq,z.lower,z.upper,color='#d6e5f1');ax[1].plot(z.tq,z.CUSUMSQ,color='#1b4f72')
                ax[1].set_title('CUSUMSQ | Gaussian-reference MC p='+fmt(pv))
                for aa in ax:
                    ticks=np.linspace(0,len(z)-1,4,dtype=int);aa.set_xticks(z.tq.iloc[ticks],[str(pd.Period('1960Q1',freq='Q')+int(v)) for v in z.tq.iloc[ticks]],rotation=20)
                fig.suptitle(model);fig.tight_layout();savefig(fig,model+'_stability')
        for direction,v,shock in [('depreciation','q' if row.estimator=='ARDL' else 'neg',-np.log(1.1)),('appreciation','q' if row.estimator=='ARDL' else 'pos',np.log(1.1))]:
            response=multiplier(b,terms,v,shock)
            grad=np.zeros((25,len(b)))
            for j,t in enumerate(terms):
                if coef_var(t) not in ['y',v]:continue
                step=1e-5*max(1,abs(b[j]));bb=b.copy();bb[j]+=step;bm=b.copy();bm[j]-=step
                grad[:,j]=(multiplier(bb,terms,v,shock)-multiplier(bm,terms,v,shock))/(2*step)
            se=np.sqrt(np.maximum(0,np.einsum('ij,jk,ik->i',grad,V,grad)))
            critical=stats.t.ppf(.975,row.df_r)
            for h in range(25):dyn.append({'model_id':model,'direction':direction,'horizon_quarters':h,
                 'effect_logpoints':100*response[h],'lower95_logpoints':100*(response[h]-critical*se[h]),
                 'upper95_logpoints':100*(response[h]+critical*se[h]),'shock_log_q':shock})
        if maincase:
            a=pd.DataFrame(dyn[-50:]);fig,ax=plt.subplots(figsize=(10,4.8))
            for direction,color in [('depreciation','#1b4f72'),('appreciation','#cb6b2b')]:
                z=a[a.direction.eq(direction)];ax.plot(z.horizon_quarters,z.effect_logpoints,label=direction,color=color)
                ax.fill_between(z.horizon_quarters,z.lower95_logpoints,z.upper95_logpoints,color=color,alpha=.15)
            ax.axhline(0,color='gray',lw=.8);ax.set(xlabel='Quarters after permanent +/-ln(1.10) exchange-rate shock',ylabel='100 x change in ln(M/X)',title=model+' | dynamic responses')
            ax.legend();fig.text(.02,.01,'Pointwise delta-method 95% intervals; conditional associations, not causal effects. Negative = trade-balance improvement.',fontsize=8)
            savefig(fig,model+'_multipliers')
        print('POSTPROCESSED',model,flush=True)
    # Unit-root flag: failure to reject in both first-difference tests is a caution, not proof of I(2).
    ec=pd.concat([ec,pd.DataFrame(constant_rows)],ignore_index=True)
    csv(ec,T/'coefficients_ecm_with_LR_constant.csv')
    s['Estimation_Start']=[str(pd.Period(a,freq='Q')+int(b)) for a,b in zip(s.first_quarter,s.cap)]
    s['Estimation_End']=s.last_quarter
    caution={}
    for sid,g in unit[unit['transform'].eq('diff')&unit['test'].isin(['ADF_BIC','PP'])].groupby('sid'):
        caution[sid]=set(v for v,a in g.groupby('variable') if len(a)>=2 and a.p.gt(.10).all())
    for i,r in s.iterrows():
        used={'y','yd','yf','q'}|({'pos','neg'} if r.estimator=='NARDL' else set())|({'cp'} if r.price_control else set())
        s.loc[i,'I2_not_ruled_out']=bool(caution.get(r.sid,set())&used)
    s['Bounds5']=np.where((s.F_pI1<.05)&(s.t_pI1<.05),'Reject no-level relation',np.where((s.F_pI0>.05)|(s.t_pI0>.05),'No rejection','Inconclusive'))
    s.loc[s.F_pI1.isna()|s.t_pI1.isna(),'Bounds5']='Unavailable'
    s['Bounds10_Fonly_paper_style']=s.F_pss>s.F_hi10
    s['Dynamic_stable']=s.max_AR_root<1
    s['Levels_supported5']=s.Bounds5.eq('Reject no-level relation')&s.lr_x_p.lt(.05)&s.Dynamic_stable&~s.I2_not_ruled_out.astype(bool)&s.df_r.ge(15)
    s['CUSUM_stable5']=s.cusum.le(s.cusum_cv5)
    s['Diagnostic_clean5']=~s.Recursive_initial_rank_deficient & s.bg4_p.ge(.05)&s.hetero_p.ge(.05)&s.reset_p.ge(.05)&s.CUSUM_stable5&s.CUSUMSQ_p_MC.ge(.05)&s.ARCH4_p.ge(.05)&s.JB_p.ge(.05)
    s['Interpretation_Status']=np.where(s.Levels_supported5& s.Diagnostic_clean5,'Levels supported; diagnostics not rejected',np.where(s.Levels_supported5,'Levels supported; diagnostic caveats','Long-run interpretation not established'))
    for i,r in s.iterrows():
        flags=[]
        for col,label in [('bg4_p','BG4 serial correlation'),('hetero_p','heteroskedasticity'),('reset_p','RESET'),('CUSUMSQ_p_MC','CUSUMSQ instability'),('ARCH4_p','ARCH4'),('JB_p','non-normal residuals')]:
            if pd.notna(r[col]) and r[col]<.05:flags.append(label)
        if not r.CUSUM_stable5:flags.append('CUSUM instability or unavailable')
        if r.I2_not_ruled_out:flags.append('I(2) not ruled out')
        if r.df_r<15:flags.append('low residual df')
        if r.Recursive_initial_rank_deficient:flags.append('Recursive initial matrix rank deficient; official Stata CUSUM retained')
        s.loc[i,'Diagnostic_Flags']='; '.join(flags) or 'No rejection in listed tests'
    s['Dep_LR_p']=np.where(s.estimator.eq('ARDL'),s.lr_q_p,s.lr_neg_p)
    s['Dep_LR_p_BH']=np.nan
    mainmask=s.scenario.eq('main')&s.cap.eq(4)
    for _,g in s[mainmask].groupby(['scope','estimator']):
        good=g.Dep_LR_p.dropna()
        if len(good):s.loc[good.index,'Dep_LR_p_BH']=multipletests(good,method='fdr_bh')[1]
    primary=s[mainmask].copy()
    for df,name in [(s,'results_all_models.csv'),(primary,'results_primary_models.csv')]:csv(df,T/name)
    csv(pd.DataFrame(dyn),D/'dynamic_multipliers.csv');csv(pd.DataFrame(squares),D/'stability_paths.csv')
    sp=pd.DataFrame(squares)
    cu=sp.groupby('model_id').apply(lambda g:np.max(np.abs(g.Python_CUSUM)/(1+2*g.expected)),include_groups=False).rename('python_cusum')
    cc=primary[['model_id','cusum','Recursive_initial_rank_deficient']].merge(cu,on='model_id')
    cc['difference']=abs(cc.cusum-cc.python_cusum)
    cc['independent_check_applicable']=~cc.Recursive_initial_rank_deficient
    cc['check_status']=np.where(cc.independent_check_applicable,'Independent agreement required','Initialization differs: singular first-K design; use official Stata path')
    assert cc.loc[cc.independent_check_applicable,'difference'].max()<2e-5
    assert set(primary.model_id)==set(official_paths.model_id)
    cc['official_path_reproduces_stored_statistic']=True
    csv(cc,D/'CUSUM_cross_implementation_check.csv')
    csv(pd.DataFrame(checks),D/'independent_OLS_checks.csv')
    csv(s[['model_id','N','df_r','lag_order','F_pss','t_pss','F_pI0','F_pI1','t_pI0','t_pI1','Bounds5','lr_x_p','bg1_p','bg4_p','hetero_p','reset_p','JB_p','ARCH4_p','cusum','cusum_cv5','CUSUMSQ_p_MC','max_AR_root','I2_not_ruled_out','Levels_supported5','Diagnostic_Flags']],D/'diagnostic_summary.csv')
    # Every primary model gets a readable coefficient table image (short and long run).
    for _,r in primary.iterrows():
        a=ec[ec.model_id.eq(r.model_id)].copy()
        a['Estimate']=a.b.map(fmt);a['SE']=a.se.map(fmt);a['p-value']=a.p.map(fmt)
        a['95% CI']=['['+fmt(l)+', '+fmt(h)+']' for l,h in zip(a.lo95,a.hi95)]
        table_image(a[['term','Estimate','SE','p-value','95% CI']],r.label+' | '+r.estimator+' '+r.lag_order,
            r.model_id+'_coefficients',f'{r.first_quarter} to {r.last_quarter}; estimated N={int(r.N)}. Outcome ln(M/X); q up=appreciation.\n{r.Interpretation_Status}. Post-AIC p-values/intervals are nominal, without selection correction.')
    def summary_table(a,title,name):
        out=pd.DataFrame({'Series':a.label,'Model':a.estimator,'N':a.N.astype(int),'Lag':a.lag_order,
            'LR q / POS':np.where(a.estimator.eq('ARDL'),a.lr_q_b,a.lr_pos_b),
            'LR NEG':a.lr_neg_b,'Wald LR p':a.lr_asym_p,'Bounds 5%':a.Bounds5,
            'BG4 p':a.bg4_p,'CUSUM':np.where(a.CUSUM_stable5,'Stable','Reject')})
        for c in ['LR q / POS','LR NEG','Wald LR p','BG4 p']:out[c]=pd.Series(out[c]).map(fmt)
        for start in range(0,len(out),12):
            table_image(out.iloc[start:start+12],title,name+f'_{start//12+1}',
                'q up=appreciation; NEG is depreciation. Positive LR NEG implies a depreciation reduces ln(M/X).\nLong-run estimates require levels support and diagnostic review; significance alone is insufficient.',fontsize=8)
    summary_table(primary[primary.scope.eq('aggregate')],'Indonesia-World | baseline', '01_world_results')
    summary_table(primary[primary.scope.eq('bilateral')],'Ten partner models | baseline','02_partner_results')
    summary_table(primary[primary.scope.eq('goods')],'Seven overlapping HS6 goods groups | baseline','03_goods_results')
    summary_table(s[~s.index.isin(primary.index)],'Sensitivity models | all estimates retained','04_sensitivity_results')
    # Workbook with complete estimates and all diagnostics, not just starred coefficients.
    with pd.ExcelWriter(T/'Oskooee_Results.xlsx',engine='openpyxl') as wr:
        primary.to_excel(wr,sheet_name='Primary',index=False);s.to_excel(wr,sheet_name='All_models',index=False)
        ec.to_excel(wr,sheet_name='ECM_coefficients',index=False);unit.to_excel(wr,sheet_name='Unit_roots',index=False)
        reg.to_excel(wr,sheet_name='Samples',index=False)
    # Forest plots show all estimates, including diagnostically qualified ones.
    for scope in ['bilateral','goods']:
        a=primary[primary.scope.eq(scope)&primary.estimator.eq('NARDL')].sort_values('label')
        fig,ax=plt.subplots(figsize=(11,max(5,.4*len(a))))
        pos=np.arange(len(a));ax.errorbar(a.lr_neg_b,pos,xerr=[a.lr_neg_b-a.lr_neg_lo95,a.lr_neg_hi95-a.lr_neg_b],fmt='o',color='#1b4f72',capsize=3)
        ax.axvline(0,color='gray',lw=.8);ax.set_yticks(pos,a.label);ax.invert_yaxis()
        ax.set(xlabel='Long-run coefficient on NEG (95% nominal interval)',title='NARDL '+scope+' | depreciation coefficient; check bounds and diagnostics')
        savefig(fig,'forest_'+scope)
    # Descriptive net trade balance remains in USD, separate from model outcome.
    w=pd.read_csv(ROOT/'intermediate/Panel_World_Quarter.csv');x=np.arange(len(w))
    fig,ax=plt.subplots(figsize=(11,4.5));ax.plot(x,w.World_Trade_Balance_USDk/1e6,color='#1b4f72')
    ax.axhline(0,color='gray',lw=.8);ax.axvspan(0,15,color='#e5ab62',alpha=.25,label='2006-2009: extended-sample sensitivity')
    ticks=np.arange(0,len(w),8);ax.set_xticks(ticks,w.Quarter.iloc[ticks],rotation=30)
    ax.set(ylabel='USD billion',title='Indonesia-World | exports minus imports');ax.legend();savefig(fig,'world_net_trade_balance')
    hashes=json.loads((D/'input_sha256.json').read_text('utf-8'))
    for name,digest in hashes.items():assert hashlib.sha256((ROOT/'intermediate'/name).read_bytes()).hexdigest()==digest,name
    report={'status':'PASS','models_expected':expected,'models_estimated':len(s),'primary_models':len(primary),
        'nonfatal_bounds_test_failures':fail.to_dict('records'),
        'substantive_validity':'MODEL_SPECIFIC; see bounds and diagnostics',
        'all_levels_ECM_equivalence_pass':True,'all_independent_OLS_prediction_checks_pass':True,
        'input_files_unchanged':True,'input_import_hypothesis':'EXCLUDED',
        'primary_bounds5_rejections':int(primary.Bounds5.eq('Reject no-level relation').sum()),
        'primary_levels_supported5':int(primary.Levels_supported5.sum()),
        'primary_levels_and_diagnostics_supported5':int((primary.Levels_supported5&primary.Diagnostic_clean5).sum()),
        'primary_by_scope':primary.groupby('scope').size().to_dict(),
        'CUSUMSQ_reference':'19999 Gaussian Monte Carlo draws, fixed seed, sample-size specific; approximate diagnostic',
        'inference_limits':['Nominal post-AIC inference','No causal identification from ARDL alone',
          'World demand proxy is top10, not global GDP','HS6 goods groups cover World and ten partners; categories overlap',
          'Historical source/revision issues remain; see input/reference/audit_validitas_data_macro.md']}
    (D/'analysis_validation_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2),flush=True)

if __name__=='__main__':main()
