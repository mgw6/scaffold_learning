"""
This is a driver file to test the functions
Author: MacGregpor Winegard
Date: 10/19/2021
"""



from functions import trajectory_functions as fxns
import numpy as np
np.set_printoptions(threshold = np.inf)
import pandas as pd

#single_test = fxns.calc_trajectory(.01, .015, .05, .05, 2, num_steps = 5)

steps = 1000

l_start = -4
l_end = 4
l_step = .1
l_span = np.arange(l_start, l_end, l_step)
len_l = int((l_end - l_start)/l_step)

h_start = -4
h_end = 4
h_step = .1
h_span = np.arange(l_start, l_end, l_step)
len_h = int((h_end - h_start)/h_step)

data = []


many_traj = np.empty(shape = (len_l+1, len_h+1, steps+1, 2), dtype = np.float64)

for l in range(len_l+1):
    print("l= " + str(l))
    for h in range(len_h+1):
        many_traj[l,h] = fxns.calc_trajectory(l, h, .05, .05, 2, num_steps = steps)

