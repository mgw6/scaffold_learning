library(foreach)
library(parallel)
library(doParallel)
source("functions.R")
library(data.table)
library(tidyverse)

#par sapply

cl <- makeCluster(detectCores() - 1)
registerDoParallel(cl, cores = detectCores() - 1)

cl

H = .01
R_L = .5
R_H = .5
D = 2
n_step = 100

#.combine = 'cbind'


par_test <-
  foreach(L = seq(0,1,by=.001), .inorder = FALSE, .combine= rbind) %dopar%
  {
    multi_test = calc_trajectory(L, H, R_L, R_H, D, l_n1 = NULL, num_steps=n_step)
  }

stopCluster(cl)

typeof(par_test)
dim(par_test)
par_test[2:10,2]
