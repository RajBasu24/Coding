n=int(input("Enter no of terms:"))
num=0
n1=0
n2=1
c=0
if(n<=0):
    print("Please enter a positive no")
elif(n==1):
    print("Fibonacci Series")
while(c<n):
    print(n1)
    num=n1+n2
    n1=n2
    n2=num
    c=c+1
