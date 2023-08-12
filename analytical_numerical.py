# checking the numerical and analytical method.
# using the trapezoidal module

import math
import numpy as np
import trapezoidal_module

# This is the numerical method
v = lambda t: 3*(t**2)*math.exp(t**3)
n = 4
num_sol = trapezoidal_module.trapezoidal(v,0,1,n)
print(num_sol)

# This is the analytical method
r = lambda t1: math.exp(t1**3)
exc_sol = r(1) - r(0)
print(exc_sol)

# Calculating the error between analytical vs numerical
print(exc_sol-num_sol)

# However, using more trapezoid (more n) will provide better numerical solution
v1 = lambda t2: 3*(t2**2)*math.exp(t2**3)
n = 400
num_sol = trapezoidal_module.trapezoidal(v,0,1,n)
print(num_sol)

print(exc_sol-num_sol) # result will get lower and lower if we're using more n (trapezoids)