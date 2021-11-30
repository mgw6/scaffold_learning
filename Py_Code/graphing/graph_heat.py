# Author: MacGregor Winegard
# Date: 10/25/2021
# This file reads saved numpy arrays and graphs the basin of attraction.

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import seaborn as sns

import graph_utils

#This loads the array
root = tk.Tk() 
root.withdraw()  #https://www.youtube.com/watch?v=H71ts4XxWYU   
file_path = tk.filedialog.askopenfilename(filetypes = [('Numpy Arrays', '*.npy')],
                                        initialdir = "C:/Users/User/SSCH_Research/scaffold_learning/Py_Code/np_arrs",
                                        title = "Select a np.array"    
                                        )
many_traj = np.load(file_path)

dims_dict = graph_utils.graph_dims(many_traj)

#TODO: basically flatten this into a 2d array where the value at each index is the value at the end of that trajectory.
#The issue with that is that this will not maintain the coordinates. 

heat_map = np.empty(shape = (dims_dict['len_l'],dims_dict['len_h']), dtype = float)

#TODO: This could be made so much more efficient if you just said take the top layer
print("Entering for-loops")
for l in range(dims_dict['len_l']):
    for h in range(dims_dict['len_h']): 
        heat_map[l,h] = many_traj[l, h, dims_dict['n_steps'], 0]
print("Exiting for-loops")

"""
plt.imshow(np.rot90(heat_map))
plt.colorbar()
plt.axis([l_start, l_end, h_start, h_end])
plt.grid()
"""

heat_map = np.where(heat_map > 2, np.nan, heat_map)
heat_map = np.where(heat_map < 0, np.nan, heat_map)

ax = sns.heatmap(np.rot90(heat_map))
plt.show()