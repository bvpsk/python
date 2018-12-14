import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow('blurred',np.hstack([cv2.blur(image,(3,3)),cv2.blur(image,(5,5)),cv2.blur(image,(7,7))]))
cv2.waitKey(0)
cv2.destroyAllWindows()