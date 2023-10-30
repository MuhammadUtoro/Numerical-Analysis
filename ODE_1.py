#Plotting ODE with IVP
#Find the solution of y' = x**3, y(1) = 2
#solve_ivp(fun, t_span, y0, t_eval).

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Define the ODE
def ode(x, y):
    return x**3

#Define the general solution
def f(t):
    return (t**4+7)/4


dom_x = (-2, 2) #Plotting the x-interval
t = np.linspace(-2,2,100)
y0 = 2 #Initial condition
x0 = 1
sol_ODE = solve_ivp(ode, dom_x, [y0], t_eval = np.linspace(-2,2,100))
gen_sol = f(t)

#Plotting
plt.title('Solution for dy/dx = x**3. y(1) =2 ')
plt.plot(t, gen_sol, label='General solution')
plt.scatter(x0, y0, color='red', label='IVP')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(0,6)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True)
plt.legend()
plt.show()
