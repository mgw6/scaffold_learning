import time
from joblib import Parallel, delayed

import numpy as np
np.set_printoptions(threshold = np.inf)
import os
import pandas as pd
import matplotlib.pyplot as plt

from functions import kg_functions as fxns
from functions import TVA

np_folder = "np_arrs/"

eps = .1
d = 2
data = []

steps = 1000

l_start = .5
l_end = 1.5
l_step = .01
l_span = np.arange(l_start, l_end+l_step, l_step)
len_l = len(l_span)

h_start = 1
h_end = 2
h_step = .0001
h_span = np.arange(h_start, h_end+h_step, h_step)
len_h = len(h_span)



many_traj = np.empty(shape = (len_l, len_h, steps+1, 2), dtype = np.float16)


start_time = TVA.tic()
for l in range(len_l):
    print("Starting " + str(l) + "/" + str(len_l) + " l's.")
    many_traj[l] = Parallel(n_jobs = -1, batch_size = 3)(
        delayed(fxns.calc_trajectory)(l_span[l], H, steps) for H in h_span)
time_elapsed = TVA.toc(start_time)
print(time_elapsed)


folder_name =  time.strftime("%m.%d__%H.%M.%S/")
os.mkdir(np_folder + folder_name)
np.save(np_folder + folder_name + "arr", many_traj)


file = open((np_folder + folder_name + "notes.txt"), "w+")
file.write("Time run: " + folder_name[:-1] + "\n")
file.write(time_elapsed + "\n")
file.write("====================\n")
file.write("Number of steps: " + str(steps) + "\n\n")

file.write("l_start: " + str(l_start) + "\n")
file.write("l_end: " + str(l_end) + "\n")
file.write("l_step: " + str(l_step) + "\n\n\n")


file.write("h_start: " + str(h_start) + "\n")
file.write("h_end: " + str(h_end) + "\n")
file.write("h_step: " + str(h_step) + "\n")
file.close()
