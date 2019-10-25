def calculateMean( array ):

    mean = 0
    # mean = (mean + val for val in array)/len(array)
    for val in array:
        mean = mean + val
    mean = mean/len(array)
    return mean

def calculateMedian( array ):
    length = len(array)
    if(length%2 == 0):
        array.sort()
        median = (array[length//2] + array[length//2-1])/2
    else:
        median = array[length/2]
    return median

def calculateMode( array ):

    mode = -1
    for val in array:
        mode = val if array.count(val) > array.count(mode) else mode
    return mode



N = int(input())

if( N >= 10 and N <= 2500 ):

    X = input().split(" ")
    X = [int(n) for n in X]

    mean = calculateMean(X)
    median = calculateMedian(X)
    mode = calculateMode(X)

    print( mean )
    print( median )
    print( mode )


# print( X if X else False)