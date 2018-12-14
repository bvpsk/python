import matplotlib.pyplot as plt
import numpy as np
plt.ion()
x=np.linspace(-np.pi,np.pi,200)
y=np.sin(x)
fig=plt.figure()
ax=fig.add_subplot(111)
line1,=ax.plot(x,y)
for i in np.linspace(-np.pi,np.pi,200):
    line1.set_ydata(np.sin(0.5*x+i))
    fig.canvas.draw()
