import numpy as np
import matplotlib.pyplot as plt
import array as arr

# Euler's Method for computing object position at some time 't'
# v(t) = -9.8*t

y = np.zeros(21) # Preallocating array to store the y/position value
t = np.zeros(21) # Preallocating array to store the time value
t[0] = 0 # Initial value
y[0] = 10 # Initial value
n = 20 # number of sub-interval
dt = 0.1 # time-step

# for-loop is used to iterate the position at every time 't'
# Remember that in python, in range means that from a number up to n, but not including
for i in range(0,n):
    t[i+1] = t[i] + dt
    y[i+1] = y[i] + (-10*t[i])*dt

print(t)
plt.plot(t,y)
plt.show()