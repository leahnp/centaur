import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib 

# reload the model to test
knn = joblib.load('model/knn')
data = []
rebuild = []

with open('predict/general-632478-features.dat', 'r') as dat:
# with open('training/canter-1359889-features.dat', 'r') as dat:
  for line in dat:
    split = line.rstrip().split(' ')
    # # secs/0, z-accel/1, label/2, feat1/3, feat2/4
    rebuild.append([split[0], split[3]])

    data.append([float(split[6]), float(split[8])])

data = np.array(data)

# # try to predict labels for the test data
labels_test = knn.predict(data)
labels_probability = knn.predict_proba(data)
# print len(labels_test)
# print len(data)

# check probability
# if max value is 

for i, label, proba in zip(rebuild, labels_test, labels_probability):
  print str(i[0]) + ' ' + str(i[1]) + ' ' + str(label) + ' ' + str(proba)
