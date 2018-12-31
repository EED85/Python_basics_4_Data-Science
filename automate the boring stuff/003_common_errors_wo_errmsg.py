#FUNCTIONS
    # no return value defined
def _local():
    S = 2
print(_local())

#dic withount comma seperated
dic = ['a' 'b'] #-> only one item!

# change in a list, will change all refrenced lists ....
l1 = list(range(5))
l2 = l1
l2[0] = -1 #l1 & l2 will be changed!!
l1
    #use copy instead
import copy
l3 = copy.deepcopy(l1)

#Note - Lists are working different for mutable variables regrading local and global scopes (see refrence)!!!

def edit_list(l):
    l.append('a')

l2 = ['0']
edit_list(l2)
l2

    #use copy instead
import copy
l3 = copy.deepcopy(l2)

#sorting Lists in true alphabetic order

l = ['a','b','A','B']
l.sort() #sorts first the capital letters - B before a ..
l
l.sort(key=str.lower)
l

#NEVER call a variable str (or like another existing function)
l.sort(key=str.lower)
str = 'a'
l.sort(key=str.lower) #throws an error
del str
l.sort(key=str.lower)