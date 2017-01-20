#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).
    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import math
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

num_no_pay = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN' \
        and enron_data[key]['poi'] > 0:
        num_no_pay += 1

print "People with no pay:", num_no_pay

'''
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
'''
