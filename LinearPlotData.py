# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 03:01:16 2017
This program analyzes a three column data file and outputs linear plot of the data with error bars
@author: Mitchell
"""

import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter file name to read')
x,y,z=np.loadtxt(filename, unpack=True, usecols=[0,1,2])

xdata = np.array(x)
ydata = np.array(y)
yerr = np.array(z)

ax = plt.axes()
ax.set_xlabel('y')
ax.set_ylabel('x')
plt.scatter(xdata, ydata)
plt.errorbar(xdata, ydata, yerr, ls="None")

plt.savefig("Linear Plot.png")
plt.show()