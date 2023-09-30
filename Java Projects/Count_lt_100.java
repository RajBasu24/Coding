import java.lang.*;
class Count
{
    public static void main(String args[])
    {
        for(int i=0;i<args.length;i++)
        {
            int a=Integer.parseInt(args[i]);
            if(a<100)
                System.out.println(a);
        }
    }
}