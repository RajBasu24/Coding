# Program to convert Celsius to Fahrenheit ans vice versa
n = float(input("Enter the temperature: "))
s = int(input("Enter 1 for Celsius, Enter 2 for Fahrenheit: "))
if s == 1:
    c = (n - 32) / 9 * 5
    print(n, "degree Fahrenheit is equals to", round(c, 2), "degree Celsius")
elif s == 2:
    f = (n / 5) * 9 + 32
    print(n, "degree Celsius is equals to", round(f, 2), "degree Fahrenheit")
else:
    print("Enter correct choice")