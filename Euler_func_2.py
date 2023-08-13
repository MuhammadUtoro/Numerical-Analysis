# Implementing function for Euler's method using Newton's gravitational model
# For complete explanation see wdflannery_VL01_A.py

import numpy as np
import matplotlib.pyplot as plt
import array as arr

def euler_m(n,t,y,v,dt):
    G = 6.7e-11 # Gravitational Constant
    mEarth = 5.97e24 # Earth's mass
    rEarth = 6.37e6 # Earth's radius
    n = inp_n
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    v = np.zeros(n+1)
    t[0] = inp_t0
    y[0] = inp_y0
    v[0] = inp_v0
    dt = inp_dt

    for i in range(0,n):
        t[i+1] = t[i] + inp_dt
        y[i+1] = y[i] + v[i] * inp_dt
        a = -G*mEarth/(y[i]+rEarth)**2
        v[i+1] = v[i] + a * inp_dt

    plt.plot(t, y)
    plt.xlabel("time (seconds)")
    plt.ylabel("height (meters)")
    plt.show()

    return t,y,v

inp_n = int(input("Enter the value for sub interval: "))
inp_t0 = float(input("Enter initial condition (t0): "))
inp_y0 = float(input("Enter initial condition (y0): "))
inp_v0 = float(input("Enter initial condition (v0): "))
inp_dt = float(input("Enter the time step (dt): "))

t,y,v = euler_m(inp_n, inp_t0, inp_y0, inp_v0, inp_dt)
