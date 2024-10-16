#!/usr/bin python3

from math import exp
import matplotlib.pyplot as plt
import numpy as np

t0 = 0.0 # starting time
tf = 10.0 # finishing time
h = 0.1 # step

t = []
for x in range(0, int(tf / h)): # time list
	t.append(x)

# Our functions 
def actualY(a):
	return -exp(a)
def y(a):
	return -5.74 * exp(a) + 5.74
def dy(a):
	return -5.74 * exp(a)

# Our list of values
yReal = []
yEst = []
yEst.append(0) # IC of the DE

for x in range(0, len(t)):
	yReal.append(actualY(t[x]))
	yInt = yEst[x] + h * dy(t[x])
	yEst.append(yEst[x] + (h / 2) * (dy(t[x]) + dy(t[x] + h)))

""" 
These next 2 lines are necessary for the x and y values to 
match in dimension. The two lines just add one more value at
the end.
"""

yReal.append(actualY(tf / h + 1)) 
t.append(len(t) + 1)

plt.close('all')
# Plots top left Euler method for y-value
plt.subplot(221)
plt.plot(t, yEst, 'b-')
plt.title('Euler method')
plt.ylabel('y-value')

# Plots top right Real y-value
plt.subplot(222)
plt.plot(t, yReal, 'r')
plt.title('Real Function')
plt.xlabel('time t')
plt.ylabel('y-value')

# Plots bottom left Euler method for x-value
plt.subplot(223)
plt.plot([1, 2, 3, 4], [5, 6, 7, 8], 'm')
plt.ylabel('x-value')

# Plots bottom right Real x-value
plt.subplot(224)
plt.plot([4, 3, 2, 1], [8, 7, 6, 5], 'g')
plt.ylabel('x-value')

plt.show()
