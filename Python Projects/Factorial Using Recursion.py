def recur_fact(n):
    if(n==1):
        return n
    else:
        return n*recur_fact(n-1)
num=int(input("Enter the no:"))
if(num<0):
    print("Factorial is not possible")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial is",recur_fact(num))
