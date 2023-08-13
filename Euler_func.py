# Implementing function for Euler's method, assuming that the v(t) = -9.81*t

import numpy as np
import matplotlib.pyplot as plt
import array as arr

def euler_m(n,t,y,dt):
    n = inp_n
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = inp_t0
    y[0] = inp_y0
    dt = inp_dt

    for i in range(0,n):
        t[i+1] = t[i] + inp_dt
        y[i+1] = y[i] + (-9.81*t[i])*inp_dt

    plt.plot(t, y)
    plt.xlabel("time (seconds)")
    plt.ylabel("height (meters)")
    plt.show()

    return t,y

inp_n = int(input("Enter the value for sub interval: "))
inp_t0 = float(input("Enter initial condition (t0): "))
inp_y0 = float(input("Enter initial condition y[0]: "))
inp_dt = float(input("Enter the time step (dt): "))

t,y = euler_m(inp_n, inp_t0, inp_y0, inp_dt)
