import java.lang.*;
class Sum
{
    public static void main(String args[])
    {
        int s=0;
        for(int i=0;i<args.length;i++)
        {
            int a=Integer.parseInt(args[i]);
            s=s+a;
        }
        System.out.println("Sum of the numbers is "+s);
    }
}