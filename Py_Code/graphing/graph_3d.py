#Author: MacGregor Winegard
#Date: 10/25/2021
# This file reads saved numpy arrays and graphs the basin of attraction.


import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import graph_utils


root = tk.Tk() 
root.withdraw()  #https://www.youtube.com/watch?v=H71ts4XxWYU   
file_path = tk.filedialog.askopenfilename(filetypes = [('Numpy Arrays', '*.npy')],
                                        initialdir = "C:/Users/User/SSCH_Research/scaffold_learning/Py_Code/np_arrs",
                                        title = "Select a np.array"    
                                        )
many_traj = np.load(file_path)


eps = .1
d = 2
data = []

dims_dict = graph_utils.graph_dims(many_traj)

z_line = np.linspace(0, dims_dict['n_steps'], dims_dict['n_steps']+1)
fig = plt.figure()
ax = plt.axes(projection='3d',
            xlabel = "X",
            ylabel = "Y",
            zlabel = "Z"
            )

many_traj = np.where(many_traj > 10, np.nan, many_traj)
many_traj = np.where(many_traj < -10, np.nan, many_traj)

print("Entering for-loops")
for l in range(dims_dict['len_l']):
    for h in range(dims_dict['len_h']):
        ax.plot3D(
            many_traj[l,h,:,0],
            many_traj[l,h,:,1],
            z_line
        )   
print("Exiting for-loops")
plt.show()