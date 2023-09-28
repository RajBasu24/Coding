#Unpacking of tuples
def unpackTuple():
    customerTuple=("Agni","Kolkata",28)
    print(customerTuple)
    (Name,Address,Age)=customerTuple
    print(Name)
    print(Address)
    print(Age)
#Combination of tuples and lists
def loadDatabase():
    #Create a tuple
    t1=("Agni","Kolkata",28)
    t2=("Palash","Mumbai",32)
    t3=("Rishi","Bangalore",50)
    customerDB=[t1,t2,t3]
    return customerDB
#Print the tuples in the lists
def display(customerDB):
    for i in range(0,len(customerDB)):
        print(customerDB[i])
#Search for a customer name in the list
def searchName(arg,customerDB):
    flag=False
    for i in range(0,len(customerDB)):
        Name,Adderess,Age=customerDB
        if Name==arg:
            flag=False
            break
        if(flag==True):
            print("Name found")
        else:
            print("Name not found")
#To insert the customer ID
def insertCustomer(argName,argAddress,argAge):
    argDB=loadDatabase()
    t=[argName,argAddress,argAge]
    argDB.append(t)
    return argDB
def start():
    customerDB=[]
    flag=True
    while(flag):
        print("Enter 1 to Insert\nEnter 2 to Display\nEnter 3 to Search\nEnter 4 to Delete")
    ch=int(input("Enter choice:"))
    if(ch==1):
        Name=input("Enter Name:")
        Address=input("Enter Address:")
        Age=input("Enter Age:")
        customerDB=insertCustomer(Name,Address,Age)
    elif(ch==2):
        display(customerDB)
    elif(ch==3):
        Name=input("Enter Name:")
        searchName(Name,customerDB)
    elif(ch==4):
        customerDB.pop()
