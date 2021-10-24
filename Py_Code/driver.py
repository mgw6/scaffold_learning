"""
This is a driver file to test the functions
Author: MacGregor Winegard
Date: 10/19/2021
"""

from functions import kg_functions as fxns
import numpy as np
np.set_printoptions(threshold = np.inf)
import pandas as pd
import matplotlib.pyplot as plt

#single_test = fxns.calc_trajectory(.01, .015, .05, .05, 2, num_steps = 100)
steps = 1000
eps = .1
d = 2

l_start = -1
l_end = 3
l_step = .02
l_span = np.arange(l_start, l_end+l_step, l_step)
len_l = len(l_span)


h_start = -4
h_end = 4
h_step = .02
h_span = np.arange(l_start, l_end+h_step, l_step)
len_h = len(h_span)

data = []



many_traj = np.empty(shape = (len_l, len_h, steps+1, 2), dtype = np.float64)

for l in range(len_l):
    print("Starting " + str(l) + "/" + str(len_l) + " l's.")
    for h in range(len_h):
        many_traj[l,h] = fxns.calc_trajectory(l_span[l], h_span[h], num_steps = steps)
        
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
plt.show()

