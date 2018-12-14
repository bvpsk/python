import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
img = np.ones(image.shape,dtype = 'uint8')*100
whiten = cv2.subtract(image,img)
cv2.imshow('original',image)
cv2.imshow('whiten',whiten)
cv2.waitKey(0)
cv2.destroyAllWindows()
