import argparse
import numpy as np
import cv2
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
img = cv2.imread(args['image'])
M = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),45,1)
rotated = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv2.imshow('original',img)
cv2.imshow('rotated',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
