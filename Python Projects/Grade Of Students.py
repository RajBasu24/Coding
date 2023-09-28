Maths=int(input("Enter the marks of Maths:"))
Biology=int(input("Enter the marks of Biology:"))
History=int(input("Enter the marks of History:"))
English=int(input("Enter the marks of English:"))
Coms=int(input("Enter the marks of Coms:"))
sum=Maths+Biology+History+English+Coms
avg=sum/5
if(avg>=90):
    print("Grade=A")
elif(avg>=80 and avg<90):
    print("Grade=B")
elif(avg>=70 and avg<80):
    print("Grade=C")
elif(avg>=60 and avg<70):
    print("Grade=D")
else:
    print("Grade=F")
