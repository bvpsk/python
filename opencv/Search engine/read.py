import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import cPickle
import glob
import cv2
f = open('database.txt','r')
data = f.read()
index = cPickle.loads(data)
f.close()
plt.figure()
plt.title('testing')
for (k,i) in index.items():
    hist = i
    plt.plot(hist)
plt.show()
