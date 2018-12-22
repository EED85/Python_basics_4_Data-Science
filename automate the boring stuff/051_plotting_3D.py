# https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#Surface PLots

    #define functions

def poly_3D(x,y):
    return x**2+y**2

def poly_3D2(M):
    return M[0]**2+M[1]**2


    #prepare data

step = 1
X = np.arange(-4,5,step)
Y=X

X,Y = np.meshgrid(X,Y)
Z = poly_3D(X,Y)

    #plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)
plt.show()

