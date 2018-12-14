import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10*np.pi,10*np.pi,200,endpoint =True)
c,s=np.cos(x),np.sin(x)

z=[0]*100
t,u,v,ch,hal=[],[],[],[],[]
h=-51
f=[]
for j in range(100):
    h+=1
    f.append(h)
for k in range(200):
    s[k]=s[k]*2
    plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim([-25,25])
ax.set_ylim([-4,4])
h,=ax.plot(x,c,color='red',linewidth=2.0,linestyle='--',label='2*cosine')
h1,=ax.plot(x,s,color='blue',linewidth=2.0,linestyle='-',label='sine')
p,=ax.plot(t,u,color='green',linewidth=1.0,linestyle=':')
p1,=ax.plot(t,v,color='green',linewidth=1.0,linestyle=':')
c,=ax.plot(t,ch,color='green',linewidth=1.0,linestyle=':')
c1,=ax.plot(t,hal,color='green',linewidth=1.0,linestyle=':')
ax.plot(f,z,color='black',linewidth=0.5)
ax.legend(loc='upper right',frameon=True)
la=-51
for r in range(100):
    la+=1
    t.append(la)
for i in np.linspace(-np.pi,np.pi,200):
    for j in range(200):
        x[j]=x[j]-1
    d=np.cos(x)
    q=np.sin(x)
    for k in range(200):
        q[k]=q[k]*3
    l=max(q)
    ku=min(q)
    cha=max(d)
    hall=min(d)
    ch=[cha]*100
    hal=[hall]*100
    u=[l]*100
    v=[ku]*100
    c.set_ydata(ch)
    c.set_xdata(t)
    c1.set_ydata(hal)
    c1.set_xdata(t)
    p1.set_ydata(v)
    p1.set_xdata(t)
    h.set_ydata(d)
    h1.set_ydata(q)
    p.set_xdata(t)
    p.set_ydata(u)
    fig.canvas.draw()
