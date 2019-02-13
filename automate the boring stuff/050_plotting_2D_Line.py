
#%% [markdown]
# # import libs

import matplotlib.pyplot as plt
import numpy as np

#%% [markdown]

# ## tip: always import seaborn and set style, plt plots look nicer then

import seaborn as sns
sns.set_style("whitegrid")

#%% [markdown]
# ## defining variables
x = np.linspace(-4,4,1000)
t = np.arange(0., 5., 0.2)

#%% [markdown]
# ## plotting of build in functions

plt.plot(x,np.sin(x))
plt.show()

#%% [markdown]

# ## subplot

fig, [ax1,ax2] = plt.subplots(2,1)
ax1.plot(x, np.sin(x))
ax2.plot(x, 2*np.sin(x-1))
plt.show()

# plt.subplot(2,1,1)
# ax1.plot(t,np.sin(t))
# plt.subplot(2,1,2)
# ax2.plot(t,np.cos(t))
# plt.show()


#%%

# important options
    #Labels
plt.plot(x,np.sin(x))
plt.ylabel('sin(x)')
plt.xlabel('x')

plt.title('My first plot')
plt.show()

    #Labels using latex

plt.plot(x,x**2)

# plt.rc('font', family='serif')
plt.title(r'$x^2$')
plt.show()

    #grid
plt.plot(x,x**2)
plt.grid(True)
plt.show()
    #format
# http://www.engineer101.com/matlab-plot-formatting/

plt.plot(x,np.sin(x),'m--+')
plt.show()



#plotting several funcs in one figure

plt.plot(t,np.sin(t),'r',label='sin')
plt.plot(t,np.cos(t),'y',label = 'cos')
plt.legend(loc='upper left')
plt.title('COS vs SIN')
plt.show()



# easy plotting of UDF

def lfunc(x):
    return 2*x+2



plt.plot(x,lfunc(x))
plt.show()
#easy plotting probability

#histogramm

np.random.seed(19680801)
mu, sigma = 1,2 
x = np.random.normal(mu, sigma, 10000)
y = np.random.normal(mu+.1, sigma, 20000)
    # the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.show()

#rugplot
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=1)
sns.rugplot(x, height=0.02, axis='x',alpha = 0.2)
plt.show()

#overlapping histogramms
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.3)
n, bins, patches = plt.hist(y, 50, normed=1, color='m', alpha=0.3)
plt.show()


#pmf: = Density / cdf:=distribution / ppf:=inverse distribution 
from scipy.stats import poisson
mu = 1
plt.plot(t,1-poisson.cdf(mu,t),label = 'Distribution')
plt.plot(t,poisson.pmf(mu,t),label = 'density')
plt.legend(loc='upper right')
plt.title('Poisson Verteilung mit ' + r'$\mu$=' + str(mu))
plt.grid(True)
plt.show()


P = np.arange(0,1,0.01)
plt.plot(P,poisson.ppf(P,mu))
plt.title('inverse Poisson Verteilung mit ' + r'$\mu$=' + str(mu))
plt.show()



