 #!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import numpy as np
import sys

sys.path.append("../tools/")

from email_preprocess import preprocess
from time import time
from sklearn import tree

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split = 40)

t0 = time()
clf.fit(features_train, labels_train)
print "Time to train", time() - t0, "s"

t1 = time()
score = clf.score(features_test, labels_test)
print "Time to predict", time() - t1, "s"
print "Accuracy Score:", score
print "Number of features:", len(features_test[0])
