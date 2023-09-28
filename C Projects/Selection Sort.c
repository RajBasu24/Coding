#include<stdio.h>
void S_Sort(int *a,int n)
{
	int i,j,min,flag,temp,k;
	for(i=0;i<n;i++)
	{
		min=i;
		flag=0;
		for(j=i+1;j<n;j+1)
		{
			if(a[j]<a[min])
			{
				min=a[j];
				flag++;
			}
		}
		if(min!=i)
		{
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
		if(flag==0)
			break;
		printf("The sorted array:");
		for(k=0;k<n;k++)
			printf("%d\n",a[k]);
	}
}
int main()
{
	int n,i;
	int *a;
	printf("Enter the size of array:");
	scanf("%d",&n);
	a=(int*)calloc(n,sizeof(int));
	for(i=0;i<n;i++)
	{
		printf("\nEnter:");
		scanf("%d",&a[i]);
	}
	S_Sort(a,n);
}

