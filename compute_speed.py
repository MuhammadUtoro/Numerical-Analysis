# Comparing computation speed between vectorization and for-loop method for calculating integration
# The calculation using midpoint method
# For a 100.000 iteration, the for-loop approach took around 0.298675 s and for the vectorization method,
# it took only around 0.015625 s

import numpy
import time

def midpoint(f,a,b,n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a+h/2.0)+i*h)
    result *= h
    return result

def midpoint_vec(f,a,b,n):
    h = float((b-a)/n)
    x = numpy.linspace(a+h/2, b-h/2, n)
    return h*sum(f(x))

st = time.process_time()

v = lambda t:3*(t**2)*numpy.exp(t**3)

r1 = midpoint(v,0,1,100000)

et = time.process_time()

dt = et-st

print(dt)
