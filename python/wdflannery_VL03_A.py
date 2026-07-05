# In this part, the implementation of newton's gravity model will be combined with atmospheric drag
# so, rather than using the constant gravity of -9.8 as followed a(t) = -10+Cd*dair*v^2*Cs/2/Mapple, 
# a(t) = -G*mEarth/(ydrag[i]+rEarth)**2+Cd*dair*vdrag[i]**2*Cs/2/Mapple. 
# where Cd = drag coefficient, dair = air density, Cs = cross-sectional area and v = velocity

import numpy as np
import matplotlib.pyplot as plt
import array as arr

Cd = 0.5
dair = 1.4
Cs = np.pi*(0.01)**2
Mapple = 0.2
G = 6.7e-11 # Gravitational Constant
mEarth = 5.97e24 # Earth's mass
rEarth = 6.37e6 # Earth's radius
n = 700
t = np.zeros(n+1)
y = np.zeros(n+1)
v = np.zeros(n+1)
ydrag = np.zeros(n+1)
vdrag = np.zeros(n+1)

t[0] = 0
y[0] = 1000
v[0] = 0
ydrag[0] = 1000
vdrag[0] = 0
dt = 0.02

for i in range(0,n):
    t[i+1] = t[i] +dt
    y[i+1] = y[i] + v[i] *dt
    a = -G*mEarth/(y[i]+rEarth)**2
    v[i+1] = v[i] + a *dt
    ydrag[i+1] = ydrag[i] + vdrag[i] *dt
    adrag = -G*mEarth/(ydrag[i]+rEarth)**2+Cd*dair*vdrag[i]**2*Cs/2/Mapple
    vdrag[i+1] = vdrag[i] + adrag *dt

plt.plot(t,ydrag,'r-',t,y,'b-')
plt.show()