import numpy as np
import matplotlib.pyplot as plt

def cube_Vol(Length):
    volume = Length**3
    return volume

L = np.linspace(1,3,3)

V = cube_Vol(L)

print(V)

plt.plot(L,V)
plt.xlabel('Cube length (unit)')
plt.ylabel('Volume (unit cubic)')
plt.show()

