import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('ironman.png',1)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('3D Histogram')
hist = cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
p = ax.imshow(hist,interpolation = 'nearest')
plt.colorbar(p)
plt.show()
