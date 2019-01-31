import time
t0 = time.clock()
time.sleep(10)
T = time.clock()
print('about ' + str(round(T-t0)) + ' seconds left')
print (time.strftime("%H:%M:%S", time.gmtime(T-t0)))