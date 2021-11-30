# Author: MacGregor Winegard
# Date: 10/25/2021
# This file reads saved numpy arrays and graphs the basin of attraction.

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import seaborn as sns

#This loads the array
root = tk.Tk() 
root.withdraw()  #https://www.youtube.com/watch?v=H71ts4XxWYU   
file_path = tk.filedialog.askopenfilename(filetypes = [('Numpy Arrays', '*.npy')],
                                        initialdir = "C:/Users/User/SSCH_Research/scaffold_learning/Py_Code/np_arrs",
                                        title = "Select a np.array"    
                                        )
many_traj = np.load(file_path)


# This is where we get the dims of the array
mt_shape = many_traj.shape

len_l = mt_shape[0]
len_h = mt_shape[1]
n_steps = mt_shape[2] -1

l_start = many_traj[0,0,0,0]
l_end = many_traj[len_l-1,0,0,0]
l_step = (l_end - l_start)/(len_l-1)
l_span = np.arange(l_start, l_end+l_step, l_step)

h_start = many_traj[0,0,0,1]
h_end = many_traj[0,len_h-1,0,1]
h_step = (h_end - h_start)/(len_h-1)
h_span = np.arange(h_start, h_end+h_step, h_step)

#TODO: basically flatten this into a 2d array where the value at each index is the value at the end of that trajectory.
#The issue with that is that this will not maintain the coordinates. 

heat_map = np.empty(shape = (len_l,len_h), dtype = float)

#TODO: This could be made so much more efficient if you just said take the top layer
print("Entering for-loops")
for l in range(len_l):
    for h in range(len_h): 
        heat_map[l,h] = many_traj[l, h, n_steps, 0]
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