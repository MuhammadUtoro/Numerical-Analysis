# This program still simulates the orbital motion but with different cases, such as geo-synch satellite to earth
# Moon to earh and earth to sun
# In this program, I'd like to use matrix as well in comparison to previous section
# Simulating moon's orbit around the earth and simulating earth orbit around the sun
# The numbers provided below are not the astronomical numbers as they are complicated to debug
# Unfortunately, I haven't figured it out the solution for this exercise

import numpy as np

G = -10 # gravitational constant
M1 = 1
R1 = 0.5
M2 = 1
R2 = 0.5 
dt = 0.00001
n = 200000

# Using 2d array to store all the values. col[0] = t, col[1] = x1, col[2] = y1, col[3] = vx1, col[4] = vy1
# col[5] = x2, col[6] = y2, col[7] = vx2, col[8] = vy2
init_state = np.zeros((n+1,9))
init_state[0,2] = 10
init_state[0,3] = 1
init_state[0,7] = -1

for i in range(0,n):
    init_state[i+1,0] = init_state[i,0] + dt
    init_state[i+1,1] = init_state[i,1] + init_state[i,3] *dt
    init_state[i+1,2] = init_state[i,2] + init_state[i,4] *dt
    init_state[i+1,5] = init_state[i,5] + init_state[i,7] *dt
    init_state[i+1,6] = init_state[i,6] + init_state[i,8] *dt
    
