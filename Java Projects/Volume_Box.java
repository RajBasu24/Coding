import java.io.*;
class Box1
{
    public static void main(String args[])
    {
        float a=0,b=0,c=0;
        DataInputStream ob=new DataInputStream(System.in);
        try
        {
            System.out.println("Enter Depth:");
            a=Float.parseFloat(ob.readLine());
            System.out.println("Enter Height:");
            b=Float.parseFloat(ob.readLine());
            System.out.println("Enter Width:");
            c=Float.parseFloat(ob.readLine());
        }
        catch(Exception e)
        {
        }
        Box2 ob1=new Box2();
        System.out.println("The volume of the box is: "+ob.vol(a,b,c));
    }
}
class Box2
{
    float vol(float a,float b,float c)
    {
        float x=a;
        float y=b;
        float z=c;
        float v=x*y*z;
        return v;
    }
}