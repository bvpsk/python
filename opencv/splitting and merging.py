import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
(b,g,r) = cv2.split(image)
cv2.imshow('red',r)
cv2.imshow('blue',b)
cv2.imshow('green',g)
(x,y) = image.shape[:2]
zeros = np.zeros((x,y),dtype = 'uint8')
cv2.imshow('complete red',cv2.merge([zeros,zeros,r]))
cv2.imshow('complete green',cv2.merge([zeros,g,zeros]))
cv2.imshow('complete blue',cv2.merge([b,zeros,zeros]))
cv2.imshow('merged',cv2.merge([b,g,r]))
cv2.waitKey(0)
cv2.destroyAllWindows()
