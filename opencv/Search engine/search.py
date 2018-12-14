import numpy as np
import cv2
import glob
import cPickle
f = open('3d data.txt','r')
data = f.read()
index = cPickle.loads(data)
f.close()
query = cv2.imread('got1.jpg',1)
hist = cv2.calcHist([query],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
hist = cv2.normalize(hist,0,256,norm_type = cv2.NORM_MINMAX)
hist = hist.flatten()
eps = 1e-10
result = {}
for (k,features) in index.items():
    d = 0.5*np.sum([((a-b)**2/(a+b+eps)) for (a,b) in zip(features,hist)])
    result[k] = d
result = sorted([(v,k) for (k,v) in result.items()])
a = result[0][1]
img = glob.glob(a)
image = img[0]
img = cv2.imread(image,1)
cv2.imshow(a,img)
cv2.waitKey(0)
cv2.destroyAllWindows()



