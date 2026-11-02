"""High-precision checks of the exact Gaussian pole-cut correction.
No critical-line Dirichlet series is evaluated. Two algebraically independent
expressions for the finite pole integral are compared at 80 decimal digits.
This script is a diagnostic supplement to the analytic proof, not its substitute.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=80

def pole_direct(x,h,W):
 def V(z):return mp.exp(-1j*z*mp.log(x)-z*z/(2*W*W))
 return -2*mp.pi*mp.quad(lambda s:V(-h/2-1j*s)-V(h/2-1j*s),[0,mp.mpf('.5')])
def pole_sine(x,h,W):
 return -4j*mp.pi*mp.exp(-h*h/(8*W*W))*mp.quad(lambda s:mp.power(x,-s)*mp.exp(s*s/(2*W*W))*mp.sin(h*(mp.log(x)-s/(W*W))/2),[0,mp.mpf('.5')])
def out(z):return {'real':mp.nstr(mp.re(z),50),'imag':mp.nstr(mp.im(z),50)}

def run():
 result={'status':'HIGH_PRECISION_DIAGNOSTICS_NOT_INTERVAL_CERTIFICATE','precision_decimal_digits':mp.mp.dps,'phase_checks':[],'asymptotic_checks':[],'branch_origin_checks':[]}
 for x,h,W in [(mp.mpf('.1'),mp.mpf('.2'),mp.mpf(3)),(mp.mpf('.001'),mp.mpf('.1'),mp.mpf(10)),(mp.mpf(1),mp.mpf('.3'),mp.mpf(2)),(mp.mpf(2),mp.mpf('.2'),mp.mpf(3))]:
  p=pole_direct(x,h,W);q=pole_sine(x,h,W);err=abs(p-q)
  assert err<mp.mpf('1e-70')*(1+abs(p))
  if x<=1:assert mp.im(p)>0 and abs(mp.re(p))<mp.mpf('1e-70')
  result['phase_checks'].append({'x':str(x),'h':str(h),'W':str(W),'direct':out(p),'sine_form':out(q),'absolute_difference':mp.nstr(err,10),'mixed_coefficient_for_c_equals_minus_i':out(1j*p)})
 eta=mp.mpf('0.25')
 for T in [mp.mpf(100),mp.mpf(10000),mp.mpf('1e8')]:
  h=mp.pi/mp.log(T);W=T/mp.log(T);k=T**(1+eta);p=pole_sine(1/k,h,W)
  leading=4j*mp.pi*mp.sin(h*mp.log(k)/2)*(mp.sqrt(k)-1)/mp.log(k)
  ratio=p/leading
  assert mp.im(p)>0 and abs(ratio-1)<mp.mpf('.001')
  result['asymptotic_checks'].append({'T':str(T),'eta':str(eta),'h':mp.nstr(h,30),'W':mp.nstr(W,30),'k':mp.nstr(k,30),'pole':out(p),'leading_pole':out(leading),'pole_to_leading_ratio':out(ratio),'negative_mixed_pole':out(1j*p/mp.sqrt(k))})
 for h in [mp.mpf('.1'),mp.mpf('.01')]:
  # At these tiny heights the horizontal branch agrees with principal log:
  # Im log zeta(.5+i*t) approaches -pi for t down to0.
  zplus=mp.log(mp.zeta(mp.mpf('.5')+1j*h/2));zminus=mp.log(mp.zeta(mp.mpf('.5')-1j*h/2))
  deltaS=mp.im(zplus-zminus)/mp.pi
  gamma_increment=2*mp.siegeltheta(h/2)/mp.pi
  total=gamma_increment+deltaS+2
  assert abs(total)<mp.mpf('1e-65')
  result['branch_origin_checks'].append({'h':str(h),'deltaS':mp.nstr(deltaS,50),'theta_increment_over_pi':mp.nstr(gamma_increment,50),'required_origin_indicator':2,'sum':mp.nstr(total,10)})
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':run()
