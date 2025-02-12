# Program to find the roots of a quadratic equation
import math
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
if (b**2 - 4*a*c) < 0:
    print("The roots are imaginary")
else:
    r1 = (-b + math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    print("First root is", r1, "and second root is", r2)