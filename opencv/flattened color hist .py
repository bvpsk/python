import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('ironman.png',1)
chans = cv2.split(img)
colors = ('b','g','r')
plt.figure()
plt.title('flattened color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
features = []
for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    features.append(hist)
    plt.plot(hist , color = color)
plt.xlim([0,256])
plt.show()
