S = 1 #global
def _local():
    S = 2 #local
    return S

print(S)
print(_local())

#Use global variable within function

Glob = "global"

def _local_call_global():
    print(Glob)
_local_call_global()

#set exispting gobal variable

Glob = "global"
def _set_global():
    global Glob
    Glob = "global_def"

print(Glob)
_set_global()
print(Glob)

#Note - Lists are working different (see refrence)!!!

def edit_list(l):
    l.append('a')

l2 = ['0']
edit_list(l2)
l2




#define a global variable within function

def def_globvar():
    global Glob2
    Glob2 = "a"
def_globvar
print(Glob2)