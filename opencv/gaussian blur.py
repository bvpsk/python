import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow('blurred',np.hstack([cv2.GaussianBlur(image,(3,3),0),cv2.GaussianBlur(image,(5,5),0),cv2.GaussianBlur(image,(7,7),0)]))
cv2.waitKey(0)
cv2.destroyAllWindows()