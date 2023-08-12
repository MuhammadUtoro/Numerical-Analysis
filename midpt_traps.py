# Comparing trapezoidal and midpoint method
# the function is y = e^-y^2

import math

def mdpt(f,a,b,n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a+h/2.0)+i*h)
    result *= h
    return result

def trpz(f,a,b,n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1,n):
        result += f(a + i*h)
    result *= h
    return result


f = lambda t:math.exp(-t**2)
a = 0
b = 2

for i in range(1,11):
    n = 2**i
    mdpt_sol = mdpt(f,a,b,n)
    trp_sol = trpz(f,a,b,n)
    print(mdpt_sol)
    print(trp_sol)