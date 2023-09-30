import java.io.*;
class bankAcc
{
    public static void main(String args[])
    {
        String name;
        double balance=0.0,dep=0.0,with=0.0;
        DataInputStream ob=new DataInputStream(System.in);
        try
        {
            System.out.println("Enter your name: ");
            name=ob.readLine();
            System.out.println("Enter your balance: ");
            balance=Double.parseDouble(ob.readLine());
            System.out.println("Enter the amount to be deposited: ");
            dep=Double.parseDouble(ob.readLine());
            System.out.println("Enter the amount to be withdrawn: ");
            with=Double.parseDouble(ob.readLine());
        }
        catch(Exception e)
        {
        }
        func ob1=new func();
        ob1.deposit(balance,dep);
        ob1.withdraw(balance,with);
    }
}
class func
{
    double balance,d,w;
    void deposit(double b,double db)
    {
        balance=b;
        d=balance+db;
        System.out.println("The balance after deposit is: "+d);
    }
    void withdraw(double b,double wb)
    {
        balance=b;
        w=wb;
        if(balance<w)
        {
            System.out.println("Insufficient balance");
        }
        else
        {
            balance=balance-w;
            System.out.println("The balance after withdrawal is: "+balance);
        }
    }
}