import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'],0)
eq = cv2.equalizeHist(image)
cv2.imshow('hist equalization',np.vstack([image,eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()
