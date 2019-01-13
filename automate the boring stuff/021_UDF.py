#Note : Paraemter do not need to be defined as string / Number

#positinal

def _print_(s_msg):
    print(s_msg)

_print_('h')

    #Return one value

def plusOne(no):
    return no +1

print(plusOne(1))

#keyword Parameter / default value / optional Parameter

def _key(s_msg = "Test"):
    print(s_msg)

_key() #prints default value
_key(s_msg = "a") #prints default value
_key('r')

# ?Keyword and positional parameters

    #check if an optional paramater was defined within function call



# return several values

#passing undefined number of Parameters in the function

#check datatype of input parameter

    # Number
def _devide_err(arg1,arg2):
    try:
        I_arg2 = int(arg2)
        return arg1/I_arg2
    except ValueError:
        print("Err: arg2 is a string")
    


N=_devide_err(42,'h')