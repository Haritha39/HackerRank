#include<stdio.h>
#include<string.h>


int main()
{
    int n , m , i = 0 ,j = 0 , max = -1 ;
    printf( " Enter Array size and No . of Operations : " );
    scanf("%d%d" , &n , &m );

    int arr[n+1] ;
    int opera[m][3] ;

    bzero( arr , sizeof(arr) );

    for( i = 1 ; i <= n ; i++ )
        printf(" %d " , arr[i] );

    for( i = 0 ; i < m ; i++)
    {
        for( j = 0 ; j < 3 ; j++ )
        {
            scanf("%d", &opera[i][j] );
        }
    }

    for( i = 0 ; i < m ; i++ )
    {
        for( j = 0 ; j < 3 ; j++ )
        {
            printf("%d " , opera[i][j] );
        }
        printf( "\n" );
    }

    for(i = 0 ; i < m ; i++ )
    {
        for( j = opera[i][0] ; j <= opera[i][1] ; j++ )
        {
            arr[j] = arr[j] + opera[i][2];
            if(max < arr[j] )
                max = arr[j] ;
            printf("arr[j] %d\n" , arr[j] );
        }
    }

    for( i = 1 ; i <= n ; i++ )
    {
        printf(" %d " , arr[i] );
    }

    printf("\n max : %d \n" , max );

    return 0;
}