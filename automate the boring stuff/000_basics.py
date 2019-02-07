#%% [markdown]
# # Used packages
import time
import datetime
import re


#%% [markdown]
# # General characteristis of python

# ## code intend is forced on loops / if statements ...


 # ## multiple assigment trick

a = 'A'
b = 'B'
a = 'A';b = 'B'
a,b = 'A','B'

b = a ; a = b
a,b = b,a

#%% [markdown]
 # ## line break within code only
a = '1' + '2' + '3' + \
    '4' + '5'
print(a)
s_long = 'Hello, ' + \
            'my name is '
print(s_long)
#%% [markdown]
# ## defining long strings with line break within string and code
s_long2 = '''uhsdfuhsdf
dfödslfjlf'''
print(s_long2)

#%% [markdown]


    # Increment Variables / augmented assignment operators
    # https://docs.python.org/2.0/ref/augassign.html
I = 10
I += 1 #I = I + 1 -> I = 11
I -= 1 #I = I - 1 -> I = 10
I *= 2 #I = I *2 -> I = 20
I /= 2 #I = I/2 -> I = 10
I %= 3 #I = I % 3 -> I = 1

#%% [markdown]

    # object oriented
    # every class has methods, less functions than in other o
    # languages

# ## mutable and immutable
    # lists are mutable, strings are not
l = list('hello')
str1 = 'hel1lo'
l[1] = "H"
str1[1] = "H" # throws error

#%% [markdown]
#    ##Note - mutable variables use references ...
l1 = list(range(5))
print(l1)
l2 = l1
l2[0] = -1 #l1 & l2 will be changed!!
print(l1)

#%% [markdown]
# # strings in Python
# ## Use either ' or "
a = 'hello'
b = "test"

#%% [markdown]
# ## CONCATENATE
c = a+b
print(c)
#%% [markdown]
# ## repeat
d = a*3
print(d)

#%% [markdown]
# ## Indexing
a[1] #returns second letter of hello

#%% [markdown]
# ### substring
a[1:3]
#%% [markdown]
# ## important methods
# ### match
a.find('e')
'll' in a
#%% [markdown]
# ### replace
a.replace('ll','LL')

#%% [markdown]

# split,join,reverse, is*

# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3

#%% [markdown]
#    ## print
msg= "Hello"
msg1 = "!"
n=23
print('%s world%s' %(msg,msg1))

print('{_1} - {_2} - {_1}'.format(_1=msg,_2=n))
print('{} - {}'.format(msg,n))

#%% [markdown]

# ## format strings
# [link](https://pyformat.info/)
# ```python
# d:= integer
# f:= float
# s:= string
# ```
# https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
 # ### format numbers

print('{:d}'.format(42))
print('{:.2f}'.format(452.345))
print('{:.2f} €'.format(100.34))
print('{:04d}'.format(1))

#%% [markdown]
# ### align center -> does not work in vsc?
print('{:^20}'.format('test'))


#%% [markdown]
# ### Datetime
# http://strftime.org/

today = datetime.date.today()
print(today)
print('{:%Y}'.format(today))
print(f"{today:%B %d, %Y}")


#%% [markdown]
    # ?regexpression
#import re

#%% [markdown]
# basic math

2+2
5-3
3*7
3/4
3**2 #power exponent
4%3 #-> 1 (division remainder / Rest)



# conversion

int(2.3)
int('2')
round(2.234,1) #one decimal

print(str(2.3))


#List
    #define
l = ['a','b','c']
l1 = list(range(5))
        #List within a List
ll = [['a','b','c'],[1,2,3]]
l2 = [  'hello',
        'you']
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

    #comparing lists

list(range(2)) == [1,0]
    #no short cut for an Element by ELement comparison
    #match
'A' in l # case sensitive!
'a' in l 
l.index('A')
l.index('ff') # throws ValueError, if not within List


    # other methods
l.index('A')
l.append('E')
l.insert(0,'0')
l
l.remove('0')
l = ['A','b','B','C','D']
l.sort() #uses ASCII Sort (meaning Capital Letters before small letters)
l.sort(key=str.lower);l
l.sort(key=str.lower,reverse=True);l

l_cat = ['fat','orange','loud']
l_cat.sort(key=len);l_cat

    #multiple assigment trick list

size, color,dis = l_cat
 # dictonary

    #defining
d_mycat = {'size':'fat', 'color':'grey'}

d_mycat.setdefault('age',8) #adds new key age with the value 8
d_mycat.setdefault('size','thin') #nothin happens as key size already exists

#basic information
    
    #comparing
d_mycat2 = { 'color':'grey', 'size':'fat'}
d_mycat == d_mycat2

    #indexing

d_mycat.get('size',0) # returns 0, if size does not exist
d_mycat['size']

d_mycat.get('NaN',0)

    #loop
for key in d_mycat.keys():
    print(key)
for value in d_mycat.values():
    print(value)
for item in d_mycat.items():
    print(item)
    print('Key of item is : ' +  item[0])
    print('value of item is : ' +  item[1])

    #check for keys
"color" in d_mycat2

    #count charracters with dictionaries
s_msg = 'Hello WorLd'
count = {}
for c in s_msg.lower():
    c
    count.setdefault(c,0)
    count[c] = count[c] +1
    

# @:plotting
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show

plt.plot([1,2,3,4,5]) 
plt.show() 

#? Mising value / NaN ..

#%%
