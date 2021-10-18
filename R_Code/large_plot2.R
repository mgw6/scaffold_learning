source("functions.R")
library(ggplot2)

df = data.frame(L = NULL, rep_h = NULL)
L = seq(0,1,by=.02)

for (H in seq(0,1,by=.02) )
{
  color_list <- c()
  multi_test = many_trajectories(L, H, .1, .05, 2, l_n1 = NULL, n_steps=100)
  list_len = length(multi_test[,1,1])
  
  rep_h = rep(c(H), times = length(L))
  
  for (x in (1:length(multi_test[1,,1])))
  {
    if (!is.finite(multi_test[list_len,x,1]) || multi_test[list_len,x,1] > 100 )
    {
      color_list <- append(color_list, 'red')
    } else if 
    ((multi_test[list_len,x,1] - multi_test[list_len-1,x,1])^2 + 
     (multi_test[list_len,x,2] - multi_test[list_len-1,x,2])^2  <=
     (multi_test[list_len-1,x,] - multi_test[list_len-2,x,1])^2 + 
     (multi_test[list_len-1,x,2] - multi_test[list_len-2,x,2])^2
    )
    {
      color_list <- append(color_list, 'blue')
    } else { 
      color_list <- append(color_list, 'green')
    }
  }
  df = rbind(df, data.frame(L, rep_h, color_list))
}

dim(df)
plot = ggplot(df, aes(L,rep_h )) + geom_point(colour = df$color_list) 
plot

#Tells us its converging, but not what it converged to. 