# This is a driver file to test the functions
#import functions.trajectory_functions as fxns
from functions import trajectory_functions as fxns
import numpy as np

#single_test = fxns.calc_trajectory(.01, .015, .05, .05, 2, num_steps = 5)

steps = 1000
l_span = 10
h_span = 10
d_span = 10


many_traj = np.empty(shape = (l_span+1, h_span+1, d_span+1, steps+1, 2), dtype = np.float64)

for l in range(l_span + 1):
    print("l= " + str(l))
    for h in range(h_span + 1):
        for d in range(d_span + 1): 
            many_traj[l,h,d] = fxns.calc_trajectory(l/l_span, h/h_span, .05, .05, d, num_steps = steps)

print(many_traj[5,8,2])