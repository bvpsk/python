import matplotlib
matplotlib.use('TkAgg')
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())
img = cv2.imread("ironman.png",0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure()
cv2.imshow('gray',img)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])
#plt.ylim([-100,500])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
