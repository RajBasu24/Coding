# Print sum of all numbers within a given range
a = int(input("Enter the start of the range: "))
b = int(input("Enter the end of the range: "))
s = 0
for i in range(a, b + 1):
    s += i
print("Sum of all numbers in the given range are", s)