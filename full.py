import matplotlib
matplotlib.use('TkAgg')
from matplotlib.widgets import Button
from random import randint as r
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-np.pi,np.pi,200)
c,s=np.cos(x),np.sin(x)
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
l,=ax.plot(x,c)
li,=ax.plot(x,s)
a=-1.0
b=1.0
ax.set_xlim([a,b])
class Index:
    def x_up(self,event):
        a=r(1,10)
        b=r(1,10)
        ax.set_xlim([a,b])
        fig.canvas.draw()
    def x_down(self,event):
        a=r(1,10)
        b=r(1,10)
        ax.set_xlim([a,b])
        fig.canvas.draw()
callback=Index()
axup=plt.axes([0.6,0.05,0.1,0.075])
axdown=plt.axes([0.81,0.05,0.1,0.075])
bup=Button(axup,'UP')
bup.on_clicked(callback.x_up)
bdown=Button(axdown,'DOWN')
bdown.on_clicked(callback.x_down)
