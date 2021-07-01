from matplotlib import pyplot as pl
from matplotlib import cm
import numpy as np
import sys

pl.rcParams['figure.dpi'] = 150
pl.rcParams['figure.figsize']=[4,4]
pl.rcParams['axes.facecolor'] = 'black'


fn=sys.argv[1] # the FASTA file name
a=open(fn,'r')
b=list(a)
a.close()
c="".join([x.strip().upper().replace("N","") for x in b[1:]]) # makes all uppercase and deletes Ns

windowsize=1000 #  change as desired
plotskip=10     #  change as desired
at=[]
cg=[]
d=[0,0,0,0]
r=c[0:windowsize]
dorder=['A','C','G','T']

d[0]=r.count('A')
d[1]=r.count('C')
d[2]=r.count('G')
d[3]=r.count('T')

at.append((d[0]+1)/(d[3]+1))
cg.append((d[1]+1)/(d[2]+1))

for i in range(1,len(c)-windowsize):
    drm=dorder.index(c[i-1])
    drp=dorder.index(c[i+(windowsize-1)])
    d[drm]-=1
    d[drp]+=1
    at.append((d[0]+1)/(d[3]+1))
    cg.append((d[1]+1)/(d[2]+1))

xat=np.log(np.array(at))
ycg=np.log(np.array(cg))

pl.scatter(xat[::plotskip],ycg[::plotskip],alpha=0.1,s=1,c=range(len(xat[::plotskip])))
pl.gca().set_aspect('equal')
#pl.show()
figname=fn+".strandbias.png"
pl.savefig(figname,dpi=150)
