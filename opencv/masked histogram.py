import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
mask = np.zeros(image.shape[:2],dtype = 'uint8')
cv2.rectangle(mask,(202,0),(380,180),255,-1)
masked = cv2.bitwise_and(image,image,mask = mask)
#fig = plt.figure()
#ax = fig.add_subplot(121)
chans = cv2.split(masked)
colors = ('b','g','r')
for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],mask,[256],[0,256])
    plt.plot(hist,color = color)
cv2.imshow('original',image)
cv2.imshow('masked',masked)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()