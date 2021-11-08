#Author: MacGregor Winegard
#Date: 11/8/2021
# This file reads saved numpy arrays and graphs them

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


#TODO: Could add option to graph
def print_menu():
    print("Menu:")
    print("\t1) View Specific Trajectory")
    print("\t2) Quit")
    return(int(input("Choice: ")))
    
def get_traj_index(l_start, l_end, l_step, h_start, h_end, h_step):
    print("\n\nSelect a starting l:")
    print("\tl start: " + str(l_start))
    print("\tl end: " + str(l_end))
    print("\tl step: " + str(l_step))
    l_traj = float(input("l: "))
    
    print("Select a starting h:")
    print("\th start: " + str(h_start))
    print("\th end: " + str(h_end))
    print("\th step: " + str(h_step))
    h_traj = float(input("h: "))
    
    l_traj = int((l_traj - l_start)/l_step)
    h_traj = int((h_traj - h_start)/h_step)
    
    return l_traj, h_traj


if __name__ == '__main__':
    root = tk.Tk() 
    root.withdraw()  #https://www.youtube.com/watch?v=H71ts4XxWYU   
    file_path = tk.filedialog.askopenfilename(filetypes = [('Numpy Arrays', '*.npy')],
                                            initialdir = "C:/Users/User/SSCH_Research/scaffold_learning/Py_Code/np_arrs",
                                            title = "Select a np.array"    
                                            )
    many_traj = np.load(file_path)
    
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
    

    while True:
        choice = print_menu()
        
        if choice == 1:
            l_traj, h_traj = get_traj_index(l_start, l_end, l_step, h_start, h_end, h_step)
            
            print(many_traj[l_traj,h_traj])
        
        elif choice == 2:
            break
    print("Exiting Prorgram...")