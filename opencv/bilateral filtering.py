import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow('blurred',np.hstack([cv2.bilateralFilter(image,10,51,51),cv2.bilateralFilter(image,12,81,81)]))
cv2.waitKey(0)
cv2.destroyAllWindows()