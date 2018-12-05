#easy try except statement
def _devide(arg1 = 42,arg2 = 1):
    return arg1/arg2


try:
    N=_devide(42,0)
except:
    N = _devide(42,2)
print(N)


#?go to statemnt?

#? print Err.number / Statement)

#only except for a specific errtype

def _devide_err(arg1,arg2):
    try:
        I_arg2 = int(arg2)
        return arg1/arg2
    except ValueError:
        print("Err: arg2 is a string")
    print('a')
    


N=_devide_err(42,'h')



