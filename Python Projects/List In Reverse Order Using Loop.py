list=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    x=int(input("Enter:"))
    list.append(x)
for i in range(n-1,-1,-1):
    print(list[i])
