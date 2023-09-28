#include<stdio.h>
int main()
{
    int a,b,S,ch;
    printf("Enter the first number:");
    scanf("%d",&a);
    printf("Enter the second number:");
    scanf("%d",&b);
    S=a+b;
    printf("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division");
    printf("Enter your choice:");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1: S=a+b;
                printf("Addition of %d and %d is %d",a,b,S);
                break;
        case 2: S=a-b;
                printf("Subtraction of %d and %d is %d",a,b,S);
                break;
        case 3: S=a*b;
                printf("Multiplication of %d and %d is %d",a,b,S);
                break;
        case 4: S=a/b;
                printf("Division of %d and %d is %d",a,b,S);
                break;
        default: printf("Enter correct choice");
    }
}
