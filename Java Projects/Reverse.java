import java.util.*;
class func
{
    void rev(int n)
    {
        int copy=n;
        int r=0;
        int d=0;
        while(n!=0)
        {
            d=n%10;
            r=r*10+d;
            n=n/10;
        }
        System.out.println("The reverse of "+copy+" is "+r);
    }
}
class Reverse
{
    public static void main(String args[])
    {
        func ob=new func();
        int n=Integer.parseInt(args[0]);
        ob.rev(n);
    }
}