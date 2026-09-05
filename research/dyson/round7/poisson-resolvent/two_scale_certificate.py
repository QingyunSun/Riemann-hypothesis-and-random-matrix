"""Exact rational enclosures for a two-scale AH-Pairs discriminator.

This certifies constants and algebra, not the missing arithmetic inequality.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def interval(value):
    return (F(value),F(value))


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def neg(a):
    return -a[1],-a[0]


def mul(a,b):
    products=[x*y for x in a for y in b]
    return min(products),max(products)


def scale(a,c):
    return mul(a,interval(c))


def power(a,n):
    result=interval(1)
    for _ in range(n):
        result=mul(result,a)
    return result


def main():
    n=40
    lower=sum((F(1,factorial(k)) for k in range(n+1)),F(0))
    tail=F(1,factorial(n+1))/(1-F(1,n+2))
    e=(lower,lower+tail)
    q=(1/e[1],1/e[0])
    # W = sinh(2)*V(2) - sinh(1)*V(1).
    ah=interval(F(3,2))
    for term in (scale(power(e,2),F(1,4)),scale(power(q,2),F(5,4)),neg(e),scale(q,-2)):
        ah=add(ah,term)
    gue=interval(F(3,4))
    for term in (scale(power(e,2),F(1,4)),neg(e),q,scale(power(q,2),F(-5,4)),scale(power(q,4),F(1,4))):
        gue=add(gue,term)
    gap=add(gue,neg(ah))
    assert F('0.06239')<ah[0]<ah[1]<F('0.06240')<F('0.07')
    assert F('0.07')<F('0.08227')<gue[0]<gue[1]<F('0.08228')
    assert F('0.019879')<gap[0]<gap[1]<F('0.019880')
    assert ah[1]<F('0.06240')<F(1,16)
    assert F(1,16)-ah[1]>F('0.00010')
    out={"status":"PASS: exact rational separation constants",
         "exp_one_taylor_degree":n,
         "exp_one_interval":[str(x) for x in e],
         "AH_W_interval":[str(x) for x in ah],
         "GUE_W_interval":[str(x) for x in gue],
         "GUE_minus_AH_interval":[str(x) for x in gap],
         "decimal_brackets":{"AH":["0.06239","0.06240"],"GUE":["0.08227","0.08228"],"difference":["0.019879","0.019880"]},
         "sufficient_missing_arithmetic_lower_bound":"liminf W_T >= 7/100",
         "weaker_sufficient_lower_bound":"liminf W_T >= 1/16",
         "certified_1_over_16_minus_AH_lower_bound":"greater than 0.00010",
         "p0_cancellation":"sinh(2)*2*(p0-1)/sinh(2)-sinh(1)*2*(p0-1)/sinh(1)=0",
         "scope":"Algebra and constant enclosure only. No inequality for actual zeta mean squares has been proved."}
    (HERE/'two_scale_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('_interval')},indent=2))


if __name__=='__main__':
    main()
