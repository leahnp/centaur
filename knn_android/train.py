import sys
import numpy as np
from sklearn import datasets
import fnmatch
import os

output_fn = sys.argv[1]
if not output_fn:
  print "specify output file"
  exit(1)

# array of files in /training I need to process
input_fn = sys.argv[2:]
if not len(input_fn):
  print "specify input file"
  exit(1)

# halt walk trot canter
labels = [] 
# feature 1, feature 2 subarrays
data = []
# for file in os.listdir('./training'):
#   if fnmatch.fnmatch(file, '*-features.dat'):
for file in input_fn:
  with open(file, 'r') as dat:
    for line in dat:
      # input data is in the format:
      # time, x-accel, y-accel, z-accel, label, time, feature1, time, feature2
      split = line.rstrip().split(' ')
      label = int(split[4])
      feature1 = float(split[6])
      feature2 = float(split[8])
      labels.append(label)
      data.append([feature1, feature2])

# convert to numpy arrays for wierd syntax below
labels = np.array(labels)
data = np.array(data)


# create knn classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
  
# train classifier with training data
knn.fit(data, labels) 

# save out 
from sklearn.externals import joblib   
joblib.dump(knn, output_fn)
# reload the model to test
#knn = joblib.load('model/knn')


