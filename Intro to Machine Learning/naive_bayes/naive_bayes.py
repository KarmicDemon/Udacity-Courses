#!/usr/bin/python

"""
    Using a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
import numpy as np

sys.path.append("../tools/")

from time import time
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t0 = time()
hello = clf.score(features_test, labels_test)
print "scoring time:", round(time() - t0, 3), "s"

print hello

#########################################################
### your code goes here ###


#########################################################
