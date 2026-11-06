from check_first_size import *
n=10
edges,cycles=complement_cycles(n,summary_fibres(n))
ids=sorted({j for cyc in cycles for j,_ in cyc});loc={j:i for i,j in enumerate(ids)}
gs=[edges[j] for j in ids]
D=np.zeros((len(gs),len(cycles)),dtype=np.int64)
for i,cyc in enumerate(cycles):
    for j,sgn in cyc:D[loc[j],i]=sgn
ctx.prec=176
roots=[acb(arb(j)/n).exp_pi_i() for j in range(2*n)]
label=[]
for t in (72,70):
    heat=[(arb(t+1)/t)**(j*(n-j)) for j in range(n+1)]
    d=np.array([is_survivor(b,roots,heat)-is_survivor(a,roots,heat) for a,b in gs])@D
    label.append(d)
results=[]
for p in (101,241,401):
    root=next(a for a in range(2,p) if pow(a,20,p)==1 and
              all(pow(a,j,p)!=1 for j in range(1,20)))
    A=np.array([row for _,_,row in modular_rows(n,gs,p,root)])
    W=A@D%p
    rank=nmod_mat(W.tolist(),p).rank()
    individual=[nmod_mat(np.vstack((W,d%p)).tolist(),p).rank() for d in label]
    both=nmod_mat(np.vstack((W,*(d%p for d in label))).tolist(),p).rank()
    item=dict(prime=p,root=root,rank=rank,individual=individual,both=both)
    results.append(item)

print(json.dumps(results, indent=2))
