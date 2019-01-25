import numpy as np
l = [] #list
l_cat = ['fat','orange','loud']
d = {} #dictonary
d_mycat = {'size':'fat', 'color':'grey'}
s_msg = 'Hello World' #string representing a message
s_str = ''
s_long = 'Hello World' + \
'How are u?'
s_long2 = '''Hello World
How are u?'''
name = 'EED'

L = len(s_long) # L := length of sth.

I,J,K = 0,0,0 #count variables (For Loop)

x = np.linspace(-4,4,100)
t = np.arange(0., 5, 0.2)
y = np.sin(x) #numpy vector
mat = np.eye(4) #Numpy Matrix
m,n = mat.shape #dimensins of matrix
print(name)