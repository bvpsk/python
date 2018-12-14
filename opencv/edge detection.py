import cv2
import numpy as np
import argparse
import mahotas
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'],0)
image = cv2.resize(image,(517,401),interpolation = cv2.INTER_AREA)
lap = cv2.Laplacian(image,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
sobelx = np.uint8(np.absolute(cv2.Sobel(image,cv2.CV_64F,1,0)))
sobely = np.uint8(np.absolute(cv2.Sobel(image,cv2.CV_64F,0,1)))
sobel = cv2.bitwise_or(sobelx,sobely)
blurred = cv2.GaussianBlur(image,(5,5),0)
canny = cv2.Canny(blurred,30,150)
cv2.imshow('canny',canny)
cv2.imshow('sobel',sobel)
cv2.imshow('Laplacian',lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
