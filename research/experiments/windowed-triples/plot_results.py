import csv, sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rows = list(csv.DictReader(open(sys.argv[1])))
plt.rcParams.update({"font.family":"sans-serif", "font.sans-serif":["Arial Unicode MS", "DejaVu Sans"],
                     "axes.unicode_minus":False, "font.size":11.5, "svg.fonttype":"none"})
fig, ax = plt.subplots(figsize=(9.0,5.65))
names = list(dict.fromkeys(r['sample'] for r in rows))[:7]
colors = ["#28767F", "#173353", "#BB6237"]
for i,(w,col) in enumerate(zip((10,20,40), colors)):
    rr=[r for r in rows if r['sample'] in names and int(r['width'])==w]
    y=np.arange(len(rr))+(i-1)*.20
    ax.errorbar([float(r['mean']) for r in rr],y,xerr=[2*float(r['se']) for r in rr],
                color=col,fmt=['o','s','^'][i],ms=4.6,lw=1.15,capsize=2,label=f"窗宽 {w}")
ax.axvline(0,color="#784858",lw=1.4)
ax.axvline(-.4,color="#697980",ls=(0,(4,3)),lw=1.1)
ax.set_yticks(range(7),["第 1–10 万个","第 10 万–100 万个","第 100 万–200 万个",
                         "第 $10^{12}$ 个之后","第 $10^{21}$ 个之后","第 $10^{22}$ 个之后","随机酉矩阵模拟"])
ax.invert_yaxis()
ax.grid(axis="x",alpha=.13)
ax.set_xlim(-1,.12)
ax.set_xlabel("三点统计量的平均读数")
ax.spines[['right','top','left']].set_visible(False)
ax.tick_params(axis='y',length=0,pad=9)
fig.subplots_adjust(left=.23,right=.97,top=.79,bottom=.20)
fig.text(.08,.94,"真实 ζ 零点在三个窗宽下均给出负读数",fontsize=19,weight='bold',color="#172E42")
fig.text(.08,.875,"紫色实线为精确半格的零值，灰色虚线为同窗随机酉矩阵理论均值（约 −0.400）。",fontsize=11,color="#3E515C")
fig.legend(loc='lower center',bbox_to_anchor=(.53,.065),ncol=3,frameon=False,fontsize=10.5)
fig.text(.08,.028,"横线为均值 ± 2 个分块标准误，仅描述波动。三个高处样本各含 10,000 个零点。数据：Odlyzko。",fontsize=9.5,color="#495864")
fig.savefig(sys.argv[2],dpi=165,facecolor="white")
