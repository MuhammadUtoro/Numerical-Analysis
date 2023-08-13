# Continued section to model the atmospheric drag on an apple
# Using the same program with the previous but added more constants 
# They are gravitational constant (G), earth's mass (M), earth radius (R)
# This due to the cause that Newton's Gravitational Equation is Fg = G.Mobject.Mearth/R^2
# Newton's second law states that F = m.a, then we substitute the F with Fg, so in the case with the apple
# G.Mearth.Mapple/R^2 = Mapple.A, A(t) = G.Mearth/(p(t) + R)^2

import numpy as np
import matplotlib.pyplot as plt
import array as arr 

G = 6.7e-11 # Gravitational Constant
mEarth = 5.97e24 # Earth's mass
rEarth = 6.37e6 # Earth's radius

y = np.zeros(5) # Preallocating array to store the y/position value
t = np.zeros(5) # Preallocating array to store the time value
v = np.zeros(5) # Preallocating array to store the velocity value
t[0] = 0 # Initial value
y[0] = 20 # Initial value
v[0] = 0
n = 4 # number of sub-interval
dt = 0.5 # time-step

# for-loop is used to iterate the position at every time 't'
# Remember that in python, in range means that from a number up to n, but not including
for i in range(0,n):
    t[i+1] = t[i] + dt
    y[i+1] = y[i] + v[i] * dt
    a = -G*mEarth/(y[i] + rEarth)**2 # Negative sign because G acting downwards
    v[i+1] = v[i] + a * dt

plt.plot(t,y)
plt.show()