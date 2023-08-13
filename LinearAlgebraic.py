# Using a scipy module for linear algebra (matrix) calculation

import numpy as np
from scipy.linalg import eig

#Generating 4-by-4 matrix with a random value from 0 to 5
mat_a = np.random.randint(0,5, size=(4,4))
print(mat_a)

#Matrix multiplication
mat_a_mult = mat_a*mat_a
print(mat_a_mult)

#Find the eigenvalues of Matrix a
eig(mat_a)