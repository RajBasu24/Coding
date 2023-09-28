n=int(input("Enter number of elements:"))
list=[]
for i in range(0,n):
    x=int(input("Enter:"))
    list.append(x)
print("List is:",list)
l2=[]
for i in range(0,n):
    if list[i] not in l2:
        l2.append(list[i])
print("Removed list is:",l2)
