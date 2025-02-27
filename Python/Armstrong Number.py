# Program to check if a number is armstrong or not
n = int(input("Enter the number: "))
temp = n
s = 0
num = len(str(n))
while temp > 0:
    r = temp % 10
    s += r ** num
    temp //= 10
if n == s:
    print(s, "is an armstrong number")
else:
    print(s, "is not an armstrong number")