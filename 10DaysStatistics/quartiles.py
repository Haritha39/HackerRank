def calculateMedian( array ):
    length = len(array)
    if(length%2 == 0):
        array.sort()
        median = (array[length//2] + array[length//2-1])//2
    else:
        median = array[length//2]
    return median

def handleEvenLengthArray(array):

    temp = len(array)//2
    # print(temp)
    left = array[0:temp]
    right = array[temp:]

    q1 = calculateMedian( left )
    q2 = calculateMedian( array )
    q3 = calculateMedian( right )

    # print(q1,q3)

    return [q1,q2,q3]

def handleOddLengthArray( array ):

    temp = len(array)//2
    # print(temp)
    left = array[0:temp]
    right = array[temp+1:]

    q1 = calculateMedian(left)
    q2 = array[temp]
    q3 = calculateMedian(right)

    # print(q1,q2,q3)

    return [q1,q2,q3]


N = int(input()) 
quartiles = []
if( N >=5 and N <= 50 ):
    X = input().split(" ")
    X = [int(val) for val in X]
    X.sort()
    # print( X )

    if(N%2 == 0):
        quartiles = handleEvenLengthArray( X )
    else:
        quartiles = handleOddLengthArray( X )
    # print(quartiles)

    for q in quartiles:
        print(q)
    


# 3 7 8 5 12 14 21 15 18 14