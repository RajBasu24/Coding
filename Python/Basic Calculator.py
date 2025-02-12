# Program to create a basic calculator
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = int(input("1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for Floor Division\n6 for Exponentiation\n7 for Modulus\nEnter your choice:"))
if c == 1:
    sum = a + b
elif c == 2:
    sum = a - b
elif c == 3:
    sum = a * b
elif c == 4:
    sum = a / b
elif c == 5:
    sum = a // b
elif c == 6:
    sum = a ** b
elif c == 7:
    sum = a % b
else:
    print("You have entered wrong input")
    exit()
print("The answer is", sum)