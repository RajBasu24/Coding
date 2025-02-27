# Program to check if a number is palindrome or not
n = int(input("Enter the number: "))
temp = n
s = 0
while temp > 0:
    r = temp % 10
    s = s * 10 + r
    temp //= 10
if n == s:
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")