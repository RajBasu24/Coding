n=int(input("Enter number of elements:"))
list=[]
for i in range(0,n):
    x=int(input("Enter:"))
    list.append(x)
l2=[i*i for i in list]
print("The array is:",l2)
