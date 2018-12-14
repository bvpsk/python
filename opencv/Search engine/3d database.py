import cv2
import glob
import cPickle
index = {}
for image in glob.glob('*.jpg'):
    img = cv2.imread(image,1)
    hist = cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
    hist = cv2.normalize(hist,0,256,norm_type = cv2.NORM_MINMAX)
    index[image] = hist.flatten()
for image in glob.glob('*.jpeg'):
    img = cv2.imread(image,1)
    hist = cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
    hist = cv2.normalize(hist,0,256,norm_type = cv2.NORM_MINMAX)
    index[image] = hist
f = open('3d data.txt','w')
f.write(cPickle.dumps(index))
f.close()
