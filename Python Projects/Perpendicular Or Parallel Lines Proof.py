m1=float(input("Enter slope of 1st line:"))
c1=int(input("Enter intercept of 1st line:"))
m2=float(input("Enter slope of 2nd line:"))
c2=int(input("Enter intercept of 2nd line:"))
if(m1==m2):
    print("Parralel lines")
elif(m1*m2==-1):
    print("Perpendicular lines")
else:
    print("Neither of these")
