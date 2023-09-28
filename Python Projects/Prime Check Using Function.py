def isPrime(argNumber):
    flag=True
    for i in range(2,argNumber):
        if argNumber%i==0:
            flag=False
            break
        return flag
    