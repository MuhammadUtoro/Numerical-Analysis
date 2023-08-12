# Using vectorization with midpoint method to calculate integration

import numpy

def midpoint_vec(f,a,b,n):
    h = float((b-a)/n)
    x = numpy.linspace(a+h/2, b-h/2, n)
    return h*sum(f(x))

v = lambda t:3*(t**2)*numpy.exp(t**3)

mdpt_vec = midpoint_vec(v,0,1,10)

print(mdpt_vec)

def trapezoidal_vec(f,a,b,n):
    h = float((b-a)/n)
    x = numpy.linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

trp_vec = trapezoidal_vec(v,0,1,10)

print(trp_vec)
