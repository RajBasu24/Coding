# Program to find the bill amount after discount
a = float(input("Enter the total amount:"))
if a < 0:
    print("Enter correct amount")
    exit()
elif a <= 1000:
    s = a - (a * 10 / 100)
elif a > 1000 and a <= 5000:
    s = a - (a * 20 / 100)
elif a > 5000 and a <= 10000:
    s = a - (a * 30 / 100)
elif a > 10000:
    s = a - (a * 50 / 100)
print("Amount after discount is", s)