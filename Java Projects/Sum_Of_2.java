import java.lang.*;
class Sum
{
    public static void main(String args[])
    {
        int S;
        if(args.length!=2)
            System.out.println("Please enter 2 numbers");
        else
        {
            int a=Integer.parseInt(args[0]);
            int b=Integer.parseInt(args[1]);
            S=a+b;
            System.out.println("Sum of "+a+" and "+b+" is "+S);
        }
    }
}