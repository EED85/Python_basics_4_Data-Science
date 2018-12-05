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


#sorting Lists in true alphabetic order

l = ['a','b','A','B']
l.sort() #sorts first the capital letters - B before a ..
l
l.sort(key=str.lower)
l