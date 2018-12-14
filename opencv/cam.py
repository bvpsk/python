import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    r,frame = cap.read()
    cv2.imshow('our live sketcher',frame)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
