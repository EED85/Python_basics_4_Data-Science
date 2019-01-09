#easy try except statement
def _devide(arg1 = 42,arg2 = 1):
    return arg1/arg2


try:
    N=_devide(42,0)
except:
    N = _devide(42,2)
print(N)





#only except for a specific errtype and print error Details
import sys
def _devide_err(arg1,arg2):
    try:
        I_arg2 = int(arg2)
        return arg1/arg2
    except ValueError:
        type, value, traceback = sys.exc_info()
        print("Err: arg2 is a string")
        print("DETAILS")
        print(value)
        print(traceback)
        print(type)
    print('a')
    


N=_devide_err(42,'h')

    # list of error types:
    # https://docs.python.org/2/library/exceptions.html

l = ["A" , "B"] 
l.index("a") # raises ValueError
string = 'Hello'
string.append(' World') # raises AttributeError

#go to statemnt

    #Does not exist
    #see https://www.quora.com/What-is-the-equivalent-of-goto-or-jump-command-in-python

#?print function name where error incurred


#raise statement - give back meaningful error messages for wrong user inputs

def div(arg1,arg2):
    if arg2 == 0:
        raise Exception("Durch null teilen nicht erlaubt")
    return arg1/arg2

print(div(1,0))


#assert statement - validate assumptions, that should always hold

sum_of_pos_no = 1 +2 +3 +4 -100
assert  sum_of_pos_no > 0 # var should have always a positive Value within a long program
print('a')

