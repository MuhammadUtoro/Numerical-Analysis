# Orbits. two-body problem in 2D. Modelling orbital motion

# Initializing constants and allocating state variables
# The space station orbits the earth with altitude of 402 km, velocity of 7706 m/s and period of 96 minutes
# In this case, the accuracy of the orbit depends on the length of sub-interval, as does other problems
# smaller the dt will result in more accurate (it will be almost exactly circular plot) therefore the 
# number of sub-interval must also be high.

import numpy as np
import matplotlib.pyplot as plt

rEarth = 6.378e6 # Earth's radius
mEarth = 5.9742e24 # Earth's mass
gEarth = 6.7e-11 # Earth's gravitational constant
xE = np.zeros(225601)
yE = np.zeros(225601)
px = np.zeros(225602)
py = np.zeros(225602)
vx = np.zeros(225602)
vy = np.zeros(225602)
t = np.zeros(225602)
t[0] = 0
px[0] = rEarth + 402000
py[0] = 0
vx[0] = 0
vy[0]= 7706
dt = 0.25 # length of the sub-interval
n = 225601 # number of sub-interval

# Calculating the orbit
for i in range(0,n):
    t[i+1] = t[i] +dt
    px[i+1] = px[i] + vx[i] *dt
    py[i+1] = py[i] + vy[i] *dt
    R = np.sqrt(px[i]**2+py[i]**2)
    Ag = -gEarth*mEarth/R**2
    vx[i+1] = vx[i] + Ag * px[i]/R *dt
    vy[i+1] = vy[i] + Ag * py[i]/R *dt
    ang = 2*np.pi*i/225600
    xE[i] = rEarth*np.cos(ang)
    yE[i] = rEarth*np.sin(ang)

plt.plot(px,py,'r-',xE,yE)
plt.show()
