#This is a driver file that will pull functions from other files
source("step_function.R")

test_result = calc_trajectory(.01, .015, .05, .05, 2, num_steps = 5)
print(test_result)

plot(test_result[,1], test_result[,2])
