import sys
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib

if len(sys.argv[1]) < 2:
  print "specify model file"
  exit(1)

model_filename = sys.argv[1]

# load data from stdin
samples = []
features = []

for line in sys.stdin:
  split = line.rstrip().split(' ')
  samples.append([float(split[0])])  
  features.append([float(split[6]), float(split[8]), float(split[10])])

# convert to numpy array
features = np.array(features)

# try to predict labels for the test data
knn = joblib.load(model_filename)
proba = knn.predict_proba(features)

for sample, p in zip(samples, proba):
	print '%f %f %f %f' % (sample[0], p[0], p[1], p[2])