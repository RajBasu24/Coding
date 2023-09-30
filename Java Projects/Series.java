import java.lang.*;
class Series
{
    void sum(int n)
    {
        int s=0;
        for(int i=1;i<=n;i++)
        {
            if(i%2==0)
                s=s-i;
            else
                s=s+i;
        }
        System.out.println("The sum is "+s);
    }
}
class Series1
{
    public static void main(String args[])
    {
        Series ob=new Series();
        int n=Integer.parseInt(args[0]);
        ob.sum(n);
    }
}