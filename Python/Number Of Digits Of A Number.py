# Program to print the number of digits of a number
n = int(input("Enter the number: "))
temp = n
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits of", temp, "is", count)