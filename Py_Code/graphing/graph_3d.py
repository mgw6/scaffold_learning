#Author: MacGregor Winegard
#Date: 10/25/2021
# This file reads saved numpy arrays and graphs the basin of attraction.


import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


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

z_line = np.linspace(0, n_steps, n_steps+1)
fig = plt.figure()
ax = plt.axes(projection='3d',
            xlabel = "X",
            ylabel = "Y",
            zlabel = "Z"
            )

many_traj = np.where(many_traj > 10, np.nan, many_traj)
many_traj = np.where(many_traj < -10, np.nan, many_traj)

print("Entering for-loops")
for l in range(len_l):
    for h in range(len_h):
        ax.plot3D(
            many_traj[l,h,:,0],
            many_traj[l,h,:,1],
            z_line
        )   
print("Exiting for-loops")
plt.show()