# Program to print the grade of the marks
n = int(input("Enter the marks:"))
if n >= 90 and n <= 100:
    print("Grade is O")
elif n >= 80 and n <= 89:
    print("Grade is E")
elif n >= 70 and n <= 79:
    print("Grade is A")
elif n >= 60 and n <= 69:
    print("Grade is B")
elif n >= 50 and n <= 59:
    print("Grade is C")
elif n >= 40 and n <= 49:
    print("Grade is D")
elif n < 40:
    print("Grade is F")
else:
    print("Enter correct marks")