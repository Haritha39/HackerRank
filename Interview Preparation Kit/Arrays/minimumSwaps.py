""" Swap the smallest number with starting index of remaining array
Swap the largest number with ending index of remaining array """

def swap( array , mini_index ,mini_swap_index, maxi_index ,maxi_swap_index ):
    count = 0

    if( mini_index != mini_swap_index ):

        temp = array[mini_index]
        array[mini_index] = array[mini_swap_index]
        array[mini_swap_index] = temp
        # print("min ", array )
        count = count + 1
    
    if( maxi_index != maxi_swap_index ):
        temp = array[maxi_index]
        array[maxi_index] = array[maxi_swap_index]
        array[maxi_swap_index] = temp
        # print( "max ", array )
        count = count + 1

    return count


# Calculates smallest and largest number and returns their indices in array

def get_mini_maxi(array, start , end ):

    # print( start , end )
    mini = 999999
    maxi = 0
    for i in range( start , end+1):
        # print( i )
        if( array[i] < mini ):
            mini = array[i]
            mini_index = i
        if( array[i] > maxi ):
            maxi = array[i]
            maxi_index = i
    return [ mini_index , maxi_index ]


if( __name__ == "__main__"):
    n = int(input())

    array = []
    mini = 999999
    maxi = 0

    array = input()
    array = array.split(" ")
    temp = array
    array = []
    for each in temp:
        array.append( int(each))
    print( array)
    

    # for i in range(n):
    #     array.append(int(input()))

    # l = n-1
    # swap_count = 0
    # for i in range(n):
    #     if( i >= n/2 ):
    #         break
    #     minmax = get_mini_maxi( array , i , l )
    #     # print( minmax )
    #     # print( minmax[0] , i , minmax[1] , l )
    #     swap_count = swap_count + swap( array , minmax[0] , i , minmax[1] , l )
    #     # print("swap_count : ", swap_count )
    #     l=l-1

    # print( swap_count )

        