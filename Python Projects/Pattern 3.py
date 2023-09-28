n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    c=i
    for p in range(1,i):
        print(c-1,end=' ')
        c=c-1
    print("\n")
