"""
MacGregor Winegard
Date: 11/21/2021
This function graphs one trajectory in 3d
"""
import numpy as np
np.set_printoptions(threshold = np.inf)
from functions import kg_functions as fxns
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d


l_0 = float(input("Input l_0: "))
h_0 = float(input("Input h_0: "))
n_steps = int(input("Num steps: "))

result = fxns.calc_trajectory(l_0, h_0, n_steps)


print("Plotting")
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(
        result[:,0],
        result[:,1],
        np.linspace(0, n_steps, n_steps+1)
        )   
plt.show()

print("Here is the trajectory:")
print(result)