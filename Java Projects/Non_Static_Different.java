import java.lang.*;
class Print
{
    int b;
    void f1()
    {
        System.out.println("Number "+b);
    }
}
class Different
{
    public static void main(String args[])
    {
        Print ob=new Print();
        ob.b=7;
        ob.f1();
    }
}