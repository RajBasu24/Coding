# Program to find the greatest of 3 numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a > b and a > c:
    print ("Greatest number is",a)
elif b > c and b > a:
    print("Greatest number is",b)
elif c > a and c > b:
    print("Greatest number is",c)
else:
    print("All numbers are equal")