import numpy as np
import cv2
from random import randint as r
canvas = np.zeros((600,600,3),dtype = 'uint8')
for ra in range(5,250,20):
    cv2.circle(canvas,(r(0,600),r(0,600)),ra,(r(0,255),r(0,255),r(0,255)),-1)
cv2.imshow('abstract circles',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
