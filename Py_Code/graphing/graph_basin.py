#Author: MacGregor Winegard
#Date: 10/25/2021
# This file reads saved numpy arrays and graphs the basin of attraction.

import pandas as pd
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


print("Entering for-loops")
for l in range(dims_dict['len_l']):
    for h in range(dims_dict['len_h']):

        
        if not np.isfinite(many_traj[l, h, dims_dict['n_steps'], 0]) or many_traj[l, h, dims_dict['n_steps'],0] > 100:
            #data.append([dims_dict['l_span'][l], dims_dict['h_span'][h], 'red'])
            #https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html
            pass
        
        
        elif abs(many_traj[l, h, dims_dict['n_steps'], 0] - 1.5) < eps and abs(many_traj[l, h, dims_dict['n_steps'], 1] - 1.5) < eps:
            data.append([dims_dict['l_span'][l], dims_dict['h_span'][h], 'green'])
        
        
        elif np.abs(many_traj[l, h, dims_dict['n_steps'], 0] - many_traj[l, h, dims_dict['n_steps'], 1]) < eps:
            data.append([dims_dict['l_span'][l], dims_dict['h_span'][h], 'blue'])
        
        else:
            data.append([dims_dict['l_span'][l], dims_dict['h_span'][h], 'black'])
            
            
        """
        elif np.abs(many_traj[l, h, dims_dict['n_steps'], 1] - d*(many_traj[l, h, dims_dict['n_steps'], 0])) < eps:
            data.append([dims_dict['l_span'][l], dims_dict['h_span'][h], 'green'])
        """
print("Exited for-loops")

df = pd.DataFrame(data, columns = ["Initial l", "Initial h", "Color"])
df.plot.scatter(x = "Initial l", y = "Initial h", c = "Color", s=1)

"""
m2 = -1.5
#y2 = (m2 - 3/2)*dims_dict['l_span'] + 3/2 
y2 = np.copy(dims_dict['l_span'])
plt.plot(dims_dict['l_span'], y2, color = "red")
"""

"""
y2 = np.sqrt(dims_dict['l_span']**2 + 2*dims_dict['l_span'] -2)
plt.plot(dims_dict['l_span'], y2, color = "green")

y3 = -np.sqrt(dims_dict['l_span']**2 + 2*dims_dict['l_span'] -2)
plt.plot(dims_dict['l_span'], y3, color = "green")
"""

"""
y2 = 2*dims_dict['l_span'] - 3/2
plt.plot(dims_dict['l_span'], y2, color = "yellow")
"""

"""
m3 = 31/15
b3 = -(941/600)
y3 = m3*dims_dict['l_span'] + b3
plt.plot(dims_dict['l_span'], y3, color = "#FFD333")
"""


plt.axis([dims_dict['l_start'], dims_dict['l_end'], dims_dict['h_start'], dims_dict['h_end']])
plt.grid()
plt.show()
