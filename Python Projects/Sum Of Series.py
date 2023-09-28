def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter value of x:"))
r=int(input("Enter the range:"))
s=0
v=1
for i in range(0,r):
    c=fact(v)
    d=n**v
    c=d/c
    if(i%2!=0):
        s=s-c
    else:
        s=s+c
    v=v+2
print(s)
