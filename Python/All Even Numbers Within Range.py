# Program to print all even numbers within a given range
a = int(input("Enter the start of the range: "))
b = int(input("Enter the end of the range: "))
print("Even numbers in the given range are")
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)