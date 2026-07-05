#Graphing functions
import numpy as np
import matplotlib.pyplot as plt

#the function is y = x^2/3 + 1/x
x1 = np.linspace(0.1,2,100)
x2 = np.linspace(-2,-0.1,100)
y1 = ((x1*x1)/3) + 1/x1
y2 = ((x2*x2)/3) + 1/x2

plt.title('y = x^2/3 + 1/x')
plt.plot(x1,y1,x2,y2,'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.tight_layout()
plt.show()
