source("functions.R")
library(ggplot2)

df = data.frame(L = NULL, rep_h = NULL)
L = seq(0,1,by=.1)
color_list <- c()
for (H in seq(0,1,by=.1) )
{
  multi_test = many_trajectories(L, H, .05, .05, 2, l_n1 = NULL, n_steps=100)

  rep_h = rep(c(H), times = length(L))
  
  for (x in (1:length(multi_test[1,,1])))
  {
    if (!is.finite((multi_test[length(multi_test[,1,1]),x,1])))
    {
      color_list <- append(color_list, "red")
    } else { 
      color_list <- append(color_list, "blue")
    }
  }
  df = rbind(df, data.frame(L, rep_h))
}

df
color_list
plot = ggplot(df, aes(L,H, color = color_list, )) + geom_point() 
plot







