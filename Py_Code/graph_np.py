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

print("Entering for-loops")
for l in range(len_l):
    for h in range(len_h):

        
        if not np.isfinite(many_traj[l, h, n_steps, 0]) or many_traj[l, h, n_steps,0] > 100:
            #data.append([l_span[l], h_span[h], 'red'])
            #https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html
            pass
        
        
        elif abs(many_traj[l, h, n_steps, 0] - eps) < .1 and abs(many_traj[l, h, n_steps, 1] - 1.5) < eps:
            data.append([l_span[l], h_span[h], 'green'])
        
        
        elif np.abs(many_traj[l, h, n_steps, 0] - many_traj[l, h, n_steps, 1]) < eps:
            data.append([l_span[l], h_span[h], 'blue'])
        
        else:
            data.append([l_span[l], h_span[h], 'black'])
            
            
        """
        elif np.abs(many_traj[l, h, n_steps, 1] - d*(many_traj[l, h, n_steps, 0])) < eps:
            data.append([l_span[l], h_span[h], 'green'])
        """
print("Exited for-loops")

df = pd.DataFrame(data, columns = ["Initial l", "Initial h", "Color"])
df.plot.scatter(x = "Initial l", y = "Initial h", c = "Color", s=1)

"""
m2 = -1.5
#y2 = (m2 - 3/2)*l_span + 3/2 
y2 = np.copy(l_span)
plt.plot(l_span, y2, color = "red")
"""

"""
y2 = np.sqrt(l_span**2 + 2*l_span -2)
plt.plot(l_span, y2, color = "green")

y3 = -np.sqrt(l_span**2 + 2*l_span -2)
plt.plot(l_span, y3, color = "green")
"""

"""
y2 = 2*l_span - 3/2
plt.plot(l_span, y2, color = "yellow")
"""

"""
m3 = 31/15
b3 = -(941/600)
y3 = m3*l_span + b3
plt.plot(l_span, y3, color = "#FFD333")
"""


plt.axis([l_start, l_end, h_start, h_end])
plt.grid()
plt.show()