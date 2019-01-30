import time
t0 = time.clock()
time.sleep(10)
t1 = time.clock()
print('about ' + str(round(t1-t0)) + ' seconds left')
print (time.strftime("%H:%M:%S", time.gmtime(t1-t0)))