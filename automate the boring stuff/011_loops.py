
I = 1
while I <= 5:
    print(I)
    I = I +1


I = 1
while True:
    print(I)
    I = I +1
    if I == 4:
        break

I = 1
while I <= 5:
    if I == 3:
        continue #3 is not printed. flops tehe followimg satments and starts a new iteration
    print(I)