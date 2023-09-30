import java.util.*;
class Armstrong
{
    public static void main(String args[])
    {
        func ob=new func();
        int n=Integer.parseInt(args[0]);
        ob.sum(n);
    }
}
class func
{
    void sum(int n)
    {
        int s=0;
        int d=0;
        while(n!=0)
        {
            d=n%10;
            s=s+d;
            n=n/10;
        }
        System.out.println("The sum of digits is "+s);
        checkArmstrong(s);
    }
    void checkArmstrong(int n)
    {
        int s=0;
        int d=0;
        int copy=n;
        while(n!=0)
        {
            d=n%10;
            s=s+(int)Math.pow(d,3);
            n=n/10;
        }
        if(copy==s)
            System.out.println("The number is an Armstrong number");
        else
            System.out.println("The number is not an Armstrong number");
    }
}