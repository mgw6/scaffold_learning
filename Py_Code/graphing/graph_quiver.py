#Author: MacGregor Winegard
#Date: 11/15/2021
# This file reads saved numpy arrays and graphs them as a vector field

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

dims_dict = graph_utils.graph_dims(many_traj)

eps = .1
d = 2
data = []

x = []
y = []
end_x = []
end_y = []

print("Entering for-loops")
for l in range(dims_dict['len_l']):
    for h in range(dims_dict['len_h']):
        
        if not np.isfinite(many_traj[l, h, dims_dict['n_steps'], 0]):
            continue
    
        x.append(l*dims_dict['l_step'])
        y.append(h*dims_dict['h_step'])
        end_x.append(many_traj[l, h, dims_dict['n_steps'], 0])
        end_y.append(many_traj[l, h, dims_dict['n_steps'], 1])
print("Exited for-loops")

x = np.array(x), 
y = np.array(y), 
end_x = np.array(end_x)
end_y = np.array(end_y)


plt.quiver(
            x, 
            y, 
            end_x - x,
            end_y - y,
            #headwidth = 12
            )

#plt.axis([l_start, l_end, h_start, h_end])
plt.grid()
plt.show()