# in this practice session, the task is to approximate the derivative value of a function (sin(x)) using the
# 2nd order approximation. In the lesson, it is shown that using the 1st order approximation resulting in 
# inaccurate approximation compared to the exact value
# My observation was that the approximation value is indeed closer to the exact value using the higher order and using the third- fourth-order 
# approximation for the first derivative using central scheme will result in the same exact difference formule, hence same results

import numpy as np
import matplotlib.pyplot as plt

a = (np.pi/2)-0.35
b = (np.pi/2)+0.15
fa = np.sin(a)
fb = np.sin(b)
ex_val = np.cos(a)
deltaX = b-a
frst_order = (fb - fa)/deltaX
error = (np.abs((frst_order-ex_val)/ex_val))*100
print('The first order value is: ', frst_order,'\nand the exact value is:', ex_val)
print('The error is: ', error, '%')

# now we implement the difference formula to estimate the first derivative
# f'(a) = (-3*f(a) + 4*f(a+deltaX) - f(a+2*deltaX))/2*deltaX

# This is a second-order approximation for the first derivative using forward scheme
scnd_order = (4*(np.sin(a+deltaX)) - 3*(np.sin(a)) - np.sin(a+2*deltaX))/(2*deltaX)
upd_error = (np.abs((scnd_order-ex_val)/ex_val))*100
print('The second order value is: ', scnd_order,'\nand the exact value is:', ex_val)
print('The error is: ', upd_error, '%') # we can see that the error decrease from 71% with 1st order approx. to about 0.58% with 2nd order

# This is a third-order approximation for the first derivative using central scheme
thrd_order = (-1*(np.sin(a+2*deltaX)) + 8*(np.sin(a+deltaX)) - 8*(np.sin(a-deltaX)) + np.sin(a-2*deltaX))/(12*deltaX) 
upd_error = (np.abs((thrd_order-ex_val)/ex_val))*100
print('The third order value is: ', thrd_order,'\nand the exact value is:', ex_val)
print('The error is: ', upd_error, '%')

# This is a fourth-order approximation for the first derivative using central scheme
frth_order = (-1*(np.sin(a+2*deltaX)) + 8*(np.sin(a+deltaX)) - 8*(np.sin(a-deltaX)) + 1*(np.sin(a-2*deltaX)))/(12*deltaX)
upd_error = (np.abs((frth_order-ex_val)/ex_val))*100
print('The fourth order value is: ', frth_order,'\nand the exact value is:', ex_val)
print('The error is: ', upd_error, '%')
