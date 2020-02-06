# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:00:00 2017
This program analyzes a three column data file and outputs the mean, variance, standard deviation, and standard error.
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

sum = np.sum(data)

mean = sum/length

sum2 = 0

for unit in data:
    print(unit)
    sum2 += (unit - mean)**2

variance = sum2/(length - 1)
std_dev = mt.sqrt(variance)

std_error = std_dev/(mt.sqrt(length))

print("The mean is: ", mean)
print("The variance is: ", variance)
print("The standard deviation is: ", std_dev)
print("The standard error is: ", std_error)