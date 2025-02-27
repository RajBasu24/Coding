# Program to create a fibonacci series upto n
n = int(input("Enter the range of the fibonacci series: "))
a = 0
b = 1
print("The fibonacci series is")
print("0\n1")
for i in range(0, n - 2):
    temp = a + b
    print(temp)
    a = b
    b = temp