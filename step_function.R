
"
test_sqr <- function(x)
{
  jack = vector(double, 2)
  #[]
  return(jack)
}

test_sqr(5)

vector1 = c(1,2,3)
vector1
"


next_l <- function(l_n, h_n, r_l, d)
{
  return(l_n + (r_l*l_n)(1 - l_n/h_n)(d - h_n/l_n))
}

next_h <- function(l_n, h_n, r_h, p_n)
{
  return(h_n + (l_n - p_n)*(r_h)*(1-h_n))
}

next_step <- function(l_n, h_n, r_l, d, r_h, p_n)
{
  #This function may  be more work than its worth. 
  next_step = c(size = 2)
  next_step[1] = next_l(l_n, h_n, r_l, d)
  next_step[2] = next_h(l_n, h_n, r_h, p_n)
  return (next_step)
}

calc_trajectory <- function(l_0, h_0, r_l, r_h, d, num_steps=1000)
{
  
  if (num_steps <4) stop("Num_steps must be >=4.")
  
  l_traj = c(size = 1000)
  h_traj = c(size = 1000)
  l_traj[1] = l_0
  h_traj[1] = h_0
  
  l_traj[2] = next_l(l_traj[1], h_traj[1], r_l, d)
  h_traj[2] = next_h(l_traj[1], h_traj[1], r_h, l_traj[1] )
  
  for (n in 3: num_steps)
  {
    l_traj[n] = next_l(l_traj[n-1], h_traj[n-1], r_l, d)
    next_h(l_traj[n-1], h_traj[n-1], r_h, l_traj[n-2] )
  }
  return (c(l_traj, h_traj))
}


calc_trajectory(0,.5, .1, .1, .05, num_steps = 5)


