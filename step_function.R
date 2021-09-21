
next_l <- function(l_n, h_n, r_l, d)
{
  return(l_n + (r_l*l_n)*(1 - l_n/h_n)*(d - h_n/l_n))
}

next_h <- function(l_n, h_n, r_h, p_n)
{
  return(h_n + (l_n - p_n)*(r_h*h_n)*(1-h_n))
}

next_step <- function(l_n, h_n, r_l, d, r_h, p_n)
{
  #This function is more work than its worth. 
  next_step = c(size = 2)
  next_step[1] = next_l(l_n, h_n, r_l, d)
  next_step[2] = next_h(l_n, h_n, r_h, p_n)
  return (next_step)
}

calc_trajectory <- function(l_0, h_0, r_l, r_h, d, l_n1 = NULL, num_steps=1000)
{ 
  if (num_steps <3) stop("Num_steps must be >=3.")
  
  num_steps = num_steps+1
  l_traj = c(size = num_steps)
  h_traj = c(size = num_steps)
  
  l_traj[1] = l_0
  h_traj[1] = h_0
  l_traj[2] = next_l(l_traj[1], h_traj[1], r_l, d)
  
  if (is.null(l_n1)) 
  {
    h_traj[2] = next_h(l_traj[1], h_traj[1], r_h, l_traj[1] )
  } else {
    h_traj[2] = next_h(l_traj[1], h_traj[1], r_h, l_n1 )
  }
  
  for (n in 3:num_steps)
  {
    l_traj[n] = next_l(l_traj[n-1], h_traj[n-1], r_l, d)
    h_traj[n] = next_h(l_traj[n-1], h_traj[n-1], r_h, l_traj[n-2] )
  }
  
  n = 0:(num_steps-1)
  return (cbind(n,l_traj, h_traj))
}

many_trajectories <- function(l_0, h_0, r_l, r_h, d, l_n1 = NULL, n_steps=1000)
{
  if(is.vector(l_0))
  {
    result_l = matrix(data = NA, nrow = (n_steps+1), ncol = length(l_0))
    result_h = matrix(data = NA, nrow = (n_steps+1), ncol = length(l_0))
    
    for (count in (1:length(l_0)))
    {
        #print(count)
        one_traj_result = calc_trajectory(l_0[count], h_0, r_l, r_h, d, l_n1, num_steps = n_steps )
        result_l[,count] = one_traj_result[,2]
        result_h[,count] = one_traj_result[,3]
    }
  } else if (is.vector(h_0)) {
    stop("Coming Soon!")
  } else if (is.vector(r_l)) {
    stop("Coming Soon!")
  } else if (is.vector(r_h)) {
    stop("Coming Soon!")
  } else if (is.vector(l_n1)) {
    stop("Coming Soon!")
  } else{ 
    stop("Vector not found.")
  }

  return (simplify2array(list(result_l, result_h)))
  
}
