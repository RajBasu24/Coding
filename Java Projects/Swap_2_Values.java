import java.io.*;
class Swap
{
    public static void main(String args[])
    {
        DataInputStream ob=new DataInputStream(System.in);
        int a=0,b=0;
        try
        {
            System.out.println("Enter the value of a: ");
            int a=Integer.parseInt(ob.readLine());
            System.out.println("Enter the value of b: ");
            int b=Integer.parseInt(ob.readLine());
        }
        catch(Exception e)
        {
        }
        Swap1 ob=new Swap1();
        ob.swap(x,y);
    }
}
class Swap1
{
    void swap(int a,int b)
    {
        int t=0;
        t=a;
        a=b;
        b=t;
        System.out.println("The value of a is: "+a);
        System.out.println("The value of b is: "+b);
    }
}