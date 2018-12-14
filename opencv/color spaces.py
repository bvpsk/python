import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
(y,x) = image.shape[:2]
image = cv2.resize(image,(x//2,y//2),interpolation = cv2.INTER_AREA)
cv2.imshow('rgb original',image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow('l*a*b',lab)
cv2.waitKey(0)
cv2.destroyAllWindows()