# Program to print all odd numbers within a given range
a = int(input("Enter the start of the range: "))
b = int(input("Enter the end of the range: "))
print("Odd numbers in the given range are")
for i in range(a, b + 1):
    if i % 2 == 0:
        pass
    else:
        print(i)