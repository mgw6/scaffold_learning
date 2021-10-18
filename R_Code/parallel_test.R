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

#.combine = 'cbind'


par_test <-
    foreach(L = seq(0,1,by=.001), .inorder = FALSE) %dopar%
  {
    multi_test = calc_trajectory(L, H, R_L, R_H, D, l_n1 = NULL, num_steps=100)
  }

stopCluster(cl)

typeof(par_test[2])


temp_arr = list_to_array(par_test)
#I don't love the dimensions this is in, may be something to discuss. 
dim(temp_arr)
#Python I miss you