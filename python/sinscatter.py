from matplotlib.pyplot import ion,xlim,ylim,scatter,pause,plot,show,draw
import numpy as np
import math
ion()
xlim(0.0,20.9)
ylim(-1.5,1.5)
b=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c=[0]*21
plot(b,c)
for i in range(21):
    a=1
    while a<=5:
        j=i+(i/a)
        k=np.sin(j)
        scatter(j,k)
        pause(0.005)
        a+=1

    d=np.sin(i)
    scatter(i,d)
    pause(0.05)

while True:
    pause(0.005)
