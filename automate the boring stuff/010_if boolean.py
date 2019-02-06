a = 42==42
print(a)
b = 42!=42
c = 42>=40
d = b and c
print(c)
print(b)
name = "Alice"
if name == "Alice":
    print('hi ' + name)
pwd = "sword"
if pwd == "sword":
    print ("Access")
else:
    print("Denied")

if name == "Alice":
    print("A")
# elif name == "Bob":
#     print("B")
else:
    print("else")

#%% [markdown]

# # shortcut for if-else
# a will be assigend 1
a = 0 if 1 == 21 else 1 
