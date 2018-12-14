import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
img = cv2.imread(args['image'])
resized = cv2.resize(img,(64,64),interpolation = cv2.INTER_AREA)
cv2.imwrite('resized.jpg',resized)
cv2.imshow('original',img)
cv2.imshow('resized',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()