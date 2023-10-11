# in this practice session, the task is to approximate the derivative value of a function (sin(x)) using the
# 2nd order approximation. In the lesson, it is shown that using the 1st order approximation resulting in 
# inaccurate approximation compared to the exact value

import numpy as np
import math
import matplotlib
from matplotlib import pyplot as mplot

a = (np.pi/2)-0.35
b = (np.pi/2)+0.15
fa = np.sin(a)
fb = np.sin(b)
ex_val = np.cos(a)
deltaX = b-a
frst_order = (fb - fa)/deltaX

error = (np.abs((frst_order-ex_val)/ex_val))*100

# now we implement the difference formula to estimate the first derivative
# f'(a) = (-3*f(a) + 4*f(a+deltaX) - f(a+2*deltaX))/2*deltaX

scnd_order = (4*(np.sin(a+deltaX)) - 3*(np.sin(a)) - np.sin(a+2*deltaX))/(2*deltaX)
upd_error = (np.abs((scnd_order-ex_val)/ex_val))*100

print(scnd_order)
print(upd_error) # we can see that the error decrease from 71% with 1st order approx. to about 0.58% with 2nd order

# 3rd order aprroximation with central scheme
thrd_order = (-1*(np.sin(a+2*deltaX)) + 8*(np.sin(a+deltaX)) - 8*(np.sin(a-deltaX)) + np.sin(a-2*deltaX))/(12*deltaX)
upd_error = (np.abs((thrd_order-ex_val)/ex_val))*100

print(thrd_order)
print(upd_error)

frth_order = (-3*(np.sin(a+4*deltaX)) + 16*(np.sin(a+3*deltaX)) - 36*(np.sin(a+2*deltaX)) + 48*(np.sin(a+deltaX)) - 25*(np.sin(a)))/(12*deltaX)
upd_error = (np.abs((frth_order-ex_val)/ex_val))*100
print(upd_error)

print(thrd_order)
print(upd_error) 

# However, it is observed that using higher order approximation (higher than 2nd order) do not produce less error 
# percentage. For the 3rd order approx, the error is about 8% and 4th order approx produces the error about 1.6%
# One more observation is that for the 2nd order approximation with central-scheme produces less error compared to
# the forward-scheme. The error is about 0.2% compared to 0.58%.
