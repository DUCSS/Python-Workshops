#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    counts = [0] * 201
    count = 0
    for index in range(0, len(expenditure)):
        if index >= d:
            prefix_sum = 0
            median_1 = -1
            median_2 = -1
            for j in range(0, 201):
                prefix_sum = prefix_sum + counts[j]
                
                if d%2 == 0:
                    if median_1 == - 1 and prefix_sum - 1 >= int(d/2) - 1:
                        median_1 = j
                    if median_2 == -1 and prefix_sum - 1 >= int(d/2):
                        median_2 = j
                        break
                else:
                    if prefix_sum - 1 >= int(d/2):
                        median_1 = j
                        break
                    
            median = -1
            if d%2 == 0:
                median = (median_1 + median_2)/2.0
            else:
                median = median_1
                
            if median * 2 <= expenditure[index]:
                count = count + 1
                
        if index - d >=0:
            counts[expenditure[index - d]] =  counts[expenditure[index - d]] - 1

        counts[expenditure[index]] =  counts[expenditure[index]] + 1
    return count
        
        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
