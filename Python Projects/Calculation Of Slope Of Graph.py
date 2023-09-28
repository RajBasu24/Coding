l1=[]
m=int(input("Enter number of elements:"))
for i in range(0,m):
    x=int(input("Enter:"))
    l1.append(x)
l2=[]
n=int(input("Enter nnumber of elements:"))
for i in range(0,n):
    y=int(input("Enter:"))
    l2.append(y)
s=0
for i in range(0,m):
    s=s+(l1[i]*l2[i])
if(s>0):
    print("Positive")
else:
    print("Negative")
