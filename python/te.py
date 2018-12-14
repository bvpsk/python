import matplotlib.pyplot as plt
import numpy as np
x,y=[],[]
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
h1,=ax.plot(x,y,color='red',linestyle='--')
ax.set_ylim([0,50])
ax.set_xlim([0,50])
j=0
k=50
for i in range(250):
    if i>50:
        j+=1
        k+=1
        ax.set_xlim([j,k])
        ax.set_ylim([j,k])
    x.append(i)
    y.append(i)
    h1.set_ydata(y)
    h1.set_xdata(x)
    fig.canvas.draw()
