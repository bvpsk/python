import matplotlib
from random import randint as r
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
x=np.linspace(-np.pi,np.pi,200)
c,s=np.cos(x),np.sin(x)
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
l,=ax.plot(x,c)
li,=ax.plot(x,s)
ax.set_ylim([-3.0,3.0])
class Index:
    def cosi(self,event):
        a=r(0,10)
        x=np.linspace(-a*np.pi,a*np.pi,200)
        c=np.cos(x)
        s=np.sin(x)
        for i in range(200):
            c[i]=c[i]*2
        l.set_ydata(c)
        li.set_ydata(s)
        fig.canvas.draw()
    def sini(self,event):
        a=r(0,10)
        x=np.linspace(-a*np.pi,a*np.pi,200)
        s=np.sin(x)
        c=np.cos(x)
        for i in range(200):
            s[i]=s[i]*2
        li.set_ydata(s)
        l.set_ydata(c)
        fig.canvas.draw()
callback = Index()
axsini = plt.axes([0.7, 0.05, 0.1, 0.075])
axcosi = plt.axes([0.81, 0.05, 0.1, 0.075])
bcosi = Button(axcosi, 'COS')
bcosi.on_clicked(callback.cosi)
bsini = Button(axsini, 'SIN')
bsini.on_clicked(callback.sini)
