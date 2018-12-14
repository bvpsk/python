import numpy as np
import cv2
import argparse
import mahotas
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'],0)
image = cv2.resize(image,(517,401),interpolation = cv2.INTER_AREA)
blurred = cv2.GaussianBlur(image,(5,5),0)
(T,thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow('binary',np.hstack([thresh,cv2.bitwise_and(image,image,mask = thresh)]))
thresh= cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,5)
cv2.imshow('mean c',np.hstack([thresh,cv2.bitwise_and(image,image,mask = thresh)]))
thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,13,3)
cv2.imshow('gaussian c',np.hstack([thresh,cv2.bitwise_and(image,image,mask = thresh)]))
t = mahotas.thresholding.otsu(blurred)
print 'otsu : {}'.format(t)
thresh = image.copy()
thresh[thresh>t] = 255
thresh[thresh<255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('otsu',np.hstack([thresh,cv2.bitwise_and(image,image,mask = thresh)]))
t = mahotas.thresholding.rc(blurred)
print 'rc : {}'.format(t)
thresh = image.copy()
thresh[thresh>t] = 255
thresh[thresh<255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('rc',np.hstack([thresh,cv2.bitwise_and(image,image,mask = thresh)]))
cv2.waitKey(0)
cv2.destroyAllWindows()