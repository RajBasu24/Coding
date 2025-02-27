# Program to print the reverse of a number
n = int(input("Enter the number: "))
temp = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n //= 10
print("Reverse number of", temp, "is", rev)