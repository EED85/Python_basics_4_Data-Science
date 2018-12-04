#Note : Paraemter do not need to be defined as string / Number

#positinal

def _print_(msg):
    print(msg)

_print_('h')

    #Return one value

def plusOne(no):
    return no +1

print(plusOne(1))

#keyword Parameter / default value / optional Parameter

def _key(msg = "Test"):
    print(msg)

_key() #prints default value
_key(msg = "a") #prints default value
_key('r')

    #check if an optional paramater was defined within function call

# return several values

#passing undefined number of Parameters in the function

#check datatype of input parameter