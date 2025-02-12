# Program to print a star pattern
a = int(input("Enter the number of rows:"))
for i in range(0, a):
    for j in range(0, i + 1):
        print("* ", end = "")
    print("")