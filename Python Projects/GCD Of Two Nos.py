def GCD(a, b):
    if (a>b):
        temp=b
    else:
        temp=a
    for i in range(1, temp+1):
        if((a%i==0)and(b%i==0)):
            gcd=i
    return gcd
n1=int(input("Enter the first number:"))
n2 =int(input("Enter the second number:"))
num=GCD(n1, n2)
print("GCD of two number is:",num)
