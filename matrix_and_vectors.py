# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 11:26:16 2016

@author: francesco
"""
"""matrixes and vectors"""
matrix = np.asarray([
    [1, 2, 0, 7],
    [0, 3, 3, 11],
    [1, 2, 2, 11]
], dtype=np.float32)
print(matrix)
""" matrix[[0,2]] = matrix[[2,0]]
 will exchange the first and the third rows."""
matrix[[0,2]] = matrix[[2,0]]
print(matrix)
"""plot 1 vectors"""
X=0.0
Y=0.0
U=3.0
V=5.0
import numpy as np
import matplotlib.pyplot as plt
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
# Set the x axis limits
plt.xlim([0,6])
# Set the y axis limits
plt.ylim([0,6])
# Show the plot.
plt.show()
""" plot 2 vectors"""
X=[0.0,1.0]
Y=[0.0,2.0]
U=[2.0,1.0]
V=[5.0,6.0]
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
# Set the x axis limits
plt.xlim([0,10])
# Set the y axis limits
plt.ylim([0,10])
# Show the plot.
plt.show()
"""matrix multiplications"""
A = np.asarray([[5,2], [3,5], [6,5]])
B = np.asarray([[3,1], [4,2]])
C=np.dot(A,B)
print(C)