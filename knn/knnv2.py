# currently this file is printing portion of prediction data + labeled results to terminal
# need to modify to track labeled data and output 2 graphs, one labeled and one predicted

import numpy as np
from sklearn import datasets

LABEL_UNDEFINED = 0
LABEL_WALK = 1
LABEL_TROT = 2
LABEL_CANTER = 3
KNN_LABELS = []

# load last column (label) from label data into labels array
# load knn labels array with ms and z-accel to use for final output file
labels = [] 
with open('dat/label.dat', 'r') as dat:
  for line in dat:
    split = line.rstrip().split(' ')
    label = float(split[-1])
    ms = float(split[0])
    z_accel = float(split[1])
    labels.append(label)
    KNN_LABELS.append([ms, z_accel])

# push first data into data/feature arrays (mean accel)
data = []
with open('dat/feature1.dat', 'r') as dat:
  for line in dat:
    split = line.rstrip().split(' ')
    v = float(split[1])
    data.append([v, 0.0])

# push second data into data/feature arrays (mean beat length)
with open('dat/feature2.dat', 'r') as dat:
  i = 0
  for line in dat:
    split = line.rstrip().split(' ')
    v = float(split[1])
    data[i][1] = v
    i = i + 1

# generate a random set of indices into the label / data array
#np.random.seed(0)
indices = np.random.permutation(len(data))

# convert to numpy arrays for wierd syntax below
labels = np.array(labels)
data = np.array(data)
# knn_labels_np = np.array(KNN_LABELS)

# grab all but the last 500 indices, along with their associated labels / data to train with
labels_train = labels[indices[:-500]]
data_train = data[indices[:-500]]


# grab the last 500 indices, and their associated labels / data to predict with
expected_labels_test = labels[indices[-500:]]
data_test = data[indices[-500:]]

# create knn classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

# train classifier with training data
knn.fit(data_train, labels_train) 

# try to predict labels for the test data
labels_test = knn.predict(data_test)



for index, label in zip(indices[:-500], labels_test):
  # use indices index to get right data points
  array = KNN_LABELS[index]
  # append generated label to array
  array.append(label)

# write KNN_LABELS to file and fill in un-labeled rows with 4....?
# for line in knn_labels_np:
#   if len(line) == 3:
#     # print ms, z-accel, label
#     print line[0] + ' ' + line[1] + ' ' + line[2] + '\n'
#   else:
#     # print ms, z-accel and holder label '4'
#     print line[0] + ' ' + line[1] + ' ' + '4' + '\n'

# print the predicted labels
# print(labels_test)

# # print the actual labels for the test data
# print(expected_labels_test)
