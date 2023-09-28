n=int(input("Enter no of rows:"))
for i in range(0,n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(0,i+1):
        print("*",end=' ')
    print("\n")
