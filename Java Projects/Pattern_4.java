import java.lang.*;
class Pat4
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
        for(int i=0;i<=n-1;i++)
        {
            for(int j=0;j<=i;j++)
            {
                System.out.print(" ");
            }
            for(int k=0;k<=n-1-i;k++)
            {
                System.out.println("*" + " ");
            }
            System.out.println();
        }
    }
}