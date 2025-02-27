# Program to print an arithmetic progression series
a = int(input("Enter the first number of the series: "))
b = int(input("Enter the common difference of the series: "))
n = int(input("Enter the number of terms of the series :"))
print("The AP series from", a, "with common difference of", b, "with total of", n, "terms is")
for i in range(0, n):
    s = a + i * b
    print(s, end = " ")