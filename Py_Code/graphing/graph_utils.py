"""
MacGregor Winegard
11/29/2021

This function gets the dimensions of the np array which is then used for the graphs later

input: np array that is a graphs
output:  a dict with all of the info
"""

import numpy as np

def graph_dims(many_traj):
    dims_dict = {}
    
    dims_dict['mt_shape'] = many_traj.shape

    dims_dict['len_l'] = dims_dict['mt_shape'] [0]
    dims_dict['len_h'] = dims_dict['mt_shape'] [1]
    dims_dict['n_steps'] = dims_dict['mt_shape'] [2] -1

    dims_dict['l_start'] = many_traj[0,0,0,0]
    dims_dict['l_end'] = many_traj[dims_dict['len_l']-1,0,0,0]
    dims_dict['l_step'] = (dims_dict['l_end'] - dims_dict['l_start'])/(dims_dict['len_l']-1)
    dims_dict['l_span'] = np.arange(dims_dict['l_start'], 
                            dims_dict['l_end']+dims_dict['l_step'], 
                            dims_dict['l_step'])

    dims_dict['h_start'] = many_traj[0,0,0,1]
    dims_dict['h_end'] = many_traj[0,dims_dict['len_h']-1,0,1]
    dims_dict['h_step'] = (dims_dict['h_end'] - dims_dict['h_start'])/(dims_dict['len_h']-1)
    dims_dict['h_span'] = np.arange(dims_dict['h_start'], 
                            dims_dict['h_end']+dims_dict['h_step'],    
                            dims_dict['h_step'])
    
    return dims_dict

    
    