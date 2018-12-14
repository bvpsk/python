import matplotlib
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
def cos():
    x=np.linspace(-np.pi,np.pi,200)
    c=np.cos(x)
    s=np.sin(x)
    for i in range(200):
        c[i]=c[i]*2
    l.set_ydata(c)
    li.set_ydata(s)
    plt.draw()
def sin():
    x=np.linspace(-np.pi,np.pi,200)
    s=np.sin(x)
    c=np.cos(x)
    for i in range(200):
        s[i]=s[i]*2
    li.set_ydata(s)
    l.set_ydata(c)
    plt.draw()

axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
while(1==1):
    bcos=Button(axprev,'cos')
    bcos.on_clicked(cos())
    bsin=Button(axnext,'sin')
    bsin.on_clicked(sin())
