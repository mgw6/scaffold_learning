#MacGregor Winegard

import numpy as np
np.set_printoptions(threshold = np.inf)
from functions import kg_functions as fxns

l_0 = float(input("Input l_0: "))
h_0 = float(input("Input h_0: "))
n_steps = int(input("Num steps: "))

result = fxns.calc_trajectory(l_0, h_0, n_steps)

print(result)
