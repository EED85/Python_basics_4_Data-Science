##% [markdown]

# # For Loops

total = 0
for I in range(5): # 0-4
    total = total +I
    print(I)
print(total)


for I in range(5,7): #5 & 6
    print(I)

#Step argument (Increment by)

for I in range(0,11,2): # 0 2 4 ... 10
    print(I)


for I in range(10,-1,-2): # 10 8 ... 0
    print(I)

#%% [markdown]

q = [x**2 for x in range(-4, 5)]
print(q)

#%% [markdown]
# Lists

l = list(range(0,11,2))
l
    #looping through lists
for i in range(len(l)):
    print (l[i])



l = ['a' , 'b']
len(l)
for i in range(len(l)):
    print(str(i) + ' : ' + l[i])
