n=int(input("Enter the no:"))
temp=n
s=0
while(n>0):
    d=n%10
    s=s*10+d
    n=n//10
print("Reversed no is:",s)
if(temp==s):
    print("Entered no is Palindrome")
else:
    print("Entered no is not Palindrome")
