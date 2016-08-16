import sys
import numpy as np
from sklearn import datasets
import fnmatch
import os

LABEL_UNDEFINED = 0
LABEL_WALK = 1
LABEL_TROT = 2
LABEL_CANTER = 3
output_fn = sys.argv[1]
# array of files in /training I need to process
input_fn = sys.argv[2:]

# halt walk trot canter
labels = [] 
# feature 1, feature 2 subarrays
data = []
# for file in os.listdir('./training'):
#   if fnmatch.fnmatch(file, '*-features.dat'):
for file in input_fn:
  with open(file, 'r') as dat:
    for line in dat:
      split = line.rstrip().split(' ')
      # print split[4]
      # exit(1)
      # secs/0, z-accel/1, label/2, feat1/3, feat2/4
      labels.append(split[2])
      data.append([split[3], split[4]])

# convert to numpy arrays for wierd syntax below
labels = np.array(labels)
data = np.array(data)

# grab all but the last 500 indices, along with their associated labels / data to train with
labels_train = labels
data_train = data

# create knn classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
  
# train classifier with training data
knn.fit(data_train, labels_train) 

# save out 
from sklearn.externals import joblib   
joblib.dump(knn, output_fn)
# reload the model to test
#knn = joblib.load('model/knn')


