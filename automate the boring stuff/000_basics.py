

# General characteristis of python

    # code intend is forced on loops / if statements ...


    #multiple assigment trick

a = 'A'
b = 'B'
a = 'A';b = 'B'
a,b = 'A','B'

b = a ; a = b
a,b = b,a

    #line break within code

long_str = 'Hello, ' + \
            'my name is '

    # Increment Variables / augmented assignment operators
    # https://docs.python.org/2.0/ref/augassign.html
I = 10
I += 1 #I = I + 1 -> I = 11
I -= 1 #I = I - 1 -> I = 10
I *= 2 #I = I *2 -> I = 20
I /= 2 #I = I/2 -> I = 10
I %= 3 #I = I % 3 -> I = 1



    # object oriented
    # every class has methods, less functions than in other o
    # languages

    # mutable and immutable
    # lista are mutable, strings are not
l = list('hello')
str1 = 'hel1lo'
l[1] = "H"
str1[1] = "H" # throws error

    #Note - mutable variables use references ...
l1 = list(range(5))
l2 = l1
l2[0] = -1 #l1 & l2 will be changed!!
l1


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

cat = ['fat','orange','loud']
cat.sort(key=len);cat

    #multiple assigment trick list
cat = ['fat','orange','loud']
size, color,dis = cat
 # dictonary

    #defining
myCat = {'size':'fat', 'color':'grey'}


    #comparing
myCat2 = { 'color':'grey', 'size':'fat'}
myCat == myCat2

# plotting
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show

plt.plot([1,2,3,4,5]) 
plt.show() 

#? Mising value / NaN ..