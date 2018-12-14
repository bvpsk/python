import glob
import cv2
a = 'st2.jpg'
img = glob.glob(a)
image = cv2.imread(img[0],1)
cv2.imshow('result',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
