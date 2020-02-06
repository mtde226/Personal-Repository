# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:56:27 2017
This program analyzes a three column data file and outputs the weighted mean of the data
@author: Mitchell
"""

import numpy as np
import math as mt

filename = input('Enter file name to read')
data_file = open(filename, 'r')
count = 0
#length = int(input('Enter number of trials'))
length = int(data_file.readline())
data = np.zeros(length)

with open(filename) as f:
    next(f)
    for line in f:
        data[count] = float(line)
        count += 1

filename = input('Enter second file name to read')
data_file = open(filename, 'r')
count = 0
#length = int(input('Enter number of trials'))
length = int(data_file.readline())
unc = np.zeros(length)

with open(filename) as f:
    next(f)
    for line in f:
        unc[count] = float(line)
        count += 1

array1 = np.zeros(length) #for the mu/sigma^2
array2 = np.zeros(length) #for the 1/sigma^2
count1 = 0;
for x in array1:
    array1[count1] = data[count1]/(unc[count1]**2)
    array2[count1] = 1/(unc[count1]**2)
    count1 += 1


mean = np.sum(array1)/np.sum(array2)
variance = 1/np.sum(array2)

std_dev = mt.sqrt(variance)
std_error = std_dev/(mt.sqrt(length))

print("The mean is",mean)
print("The standard deviation is",std_dev)
