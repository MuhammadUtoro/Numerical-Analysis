import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

#Program for computing the height of the ball thrown in a vertical motion
v0 = 4.15 #Initial Velocity
g = 9.81 #Acceleration due to gravity
t = linspace(0,1,101) #Iterate time every 0.01s
y = v0*t-0.5*g*t**2 #Equation to solve vertical position


#Find the max height
max_Height = y[0] #Pre-allocate variable to store the height value

for i in range (1,100):
    if y[i] > max_Height:
        max_Height = y[i]
print("The maximum height reached is " + str(max_Height))

#Find the time as the ball hits the ground
i = 0
while y[i] >= 0:
    i += 1

print("The ball hits the ground in around " + str(0.5*(t[i-1]+t[i])) + " seconds")
        
plt.plot(t,y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
