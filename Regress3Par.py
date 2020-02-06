# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 04:49:32 2017
This program analyzes a three column data file and outputs a Chi square model of the form y = a + bx + cx^2
@author: Mitchell
"""

import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter file name to read')
x,y,sigma = np.loadtxt(filename, unpack=True, usecols=[0,1,2])
minimum = np.min(x)
maximum = np.max(x)
xlinear = np.linspace(minimum, maximum, 1000)

dc1 = sum(1/sigma**2)
dc2 = sum(x/sigma**2)
dc3 = sum(x**2/sigma**2)
dc4 = sum(x**3/sigma**2)
dc5 = sum(x**4/sigma**2)

ac1 = sum(y*1/sigma**2)
ac2 = sum(y*x/sigma**2)
ac3 = sum (y*x**2/sigma**2)

Delta = ([dc1, dc2, dc3], [dc2, dc3, dc4], [dc3, dc4, dc5])
Transform = ([ac1, ac2, ac3])
Delta_inv = np.linalg.inv(Delta)

Result = np.dot(Delta_inv,Transform)

Chi = sum(1/sigma**2*(y-Result[2]*x**2 - Result[1]*x - Result[0])**2)
Red_Chi = Chi/len(x)

print('a = ', Result[0], '+/-', sum(1/sigma**2))
print('b = ', Result[1], '+/-', sum(x**2/sigma**2))
print('c = ', Result[2], '+/-', sum(x**4/sigma**2))
print('Chi Squared = ', Chi)
print('Reduced Chi Squared = ', Red_Chi)

plt.scatter(x,y)
plt.errorbar(x,y,sigma, ls='None')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(xlinear, Result[2]*xlinear**2 + Result[1]*xlinear + Result[0])
plt.show()