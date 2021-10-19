"""
This file outlines all of the functions originally written in R. 
Author: MacGregor Winegard
Date: 10/18/2021 
"""

import numpy as np
import warnings
warnings.simplefilter("ignore") #This could be dangerous

class trajectory_functions:
    def next_l(l_n, h_n, r_l, d): 
        try:
            return l_n + (r_l*l_n)*(1 - l_n/h_n)*(d - h_n/l_n)
        except:
            return np.nan
       
    def next_h(l_n, h_n, r_h, p_n):
        try:
            return h_n + (l_n - p_n) * (r_h * h_n) * (1 - h_n)
        except:
            return np.nan
   
    """
    Calculates a whole trajectory for l and h
    l is in the 0 column, h is in the 1 column
    """
    def calc_trajectory(l_0, h_0, r_l, r_h, d, l_n1 = None, num_steps = 1000):
        if (num_steps < 3):
            raise Exception("num_steps must be >=3")        
        if (l_n1 == None):
            l_n1 = l_0
        
        one_trajectory = np.empty(shape = (num_steps+1,2), dtype = np.float64)
        
        one_trajectory[0] = [l_0, h_0]
        one_trajectory[1] = [
        trajectory_functions.next_l(l_0, h_0, r_l, d),
        trajectory_functions.next_h(l_0, h_0, r_h, l_n1)
        ]
        
        for n in range (2, num_steps+1):
            one_trajectory[n,0] = \
                trajectory_functions.next_l(one_trajectory[n-1,0],one_trajectory[n-1,1], r_l, d)
            one_trajectory[n,1] = \
                trajectory_functions.next_h(one_trajectory[n-1,0], one_trajectory[n-1,1], r_h, one_trajectory[n-2,0])
        
        return one_trajectory
