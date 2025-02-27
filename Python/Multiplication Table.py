# Program to print the multiplication table of a number
n = int(input("Enter the number: "))
print("The multiplication table for", n, "is")
for i in range(1, 11):
    print(n, "*", i, "=", n * i)