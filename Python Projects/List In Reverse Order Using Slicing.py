list=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    x=int(input("Enter:"))
    list.append(x)
print(list[::-1])
