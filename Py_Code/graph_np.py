#Author: MacGregor Winegard
#Date: 10/25/2021
# This file reads saved numpy arrays and graphs them

import pandas as pd
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
len_l = many_traj.shape[0]
len_h = many_traj.shape[1]

l_start = many_traj[0,0,0,0]
l_end = many_traj[len_l-1,0,0,0]
l_step = (l_end - l_start)/(len_l-1)
l_span = np.arange(l_start, l_end+l_step, l_step)

h_start = many_traj[0,0,0,1]
h_end = many_traj[0,len_h-1,0,1]
h_step = (h_end - h_start)/(len_h-1)
h_span = np.arange(h_start, h_end+h_step, h_step)


for l in range(len_l):
    for h in range(len_h):
        
        if not np.isfinite(many_traj[l, h, len_l, 0]) or many_traj[l, h, len_l,0] > 100:
            data.append([l_span[l], h_span[h], 'red'])
        
        elif np.abs(many_traj[l, h, len_l, 0] - many_traj[l, h, len_h, 1]) < eps:
            data.append([l_span[l], h_span[h], 'blue'])
        
        elif np.abs(many_traj[l, h, len_h, 1] - d*(many_traj[l, h, len_l, 0])) < eps:
            data.append([l_span[l], h_span[h], 'green'])
        
        else:
            data.append([l_span[l], h_span[h], 'black'])


df = pd.DataFrame(data, columns = ["Initial l", "Initial h", "Color"])
df.plot.scatter(x = "Initial l", y = "Initial h", c = "Color")

plt.grid()
plt.show()