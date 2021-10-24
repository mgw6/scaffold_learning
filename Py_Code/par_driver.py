import time
from joblib import Parallel, delayed

import numpy as np
np.set_printoptions(threshold = np.inf)
import pandas as pd
import matplotlib.pyplot as plt

from functions import kg_functions as fxns

steps = 1000
eps = .1
d = 2

l_start = 0
l_end = 1
l_step = .02
l_span = np.arange(l_start, l_end+l_step, l_step)
len_l = len(l_span)

h_start = 0
h_end = 1
h_step = .02
h_span = np.arange(l_start, l_end+h_step, l_step)
len_h = len(h_span)

many_traj = np.empty(shape = (len_l, len_h, steps+1, 2), dtype = np.float64)


t = time.time()
for l in range(len_l):
    #print("Starting " + str(l) + "/" + str(len_l) + " l's.")
    many_traj[l] = Parallel(n_jobs=-1)(delayed(fxns.calc_trajectory)(l_span[l], H, steps) for H in h_span)
print(time.time() - t)

print(many_traj.shape)