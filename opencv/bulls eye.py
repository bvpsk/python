import numpy as np
import cv2
canvas = np.zeros((300,300,3),dtype = 'uint8')
for r in range(0,175,25):
    cv2.circle(canvas,(150,150),r,(255,255,255))
cv2.imshow('bulls eye',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
