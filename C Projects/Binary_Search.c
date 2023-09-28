#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *arr;
    int n,i,l,u,k;
    printf("Enter the size of array:");
    scanf("%d",&n);
    arr=(int*)malloc(n*sizeof(int));
    printf("Enter the elements:");
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("Enter the item to be searched:");
    scanf("%d",&k);
    l=0;
    u=n-1;
    B_Search(arr,n,k);
}
B_Search(int *arr,int n,int k)
{
    int l=0;
    int u=n-1;
    int mid=0;
    while(l<u)
    {
        mid=(l+u)/2;
        if(arr[mid]==k)
        {
            printf("Element found at %d position:",(mid+1));
            break;
        }
        else if(arr[mid]>k)
            u=mid-1;
        else
            l=mid+1;
    }
    if(l>u)
        printf("Element not found");
}
