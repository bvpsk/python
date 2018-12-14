import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True)
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
M  = np.float32([[1,0,30],[0,1,30]])
shifted = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
M = np.float32([[1,0,-30],[0,1,-30]])
s = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv2.imshow('shiffted',s)
cv2.imshow('original',img)
cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
