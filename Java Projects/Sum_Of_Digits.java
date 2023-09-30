import java.lang.*;
class digitSum
{
    public static void main(String args[])
    {
        Sumseries ob=new Sumseries();
        int n=Integer.parseInt(args[0]);
        ob.sum(n);
    }
}
class Sumseries
{
    int s=0;
    int d=0;
    void sum(int n)
    {
        while(n!=0)
        {
            d=n%10;
            System.out.println("Digit is "+d);
            s=s+d;
            n=n/10;
        }
        System.out.println("The sum of digits is "+s);
    }
}