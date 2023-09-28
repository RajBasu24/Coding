n=int(input("Enter the range:"))
s=0
for i in range(1,n+1):
    print(i,end=' ')
    s=s+i
print("Sum of",n,"natural numbers is:",s)
