"""
This file outlines all of the functions originally written in R. 
Author: MacGregor Winegard
Date: 10/18/2021 
"""

import time
import numpy as np
import warnings
warnings.simplefilter("ignore") #This could be dangerous




class vg_functions:
    #These are the functions outlined in the original Van Geert paper
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
        vg_functions.next_l(l_0, h_0, r_l, d),
        vg_functions.next_h(l_0, h_0, r_h, l_n1)
        ]
        
        for n in range (2, num_steps+1):
            one_trajectory[n,0] = \
                vg_functions.next_l(one_trajectory[n-1,0],one_trajectory[n-1,1], r_l, d)
            one_trajectory[n,1] = \
                vg_functions.next_h(one_trajectory[n-1,0], one_trajectory[n-1,1], r_h, one_trajectory[n-2,0])
        
        return one_trajectory


class kg_functions:
    #These are the dummy functions designed by Dr. Kris Green
    def next_x(x_n, y_n): 
        try:
            return 2*x_n - y_n
        except:
            return np.nan
       
    def next_y(x_n, y_n):
        try:
            return y_n - y_n**2 + x_n**2
        except:
            return np.nan
   
    """
    Calculates a whole trajectory for l and h
    l is in the 0 column, h is in the 1 column
    """
    def calc_trajectory(x_0, y_0, num_steps = 1000):
        
        one_trajectory = np.empty(shape = (num_steps+1,2), dtype = np.float64)
        
        one_trajectory[0] = [x_0, y_0]
        one_trajectory[1] = [
            kg_functions.next_x(x_0, y_0),
            kg_functions.next_y(x_0, y_0)
        ]
        
        
        for n in range (2, num_steps+1):
            one_trajectory[n,0] = \
                kg_functions.next_x(one_trajectory[n-1,0],one_trajectory[n-1,1])
            one_trajectory[n,1] = \
                kg_functions.next_y(one_trajectory[n-1,0], one_trajectory[n-1,1])
            
            """
            if np.isinf(one_trajectory[n,0]) and np.isinf(one_trajectory[n,1]):
                one_trajectory[(n+1):,0] = np.inf
                one_trajectory[(n+1):,1] = np.inf
                break #This actually adds time. 
            """
            
        
        return one_trajectory

class TVA: #TIME VARIANCE AUTHORITY
    #Matlab tic and toc functions, inspired by Stack Overflow
    def tic():
        startTime_for_tictoc = time.time()
        print("Timer started at: " + time.strftime("%H:%M:%S"))
        return startTime_for_tictoc

    def toc(tic_time):
        elapsed_time = "Time Elapsed: " + \
        f"{(time.time() - tic_time)//60:0.0f} minutes, " + \
        f"{((time.time() - tic_time)%60):5.2f} seconds."
        return elapsed_time   