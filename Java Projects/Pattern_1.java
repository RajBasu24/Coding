import java.lang.*;
class Pat1
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
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=i;j++)
                System.out.print("*" + " ");
            System.out.println();
        }
    }
}