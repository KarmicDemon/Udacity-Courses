#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys

sys.path.append("../tools/")

from time import time
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = svm.SVC(kernel='rbf', C=10000.0)
print clf.kernel

### used to determine speed of svm
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "Time to finish training:", time() - t0, "s"

t0 = time()
score = clf.score(features_test, labels_test)
print "Time to finish scoring:", time() - t0, "s"

print "Accuracy Score:", score

pred = clf.predict(features_test)
num_chris = 0

for num in pred:
    if num == 1:
        num_chris += 1

print "Number belonging to Chris", num_chris

'''
print "Element 10 of test result is", clf.predict(features_test[10])
print "Element 26 of test result is", clf.predict(features_test[26])
print "Element 50 of test result is", clf.predict(features_test[50])
'''
