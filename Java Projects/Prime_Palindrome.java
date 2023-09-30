import java.util.*;
class func
{
    int prime(int n)
    {
        int c=0;
        for(int i=2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                c++;
            }
        }
        if(c!=0)
            return 0;
        else
            return 1;
    }
    int palin(int n)
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
        if(copy==r)
            return 1;
        else
            return 0;
    }
}
class primePalin
{
    public static void main(String args[])
    {
        func ob=new func();
        int l=Integer.parseInt(args[0]);
        int h=Integer.parseInt(args[1]);
        for(int i=l;i<=h;i++)
        {
            if(ob.prime(i)==1 && ob.palin(i)==1)
                System.out.println(i);
        }
    }
}