library("foreach")
library("parallel")
library("doParallel")
source("functions.R")

cl <- makeCluster(detectCores() - 1)
registerDoParallel(cl, cores = detectCores() - 1)


H = .01
R_L = .5
R_H = .5
D = 2

#.combine = 'cbind'

par_test <-
    foreach(L = seq(0,1,by=.1), .inorder = FALSE) %dopar%
  {
    multi_test = calc_trajectory(L, H, R_L, R_H, D, l_n1 = NULL, num_steps=10)
  }

par_test
length(par_test)
typeof(par_test)
dim(par_test)

stopCluster(cl)


