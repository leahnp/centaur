import sys
import numpy as np
from sklearn import datasets
import fnmatch
import os

if len(sys.argv) < 2:
  print "specify output file"
  exit(1)

output_fn = sys.argv[1]

# array of files in /training I need to process
if len(sys.argv) < 3:
  print "specify input file(s)"
  exit(1)

input_fn = sys.argv[2:]

# halt walk trot canter
labels = [] 
# feature 1, feature 2 subarrays
features = []
# for file in os.listdir('./training'):
#   if fnmatch.fnmatch(file, '*-features.dat'):
for file in input_fn:
  with open(file, 'r') as dat:
    for line in dat:
      # input data is in the format:
      # time, x-accel, y-accel, z-accel, label, time, feature1, time, feature2
      split = line.rstrip().split(' ')
      labels.append(int(split[4]))
      features.append([float(split[6]), float(split[8]), float(split[10])])

# convert to numpy arrays for wierd syntax below
labels = np.array(labels)
features = np.array(features)

# create knn classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
  
# train classifier with training data
knn.fit(features, labels) 

# save out 
from sklearn.externals import joblib   
joblib.dump(knn, output_fn)


