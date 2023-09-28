def isPrime(argNumber):
    flag=True
    for i in range(2,argNumber):
        if argNumber%i==0:
            flag=False
            break
        return flag
def primeFactGen(argNumber):
    if isPrime(argNumber)==True:
        print(argNumber)
    else:
        for i in range(2,argNumber):
            if isPrime(i)==True and argNumber%i==0:
                print(i)
