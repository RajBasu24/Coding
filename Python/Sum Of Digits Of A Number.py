# Program to print the sum of digits of a number
n = int(input("Enter the number: "))
n = abs(n)
temp = n
s = 0
while n > 0:
    r = n % 10
    s = s + r
    n //= 10
print("Sum of digits of", temp, "is", s)