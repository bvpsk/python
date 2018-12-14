import glob
import cv2
import cPickle
index = {}
for img in glob.glob('*.jpg'):
    image = cv2.imread(img,0)
    hist = cv2.calcHist([image],[0],None,[256],[0,256])
    index[img] = hist
for img in glob.glob('*.jpeg'):
    image = cv2.imread(img,0)
    hist = cv2.calcHist([image],[0],None,[256],[0,256])
    index[img] = hist
print index
f = open('database.txt','w')
f.write(cPickle.dumps(index))
f.close()
