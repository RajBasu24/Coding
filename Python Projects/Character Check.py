ch=input("Enter the character:")
if(ord(ch)>=49 and ord(ch)<=58):
    print("Digit")
elif(ord(ch)>=65 and ord(ch)<=90):
    print("Upper Case")
elif(ord(ch)>=97 and ord(ch)<=122):
    print("Lower Case")
else:
    print("Special Character")
