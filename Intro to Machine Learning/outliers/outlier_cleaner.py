#!/usr/bin/python

import operator

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    new_dicto = {}

    num_to_return = int(round(.9 * len(predictions)))
    print 'Num to return is', num_to_return

    for i in range(len(predictions)):
        new_dicto[i] = predictions[i] - net_worths[i]

    tuples = sorted(new_dicto.items(), key = lambda x:x[1])

    i = 0
    for j, k in tuples:
        cleaned_data.append(tuple((ages[j], net_worths[j], k)))
        i += 1
        if i == num_to_return:
            break

    return cleaned_data
