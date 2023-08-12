# Using midpoint method to calculate integration
# Compare it with the analytical solution

import math
import numpy
import trapezoidal_module

def midpoint(f,a,b,n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a+h/2.0)+i*h)
    result *= h
    return result

v = lambda t:3*(t**2)*math.exp(t**3)
n = int(input('n: '))

# Exact solution
exc = lambda t1:math.exp(t1**3)
exc_sol = exc(1) - exc(0)

mid_point = midpoint(v,0,2,n)
traps = trapezoidal_module.trapezoidal(v,0,2,n)

err_mid = mid_point - exc_sol
err_traps = traps - exc_sol

print(err_mid)
print(err_traps)