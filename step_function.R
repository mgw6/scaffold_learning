
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
  next_step = c(size = 2)
  next_step[1] = next_l(l_n, h_n, r_l, d)
  next_step[2] = next_h(l_n, h_n, r_h, p_n)
  return (next_step)
}


