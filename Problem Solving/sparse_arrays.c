#include<stdio.h>
#include<string.h>

void print( char strArray[][100] , int len)
{
    for( int i = 0 ; i<len;i++)
    {
        printf(" %s ",strArray[i]);
    }
}

int matchStrings( char str1[100] , char str2[100])
{
    if( strcmp(str1 , str2) ==0 )
    {
        return 0;
    }
    else
    {
        return 1;
    }
    
}

int main()
{
    int n , q ,ret;

    printf("\nenter n :: ");
    scanf("%d",&n);

    char strings[n][100];

    printf("\nenter array of strings : ");

    for( int i = 0 ;i <n ;i++)
    {
        scanf("%s",strings[i]);
    }

    print(strings , n);

    printf("\nenter q :: ");
    scanf("%d",&q);

    char queries[q][100];

    printf("\nenter array of queries : ");

    for( int i = 0 ;i <q ;i++)
    {
        scanf("%s",queries[i]);
    }

    print(queries , q);

    char result[q];
    for ( int i =0 ;i<q;i++)
    {
        result[i] = 0;
    }

    for( int i=0 ;i<q ;i++)
    {
        for( int j =0 ;j <n;j++)
        {
            ret = matchStrings( strings[j] , queries[i]);
            if( ret == 0 )
            {
                result[i]++;
            }
        }
    }

    printf( "\nresult array : ");
    for( int i=0 ;i<q;i++)
    {
        printf(" %d ",result[i]);
    }

}