for i in range(1,100):
    k=(int)(i+1/2)
    c=0
    for j in range(2,k):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i,end=' ')
