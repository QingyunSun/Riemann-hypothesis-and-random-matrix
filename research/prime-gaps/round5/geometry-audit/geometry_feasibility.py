#!/usr/bin/env python3
"""Exact source feasibility for bounded radius/plateau variations.

Reads preserving primary-source input code; writes only this round5 directory.
No physical sieve forms are evaluated and no published loss bound is inherited.
"""
from __future__ import annotations
import ast,hashlib,json,math,time,os
from fractions import Fraction as F
from pathlib import Path

BASE=Path('/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04')
SOURCE=Path(os.environ.get('PRIME186_SOURCE', str(BASE/'research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py')))
OUT=Path(__file__).resolve().parent
RHO=F(262499,10**6);GAP=F(1,10**7);RS=RHO-GAP;E=GAP/RHO
SIGMA0=F(100001,10**6);TAU=F(1,10**10);SIGMAM=F(1,2)-F(40481,100000)+TAU
SIGMA_OLD=F(1997,1000);PHYSICAL_SUM_NEW=F(5252997,10**7);SIGMA_NEW=PHYSICAL_SUM_NEW/RS
ZETA=F(19037,100000)/RHO
N=98304


def exact_json(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:exact_json(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [exact_json(v) for v in x]
    return x


def load_ladder():
    ns={'F':F,'math':math}
    node=next(n for n in ast.parse(SOURCE.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='_ladder')
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),ns)
    return ns['_ladder']


def ladders(S,T0,T1):
    build=load_ladder()
    oldcs=(((1-5*SIGMA0)/15,F(18,5)),((1-4*SIGMA0)/16,F(7,2)),(F(3,80),F(3)))
    newcs=(((1-5*SIGMAM)/15,F(18,5)),((1-4*SIGMAM)/16,F(7,2)),((1-2*SIGMAM)/20,F(16,5)))
    return {'old':build('old',T0,F(1,10**6),F(12499,10**6),oldcs,S,RHO,GAP),
            'new':build('new',T1,F(1,10**7),F(253,20000),newcs,S,RHO,GAP)}


def distribution_margins(row):
    w,d,r=row['omega'],row['delta'],row['source_order']
    m={'omega_positive':w,'omega_below_1_over_12':F(1,12)-w,'delta_positive':d,'delta_below_quarter_plus_omega':F(1,4)+w-d}
    if row['ladder']=='old':
        m['prime_corollary_2_19']={1:1-108*w-30*d,2:3-280*w-80*d,3:3-240*w-80*d}[r]
    else:
        m.update(smooth_type0=F(33856,100000)-TAU-F(1,4)-7*w-2*d,
                 typeIII=F(19,200)-TAU-F(1,18)-F(28,9)*w-F(2,9)*d,
                 long_smooth=F(59519,100000)-TAU-F(1,2)-2*w)
        if r<3:
            m['typeII']=1-68*w-14*d
            m['bilinear']=(1-54*w-15*d-5*SIGMAM) if r==1 else (1-56*w-16*d-4*SIGMAM)
        else:
            m.update(typeIII_bilinear1=1-72*w-24*d,typeIII_bilinear2=1-48*w-16*d-4*SIGMAM,
                     typeIII_bilinear3=1-64*w-20*d-2*SIGMAM)
    assert min(m.values())>0,(row['ladder'],row['index'],m)
    return m


def plateau_interval(A,C):
    assert A>C>0
    lower=max((3*A-C)/4,3*A/7,F(0));upper=min(3*A/5,3*C/5,A)
    return lower,upper


def phi(t,L):return min(F(3,2)*t,L)


def check_plateau(A,C,L):
    lo,hi=plateau_interval(A,C)
    if not lo<=L<=hi:return {'valid_template':False,'required_interval':(lo,hi),'supplied_L':L}
    u,v=A-L,(C+L)/4
    margins={'outer_plateau':u-F(2,3)*L,'inner_plateau':v-F(2,3)*L,
             'outer_owner':A-u-phi(u,L),'outer_opposite':C-3*u+phi(u,L),
             'inner_owner':C-4*v+phi(v,L),'inner_opposite':A-phi(v,L),
             'nonlargest_balanced_reduction':F(7,3)*L-max(A,C),
             'outer_lower_order_half_cap':(A+E/2)/2-u}
    assert min(margins.values())>=0,margins
    assert u+4*v==A+C
    return {'valid_template':True,'L':L,'L_over_C':L/C,'outer_cap':u,'inner_cap':v,'margins':margins}


def running_cap_shells(radius,events):
    cap=ZETA;lower=F(0);out=[]
    for core,newcap in sorted(events):
        if core>=radius:continue
        if newcap>=cap:continue
        if core>lower:out.append({'lower':lower,'upper':core,'cap':cap})
        cap=min(cap,newcap);lower=max(lower,core)
    if lower<radius:out.append({'lower':lower,'upper':radius,'cap':cap})
    assert out and all(r['cap']>0 for r in out)
    return out


def event_caps(rows,owner,L):
    events=[]
    for row in rows:
        r=row['source_order'];core=row['a' if owner=='outer' else 'b']
        if r<3:
            if owner=='inner' and r==1:continue
            cap=row['A' if owner=='outer' else 'C']/2
        else:cap=row['A']-L if owner=='outer' else (row['C']+L)/4
        events.append((core,cap))
    return events


def cells(shells,d,h,n,outer_total_cap=None):
    out=[]
    for s in shells:
        first=max(0,s['lower']//h-d+1);last=min(n-1,s['upper']//h-d)
        if outer_total_cap is not None:last=min(last,outer_total_cap-d)
        if first<=last:
            cap=s['cap']//h
            assert cap>0
            out.append({'first_index':int(first),'last_index':int(last),'fragment_cap_cells':int(cap),
                        'physical_total_upper_normalized':(last+d)*h,'fragment_cap_normalized':cap*h,
                        'shell_lower':s['lower'],'shell_upper':s['upper']})
    return out


def cap_array(rows,n):
    a=[0]*n
    for r in rows:
        for j in range(r['first_index'],r['last_index']+1):
            assert a[j]==0
            a[j]=r['fragment_cap_cells']
    return a


def self_square_source(S,T1,new12):
    w,d=F(7,2000),F(1,40)
    bbv=1/(2*RHO);cs=bbv-T1;xi=d/RHO
    margins={'level':F(1,2)+2*w-2*RS*T1,
             'prime':3-280*w-80*d,'prime_fixed_sigma_bilinear':1-56*w-16*d-4*SIGMA0,
             'typeII':1-68*w-14*d,'minorant_bilinear':1-56*w-16*d-4*SIGMAM,
             'minorant_smooth':F(33856,100000)-TAU-F(1,4)-7*w-2*d,
             'minorant_typeIII':F(19,200)-TAU-F(1,18)-F(28,9)*w-F(2,9)*d,
             'minorant_long_smooth':F(59519,100000)-TAU-F(1,2)-2*w,
             'transfer_guard':cs+xi,'row12_core_containment':cs-new12['b'],
             'row12_activation_containment':xi-new12['xi']}
    assert min(margins.values())>0,margins
    return {'omega':w,'delta':d,'level':F(1,2)+2*w,'B_BV':bbv,'c_s':cs,'xi_s':xi,'margins':margins,
            'old_source_level_margin':F(1,2)+2*F(31,10000)-2*RS*T1}


def exceptional_bound(radius):
    xi=F(9519,50000);a=F(40481,100000);step=(a-2*xi)/1024;c=1-2*radius-F(1,5000)
    ans=0;zmin=None;zmax=None
    for j in range(1,1025):
        s=2*xi+j*step;t=(s-2*xi)/xi;z=(c-s)/2
        assert 0<z<F(19037,100000) and s+2*radius+2*z==1-F(1,5000)
        zmin=z if zmin is None else min(zmin,z);zmax=z if zmax is None else max(zmax,z)
        log_upper=sum((1 if m%2 else -1)*t**m/m for m in range(1,22))
        term=10**25*24*step*log_upper/(5*s*(c-s));ans+=-((-term.numerator)//term.denominator)
    return {'K_upper':F(ans,10**25),'z_min':zmin,'z_max':zmax,'counting_margin':F(1,5000)}


def evaluate_geometry(radius,choice='common_min',k=39,trim=True):
    radius=F(radius);S=radius/RS;T0=SIGMA_OLD-S;T1=SIGMA_NEW-S;h=S/N;n=N-k
    assert 0<T0<T1<S and 2*radius<1
    full=ladders(S,T0,T1)
    assert (len(full['old']),len(full['new']))==(29,43)
    for rs in full.values():
        for row in rs:distribution_margins(row)
    Ji={'old':T0//h,'new':T1//h};Jo=N-1
    untrimmed={name:[r for r in rows if r['B']<(Jo+Ji[name])*h] for name,rows in full.items()}
    if trim:Jo=min(Jo,full['new'][39]['B']//h-Ji['new'])
    retained={name:[r for r in rows if r['B']<(Jo+Ji[name])*h] for name,rows in full.items()}
    intervals={};plateaus={};A=S+E/2
    for name,T in [('old',T0),('new',T1)]:
        C=T+E/2;lo,hi=plateau_interval(A,C)
        intervals[name]={'L_min':lo,'L_max':hi,'q_min':lo/C,'q_max':hi/C,'C':C}
    if choice=='published_fractions':Ls={name:F(23,40)*v['C'] for name,v in intervals.items()}
    elif choice=='common_min':Ls={name:intervals['old']['L_min'] for name in intervals}
    elif choice=='common_max':Ls={name:intervals['old']['L_max'] for name in intervals}
    else:raise ValueError('unknown plateau choice')
    for name,T in [('old',T0),('new',T1)]:
        C=T+E/2;plateaus[name]=check_plateau(A,C,Ls[name])
        for row in retained[name]:
            r=row['source_order']
            if r<3:
                assert row['A']==S+E and row['C']==T+E
                assert row['B']+row['xi']>=2*T
                if r==2:assert row['B']+row['xi']>=max(2*S-T,2*T-S)
            else:
                assert row['A']==A and row['C']==C
                assert row['A']+row['C']==row['B']+row['xi']
                assert row['eta_D']==row['xi']-E/2>0
    minxi=min(r['xi'] for rows in retained.values() for r in rows)
    # An exact elementary log39 bound makes the operator bound uniform here.
    ell=F(458,125)
    assert sum(ell**j/math.factorial(j) for j in range(18))>k
    cop_upper=S*k*ell/(k-1)
    assert cop_upper<4
    result={'radius':radius,'S':S,'T0':T0,'T1':T1,'physical_inner0':RS*T0,'physical_inner1':RS*T1,
            'choice':choice,'dimension':k,'N':N,'h':h,'A':A,'plateau_intervals':intervals,'plateaus':plateaus,
            'global_fragment_cap':ZETA,'physical_global_cap':RS*ZETA,
            'untrimmed_retained_indices':{n:[r['index'] for r in rr] for n,rr in untrimmed.items()},
            'retained_indices':{n:[r['index'] for r in rr] for n,rr in retained.items()},
            'outer_total_upper_cells':int(Jo),'outer_index_sum_upper':int(Jo-k),'trimmed_layers':int(N-1-Jo),
            'inner_total_upper_cells':{n:int(v) for n,v in Ji.items()},
            'new_row39_cutoff_slack':full['new'][39]['B']-(Jo+Ji['new'])*h,
            'minimum_retained_activation':minxi,'activation_over_h':minxi/h,'original_minimum_two_cell_guard':minxi>2*h,
            'common_inner_square_source':self_square_source(S,T1,retained['new'][12]),
            'operator_Cop_upper':cop_upper,'operator_Cop4_valid':True,
            'exceptional_square':exceptional_bound(radius),
            'untrimmed_new39_xi_over_h':full['new'][39]['xi']/h,
            'largest_cap_template_valid':all(v['valid_template'] for v in plateaus.values()),
            'physical_integrals_evaluated':False}
    Kbound=result['exceptional_square']['K_upper']
    K=F(-((-Kbound.numerator*10**6)//Kbound.denominator),10**6)
    mass=F(49999,50000);lam=F(1,125);ah=mass*mass-mass*lam;bh=(1-mass/lam)*(1-mass)*K
    d0=1-ah-bh
    assert F(-1,1000)<bh<0 and 0<ah+bh<1 and d0>0 and 1-4*RS*abs(bh)>0
    result['updated_hybrid']={'K_six_decimal_upper':K,'mass':mass,'lambda':lam,'a_h':ah,'b_h':bh,'d0':d0,'a_plus_b':ah+bh,'alpha_coefficient':1-4*RS*abs(bh)}
    if not result['largest_cap_template_valid']:return result
    outerevents=event_caps(retained['old'],'outer',Ls['old'])+event_caps(retained['new'],'outer',Ls['new'])
    oldevents=event_caps(retained['old'],'inner',Ls['old']);newevents=event_caps(retained['new'],'inner',Ls['new'])
    os=running_cap_shells(S,outerevents)
    # Base clipping makes H0 subset H1 even for independently chosen valid L's.
    bs=running_cap_shells(T0,oldevents+newevents);es=running_cap_shells(T1,newevents)
    cellmap={'outer':cells(os,k,h,n,Jo),'base':cells(bs,k-1,h,n),'enlarged':cells(es,k-1,h,n)}
    ca0=cap_array(cellmap['base'],n);ca1=cap_array(cellmap['enlarged'],n)
    assert all(a<=b for a,b in zip(ca0,ca1))
    assert max(r['physical_total_upper_normalized'] for r in cellmap['outer'])==Jo*h
    for name,label in [('old','base'),('new','enlarged')]:
        pairmax=(Jo+Ji[name])*h;rr=retained[name]
        assert rr[0]['B']==1/(2*RHO) and rr[-1]['upper_B']>=pairmax
        assert all(a['upper_B']==b['B'] for a,b in zip(rr,rr[1:]))
        assert max(r['physical_total_upper_normalized'] for r in cellmap[label])==Ji[name]*h
    result.update(shells={'outer':os,'base':bs,'enlarged':es},cells=cellmap,base_enlarged_nesting_checked=True,
                  actual_LCM_band_coverage_checked=True)
    return result


def main():
    start=time.monotonic();radii=['.272','.2742997','.275','.276','.278']
    results=[]
    # Verify that every analytic source row is invariant when sums are fixed.
    base=ladders(F(radii[0])/RS,SIGMA_OLD-F(radii[0])/RS,SIGMA_NEW-F(radii[0])/RS)
    invariant_keys=['omega','delta','B','upper_B','xi']
    for r in radii:
        S=F(r)/RS;rows=ladders(S,SIGMA_OLD-S,SIGMA_NEW-S)
        for name in base:
            for before,after in zip(base[name],rows[name]):
                assert all(before[key]==after[key] for key in invariant_keys)
        for choice in ['published_fractions','common_min','common_max']:
            results.append(evaluate_geometry(r,choice,trim=True))
    oldradius=(17*RS*SIGMA_OLD+RS*E)/32;newradius=(17*PHYSICAL_SUM_NEW+RS*E)/32
    # Regression against the paper's original finite exceptional constant.
    assert exceptional_bound(F(11,40))['K_upper']==F(840334010068226419110401,2500000000000000000000000)
    hmin=F('.272')/RS/N;hmax=F('.278')/RS/N
    delta=SIGMA_NEW-base['new'][39]['B']
    uniform={'h_min':hmin,'h_max':hmax,'terminal_gap_delta':delta,
             'one_layer_lower_slack':delta-hmax,'one_layer_upper_slack':2*hmin-delta,
             'row38_retained_slack':base['new'][39]['B']-base['new'][38]['B']-hmax,
             'row38_two_cell_slack':base['new'][38]['xi']-2*hmax,
             'old_row27_retained_slack':SIGMA_OLD-3*hmax-base['old'][27]['B'],
             'old_row28_excluded_slack':base['old'][28]['B']-SIGMA_OLD,
             'natural_old_plateau_radius_slack':oldradius-F('.278')}
    assert min(v for k,v in uniform.items() if k.endswith('slack'))>0
    out={'status':'exact radius/source/plateau checks complete; no sieve integral bounds',
         'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
         'rho':RHO,'rho_star':RS,'fixed_normalized_sums':{'old':SIGMA_OLD,'new':SIGMA_NEW},
         'source_ladder_invariant_keys':invariant_keys,'uniform_interval_checks':uniform,
         'natural_plateau_radius_upper':{'old':oldradius,'new':newradius},
         'cases':results,'elapsed_seconds':time.monotonic()-start,
         'remaining_obligations':['Regenerate changed positive failure-cover geometry and all physical integral bounds',
             'Update hybrid coefficients using K for maximum actual coefficient-root radius',
             'Do not inherit old97component bounds, Young-cost optimality, or k40trial certificates',
             'Include all actual outer predicates and base intersection with both old/new inner predicates']}
    (OUT/'geometry_feasibility.json').write_text(json.dumps(exact_json(out),indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':len(results),'elapsed_seconds':out['elapsed_seconds'],
       'summary':[{'r':float(c['radius']),'choice':c['choice'],'valid':c['largest_cap_template_valid'],
          'trim':c['trimmed_layers'],'rows_new':len(c['retained_indices']['new']),
          'q_min':[float(c['plateau_intervals'][n]['q_min']) for n in ['old','new']]} for c in results]},indent=2))

if __name__=='__main__':main()
