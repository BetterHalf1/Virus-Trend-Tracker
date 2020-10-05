# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:32:13 2020

@author: kenne
"""

import matplotlib.pyplot as plt
import numpy as np


plt.subplot(223)
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")
#Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()



lst = [1, 2, 3, 4, 5, 6, 7]

x = np.arange(0, 10, .1)
y = 2^x

plt.figure()
plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')




# Data for plotting
t = np.arange(0.0, 12.0, 0.01)
s = 2*t


fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()




# np.random.seed(0)

# # Set up x and y variables
# x = np.linspace(-np.pi, np.pi, 256)
# y = np.sin(x)

# # Plot and show
# plt.plot(x, y)
# plt.show()
# # TODO

# # Set axis ticks
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.yticks([-1, 0, 1])

# # Title and labels
# plt.title("f(x) + sin(x)")
# plt.xlabel("x")
# plt.ylabel("f(x)")

# #TODO
# plt.plot(x,y)
# plt.show()

# # Plot and show
# # TODO
