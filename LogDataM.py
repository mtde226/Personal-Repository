# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 02:46:38 2017
This program analyzes a two column data file that intakes the data and transforms it into a logarithmic output
@author: Mitchell
"""

import numpy as np

filename = input('Enter file name to read')
x,y=np.loadtxt(filename,unpack=True, usecols=[0,1])


data_array = np.array(x)
error_array = np.array(y)
new_array = np.log(data_array)
new_error = (error_array)/(data_array)


print(new_array)
print(new_error)