

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 's' is not defined



# strings in Python
a = 'hello'
b = "test"
c = a+b # concetant
d = a*3 # repeat

a[1] #returns second letter of hello

# ? line intend / Zeilenumbruch / einrücken
# substring
a[1:3]
# match
a.find('e')
# replace
a.replace('ll','LL')


# split,join,reverse, is*

# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3


    # print
    

    # ?regexpression



# basic math

2+2
5-3
3*7
3/4
3**2



# conversion

int(2.3)
int('2')
round(2.234,1) #one decimal

str(2.3)


#List
    #define
l = ['a','b','c']
        #List within a List
ll = [['a','b','c'],[1,,3]]
    #index
l[0:2] # keeps first & second (a , b)
l[0:] # equals l
l[0]
ll[0][1] # prints second element of first list
    #manipulate
l[2] = 'C'
l
l[0:2] = ['A','B']
l
    #delete
del l[1]
l

    #append
l + l
l*2
l.append('D')
l
    #match
'A' in l # case sensitive!
'a' in l 


 


# plotting
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show

#? Mising value / NaN ..