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

#set existing gobal variable

Glob = "global"
def _set_global():
    global Glob
    Glob = "global_def"

print(Glob)
_set_global()
print(Glob)


#define a global variable within dunction

def def_globvar():
    global Glob2
    Glob2 = "a"
def_globvar
print(Glob2)