import cv2
import numpy
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True)
args = vars(ap.parse_args())
img = cv2.imread(args['image'])
img = img[:len(img)/6]
cv2.imshow('img',img)
while cv2.waitKey(33) != 27:
    pass
cv2.imwrite("en1.png",img)
cv2.destroyAllWindows()
