#Author: MacGregor Winegard
#Date: 11/15/2021
# This file reads saved numpy arrays and graphs them as a vector field

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



x = []
y = []
end_x = []
end_y = []

print("Entering for-loops")
for l in range(len_l):
    for h in range(len_h):
        x.append(l*l_step)
        y.append(h*h_step)
        end_x.append(many_traj[l, h, n_steps, 0])
        end_y.append(many_traj[l, h, n_steps, 1])
print("Exited for-loops")

x = np.array(x), 
y = np.array(y), 
end_x = np.array(end_x)
end_y = np.array(end_y)

end_x = np.where(np.isnan(end_x), 0, end_x)
end_y = np.where(np.isnan(end_y), 0, end_y)


plt.quiver(
            x, 
            y, 
            x/end_x,
            y/end_y,
            headwidth = 12
            )

#plt.axis([l_start, l_end, h_start, h_end])
plt.grid()
plt.show()