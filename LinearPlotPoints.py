# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 04:03:42 2017
This program analyzes a two column data file and outputs a linear plot with the points connected by a line
@author: Mitchell
"""

import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter file name to read')
x,y=np.loadtxt(filename, unpack=True, usecols=[0,1])

xdata = np.array(x)
ydata = np.array(y)

ax = plt.axes()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.scatter(xdata, ydata)
plt.plot(xdata, ydata)

plt.savefig('Linear Point Plot.png')
plt.show()