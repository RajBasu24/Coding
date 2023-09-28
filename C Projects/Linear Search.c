#include<stdio.h>
#include<stdlib.h>
int main()
{
	int *a,n,i,key;
	printf("Enter the size of array:");
	scanf("%d",&n);
	a=(int*)malloc(n*sizeof(int));
	printf("Enter the values of array:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Enter the value to be searched:");
	scanf("%d",&key);
	L_Search(a,n,key);
	free(a);
}

void L_Search(int *a,int num,int k)
{
	int i,c=0;
	for(i=0;i<num;i++)
	{
		if(a[i]==k)
		{
			c++;
			printf("Element found at %d",i+1);
			break;
		}
	}
	if(c==0)
		printf("\nElement not found");
}
