#include<stdio.h>
#include<stdlib.h>

int main()
{
    long int n , v , len ;
    long int arr[99999];

    printf("enter n , v :: \n");
    scanf("%d%d",&n,&v);
    printf("%d,%d\n",n,v);

    // int *arr = (int *)malloc(n * sizeof(int) );
    printf("enter array elements\n");
    for( int i=0 ; i < n ; i++ )
    {
        scanf("%d",&arr[i]);
    }

    printf("displaying array elements\n");
    for( int i=0; i<n ; i++)
    {
        printf(" %d ",arr[i]);
    }
    printf("\n");

    int start = 0;
    int end = n-1;

    printf( "start : %d\nend : %d\narr[start] : %d\narr[end] = %d",start,end,arr[start],arr[end]);

    while( v > 0 )
    {
        arr[end+1] = arr[start];
        arr[start] = -1;
        start = start +1;
        end = end +1 ;
        v = v-1;
    }

    printf( "\nstart : %d\nend : %d\narr[start] : %d\narr[end] = %d",start,end,arr[start],arr[end]);
    printf("\nAfter 'l' rotations \n");
    for( int i = start ; i <= end ; i++)
    {
        printf(" %d " , arr[i] );
    }
}