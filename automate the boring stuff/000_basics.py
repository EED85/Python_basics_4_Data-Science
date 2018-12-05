

# General characteristis of python

    # code intend is forced on loops / if statements ...


    #multiple assigment trick

a = 'A'
b = 'B'
a = 'A';b = 'B'
a,b = 'A','B'

b = a ; a = b
a,b = b,a

    # Increment Variables / augmented assignment operators
    # https://docs.python.org/2.0/ref/augassign.html
I = 0
I = I +1
I += 1
I

    # object oriented
    # every class has methods, less functions than in other o
    # languages

# mutable and immutable
# lista are mutable, strings are not
l = list('hello')
str = 'hel1lo'
l[1] = "H"
str[1] = "H" # throws error

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
'll' in a
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
ll = [['a','b','c'],[1,2,3]]
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
l.index('A')
l.index('ff') # throws ValueError, if not within List

cat = ['fat','orange','loud']
size, color,dis = cat
    # methods
l.index('A')
l.append('E')
l.insert(0,'0')
l
l.remove('0')
l
l.sort(key=str.lower,true)



 


# plotting
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show

#? Mising value / NaN ..