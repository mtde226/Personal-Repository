# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 03:31:56 2017
This program analyzes a three column data file and outputs a logarithmic plot of the data
@author: Mitchell
"""

import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter file name to read')
x,y,z=np.loadtxt(filename, unpack=True, usecols=[0,1,2])

xdata = np.array(x)
ydata = np.array(y)
yerr = np.array(z)

ytransform = np.log(ydata)

ax = plt.axes()
ax.set_ylabel('ln(y)')
ax.set_xlabel('x')
plt.scatter(xdata, ydata)
plt.errorbar(xdata, ydata, yerr, ls="None")

plt.savefig("Linear Transformation Plot.png")
plt.show()