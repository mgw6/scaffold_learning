#This is a driver file that will pull functions from other files
source("functions.R")

single_test = calc_trajectory(.01, .015, .05, .05, 2, num_steps = 100)
print(single_test)


plot(single_test[,2], single_test[,3])

multi_test = many_trajectories(seq(0,1,by=.1), .01, .05, .05, 2, l_n1 = NULL, n_steps=10)
multi_test = many_trajectories(.01, seq(0,1,by=.1), .05, .05, 2, l_n1 = NULL, n_steps=10)
multi_test = many_trajectories(.01,  .05, seq(0,1,by=.1), .05, 2, l_n1 = NULL, n_steps=10)
multi_test = many_trajectories(.01,  .05,  .05, seq(0,1,by=.1), 2, l_n1 = NULL, n_steps=10)
multi_test = many_trajectories(.01,  .05,  .05,  2, seq(0,1,by=.1), l_n1 = NULL, n_steps=10)
multi_test = many_trajectories(.01,  .05,  .05,  2, 2, l_n1 = seq(0,1,by=.1), n_steps=10)

dim(multi_test)
multi_test


multi_test = many_trajectories(seq(0,1,by=.01), .01, .05, .05, 2, l_n1 = NULL, n_steps=1000)
multi_test

