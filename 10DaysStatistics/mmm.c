#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>

int main() {

    int N , count = 0  , i = 0 , j = 0 , temp = 0 , max = 0 , num = 0 , mode = 0 , mean , median ;
    printf( "Enter the array length  : ");
    scanf( " %d " , &N ) ;
    printf( " \n N : %d " , N );
    if( N < 10 || N > 2500 )
    {
        exit(1);
    }
   
    int arr[N] ;

    for(  i = 0 ; i < N ; i++ )
    {
      scanf(" %d ", &arr[i]);
      count = count + arr[i];
    }

    mean = count / N ;

    printf( "mean : %d\n" , mean );

    for( i = 0 ; i < N ; i++ )
    {
        for( j = i ; j < N ; j++ )
        {
            if( arr[i] >= arr [j] )
            {
                temp = arr[i] ; 
                arr[i] = arr[j] ;
                arr[j] = temp;
            }
            else
            {
                continue ;
            }
        }
    }
    for( i = 0 ; i < N ; i++ )
    {
        printf("'%d' " , arr [ i ] );
    }

    if( N/2 == 0)
    {
        median = ( arr[N/2 - 1] + arr[N/2] )/2;
    }
    else
    {
        median = ( arr[N/2] );
    }

    printf(" median : %d\n" , median );

    for( i = 0 , j = 0 , count = 0 ; i < N ; i++ )
    {
        num = arr[i] ;
        while(arr[j++] == num)
        {
            count++;
        }
        if( count > max )
        {
            max = count ;
        }
    }

    if( max == 1 )
        printf( " mode : %d\n" , arr[0] );
    else
        printf( " mode : %d\n" , num ) ;

    return 0;

}