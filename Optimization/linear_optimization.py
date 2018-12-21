# https://sites.math.washington.edu/~burke/crs/407/notes/section1.pdf

#  max25 B + 20C <=> min -25B -20C
#     subject to 20B + 12C <= 1800 
#     1/15*B +  1/15*C <= 8 <=> B+c <= 120
#     0 <= B,C <=> B,C >=0 <=> -b,-C <= 0

import numpy as np
from scipy.optimize import linprog

A_ub = np.matrix('20 12;1 1;-1 -1')
b_ub = np.matrix('1800;120;0')
c=np.array([-25,-20])

s = linprog(c,A_ub=A_ub,b_ub=b_ub)