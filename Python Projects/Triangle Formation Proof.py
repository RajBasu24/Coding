x=int(input("Enter 1st side:"))
y=int(input("Enter 2nd side:"))
z=int(input("Enter 3rd side:"))
if(x+y>z):
    if(y+z>x):
        if(x+z>y):
            print("Forms triangle")
        else:
            print("Doesn't form triangle")
    else:
        print("Doesn't form triangle")
else:
    print("Doesn't form triangle")
