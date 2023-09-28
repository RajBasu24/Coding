import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b**2-4*a*c
if(d==0):
    print("Roots are equal",-b/(2*a))
elif(d>0):
    r1=((-b+math.sqrt(d)/(2*a)))
    r2=((-b-math.sqrt(d)/(2*a)))
    print("root1=",r1)
    print("root2=",r2)
else:
    print("root1=",(-b/(2*a)),"+i",math.sqrt(abs(d)/(2*a)))
    print("root2=",(-b/(2*a)),"-i",math.sqrt(abs(d)/(2*a)))
