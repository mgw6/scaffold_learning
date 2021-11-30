"""
MacGregor Winegard
11/29/2021

This function gets the dimensions of the np array which is then used for the graphs later

input: np array that is a graphs
output:  a dict with all of the info
"""

def graph_dims(many_traj):
    dims_dict = {}
    
    dims_dict[mt_shape] = many_traj.shape

    dims_dict[len_l] = mt_shape[0]
    dims_dict[len_h] = mt_shape[1]
    dims_dict[n_steps] = mt_shape[2] -1

    dims_dict[l_start] = many_traj[0,0,0,0]
    dims_dict[l_end] = many_traj[len_l-1,0,0,0]
    dims_dict[l_step] = (l_end - l_start)/(len_l-1)
    dims_dict[l_span] = np.arange(l_start, l_end+l_step, l_step)

    dims_dict[h_start] = many_traj[0,0,0,1]
    dims_dict[h_end] = many_traj[0,len_h-1,0,1]
    dims_dict[h_step] = (h_end - h_start)/(len_h-1)
    dims_dict[h_span] = np.arange(h_start, h_end+h_step, h_step)
    
    return dims_dict

    
    