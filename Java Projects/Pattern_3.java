import java.lang.*;
class Pat3
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
        for(int i=0;i<n;i++)
        {
            for(int j=n-i;j>1;j--)
            {
                System.out.print(" ");
            }
            for(int j=0;j<=i;j++)
            {
                System.out.println("*" + " ");
            }
            System.out.println();
        }
    }
}