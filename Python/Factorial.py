n = int(input("Enter the number: "))
s = 1
for i in range(1, n + 1):
    s *= i
print("The factorial is", s)