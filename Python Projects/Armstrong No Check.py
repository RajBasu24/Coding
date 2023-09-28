num=int(input("Enter the no:"))
sum=0
temp=num
while(temp>0):
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if(num==sum):
    print(num,"is Armstrong")
else:
    print(num,"is not Armstrong")
