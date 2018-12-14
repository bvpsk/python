import numpy as np
import cv2
canvas = np.zeros((300,300,3),dtype = 'uint8')
cv2.line(canvas,(0,0),(300,300),(0,255,0),2)
cv2.line(canvas,(0,300),(300,0),(0,0,255),3)
cv2.rectangle(canvas,(10,10),(70,70),(128,0,0),3)
cv2.rectangle(canvas,(100,100),(200,200),(0,255,255),-1)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
