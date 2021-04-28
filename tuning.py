import numpy as np
from nested_dict import nested_dict
ad=np.array([6,8,9,10,11,13])
dg=ad
gc=ad

full=[]
p=0
for m in ad:
    for n in dg:
        for o in gc:
            q = m+n+o
            if 27<q<29:
                full[p] = (m, n, o)
                p=p+1
for f in range(len(full)):
    intset=full[(f)]
    n=0
    m=1
    o=0
    pitch=[0]
    cond=[0]
    while n < len(intset):
        pitch.append(intset[n]+pitch[-1])
        n=n+1
    while m < len(pitch):
        cond.append(pitch[m]%12)
        m=m+1
    cond=sorted(cond)
    conlist=[(cond)]
    conde=(cond[-1:]+cond[:-1])
    for r in range(len(cond)-1):
        q=(12-conde[0])
        for s in range(len(conde)):
            conde[s]=(conde[s]+q)
            conde[s]=(conde[s]%12)
            s=s+1
        conlist.append(conde)
        conde=(conde[-1:]+conde[:-1])
        r=r+1
    f=f+1
dex=[]
for c in range(len(conlist)):
    dex.append(conlist[c][3])
    c=c+1
prime=[]
