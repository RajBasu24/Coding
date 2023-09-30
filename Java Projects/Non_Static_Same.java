import java.lang.*;
class Same
{
    int a;
    void put()
    {
        System.out.println("Number "+a);
    }
    public static void main(String args[])
    {
        Same ob=new Same();
        ob.a=7;
        ob.put();
    }
}