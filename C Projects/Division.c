#include<stdio.h>
int main()
{
    int x,y,S;
    printf("Enter first number:");
    scanf("%d",&x);
    printf("Enter second number:");
    scanf("%d",&y);
    S=x/y;
    printf("Division of %d and %d is %d",x,y,S);
    return 0;
}
