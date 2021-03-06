# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 04:49:31 2017
This program analyzes a three column data file and outputs a Chi square model of the form y = a + bx
@author: Mitchell
"""

import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter file name to read')
x,y,sigma = np.loadtxt(filename, unpack=True, usecols=[0,1,2])
minimum = np.min(x)
maximum = np.max(x)
xlinear = np.linspace(minimum, maximum, 1000)

delta = sum(1/sigma**2)*sum(x**2/sigma**2) -(sum(x/sigma**2))**2
a = 1/delta*(sum(x**2/sigma**2)*sum(y/sigma**2)-sum(x/sigma**2)*sum(x*y/sigma**2))
b = 1/delta*(sum(1/sigma**2)*sum(x*y/(sigma**2)) - sum(x/sigma**2)*sum(y/sigma**2)) 

Chi = sum(1/sigma**2*(y-b*x-a)**2)
Red_Chi = Chi/(len(x)-2)

print('a = ', a, '+/-', np.sqrt(1/delta*sum(x**2/sigma**2)))
print('b = ', b, '+/-', np.sqrt(1/delta*sum(1/sigma**2)))
print('Chi Squared = ', Chi)
print('Reduced Chi Squared = ', Red_Chi)


plt.scatter(x,y)
plt.errorbar(x,y,sigma, ls='None')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(xlinear, a + b*xlinear)
plt.show()