import numpy as np
import matplotlib.pyplot as plt
import array as arr

# In this part, the implementation of newton's gravity model will be combined with atmospheric drag
# so, rather than using the constant gravity of -9.8 as followed a(t) = -10+Cd*dair*v^2*Cs/2/Mapple, 
# a(t) = -G*mEarth/(ydrag[i]+rEarth)**2+Cd*dair*vdrag[i]**2*Cs/2/Mapple. 
# where Cd = drag coefficient, dair = air density, Cs = cross-sectional area and v = velocity
# in this section, the function will be implemented
# and compare the result with the constant gravity model
# in the code, variables ydrag and vdrag are used to store the value of the model considering atm. drag,
# so later we can compare the result

def euler_m(n,t,y,ydrag,vdrag,dt):
    Cd = 0.5
    dair = 1.4
    Cs = np.pi*(0.01)**2
    Mapple = 0.2
    G = 6.7e-11 # Gravitational Constant
    mEarth = 5.97e24 # Earth's mass
    rEarth = 6.37e6 # Earth's radius
    n = inp_n
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    v = np.zeros(n+1)
    ydrag = np.zeros(n+1)
    vdrag = np.zeros(n+1)

    t[0] = inp_t0
    y[0] = inp_y0
    v[0] = inp_v0
    ydrag[0] = inp_ydrag
    vdrag[0] = inp_vdrag
    dt = inp_dt

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

    return t,y,ydrag,v,vdrag

inp_n = inp_n = int(input("Enter the value for sub interval: "))
inp_t0 = float(input("Enter initial condition (t0): "))
inp_y0 = float(input("Enter initial condition y[0]: "))
inp_v0 = float(input("Enter initial condition v[0]: "))
inp_ydrag = float(input("Enter initial condition for ydrag: "))
inp_vdrag = float(input("Enter initial condition vdrag: "))
inp_dt = float(input("Enter the time step (dt): "))

t,y,ydrag,v,vdrag = euler_m(inp_n, inp_t0, inp_y0, inp_ydrag, inp_vdrag, inp_dt)

plt.plot(t,v,'b-',t,vdrag,'r-')
plt.show()