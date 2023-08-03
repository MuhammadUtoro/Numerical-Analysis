import numpy as np
import matplotlib.pyplot as plt
import array as arr

# In this part, two different approaches to calculate the a(t) will be compared.
# First is the constant gravity model and drag model
# a(t) = -10+Cd*dair*v^2*Cs/2/Mapple, Cd = drag coefficient, dair = air density, Cs = cross-sectional area
# and v = velocity

Cd = 0.5
dair = 1.4
Cs = np.pi*(0.01)**2
Mapple = 0.2
G = 6.7e-11 # Gravitational Constant
mEarth = 5.97e24 # Earth's mass
rEarth = 6.37e6 # Earth's radius
n = 250
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
dt = 0.04

for i in range(0,n):
    t[i+1] = t[i] +dt
    y[i+1] = y[i] + v[i] *dt
    a = -G*mEarth/(y[i]+rEarth)**2
    v[i+1] = v[i] + a *dt
    ydrag[i+1] = ydrag[i] + vdrag[i] *dt
    adrag = -10+Cd*dair*vdrag[i]**2*Cs/2/Mapple
    vdrag[i+1] = vdrag[i] + adrag *dt

plt.plot(t,y,'r-',t,ydrag,'b-')
plt.show()