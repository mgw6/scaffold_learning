source("functions.R")
library(ggplot2)

df = data.frame(L = NULL, rep_h = NULL)
L = seq(-4,4,by=.1)
eps = .1
d = 2

for (H in seq(-4,4,by=.1) )
{
  color_list <- c()
  multi_test = many_trajectories(L, H, 1, .5, d, l_n1 = NULL, n_steps=100)
  list_len = length(multi_test[,1,1])

  rep_h = rep(c(H), times = length(L))
  
  for (x in (1:length(multi_test[1,,1])))
  {
    if (!is.finite(multi_test[list_len,x,1]) || multi_test[list_len,x,1] > 100 )
    {
      color_list <- append(color_list, 'red')
    } else if ( 
      abs(multi_test[list_len,x,1] - multi_test[list_len,x,2]) < eps)
        
    {
      "Make this be more like if (abs(ln-hn) <  eps or abs(h - d*l) < eps)"
      color_list <- append(color_list, 'blue')
    
    } else if (abs(multi_test[list_len,x,2] - d*multi_test[list_len,x,1]) < eps)
    {
      color_list <- append(color_list, 'green')
      
      } else { 
      color_list <- append(color_list, 'black')
    }
  }
  df = rbind(df, data.frame(L, rep_h, color_list))
}


plot = ggplot(df, aes(L,rep_h )) + geom_point(colour = df$color_list) 
plot

#Make on big dataframe, then start peeling off the pieces that you want to work with. 

#instead of collecting it all into one object

# code 1 -> runs traj -> write to file
# code 2 -> reads file and makes plot
#   for each file in folder
#     - read L0 H0
#     - Read Ln Hn, color
#     then L over n, h over n
#     for all initial trajectories, plot the final trajectories