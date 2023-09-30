import java.lang.*;
class Pat2
{
    public static void main(String args[])
    {
        Pat ob=new Pat();
        int n=Integer.parseInt(args[0]);
        ob.sum(n);
    }
}
class Pat
{
    void sum(int n)
    {
        for(int i=n-1;i>=0;i--)
        {
            for(int j=0;j<=i;j++)
                System.out.print("*" + " ");
            System.out.println();
        }
    }
}