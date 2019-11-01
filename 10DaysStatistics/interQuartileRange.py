def calculateMedian( array ):
    length = len(array)
    if(length%2 == 0):
        array.sort()
        median = (array[length//2] + array[length//2-1])/2
    else:
        median = array[length//2]
    return median

def handleEvenLengthArray(array):

    temp = len(array)//2
    left = array[0:temp]
    right = array[temp:]

    q1 = calculateMedian( left )
    q2 = calculateMedian( array )
    q3 = calculateMedian( right )

    # print(q1,q2,q3)
    return [q1,q2,q3]

def handleOddLengthArray( array ):

    temp = len(array)//2
    # print(temp , len(array) )
    left = array[0:temp]
    right = array[temp+1:]

    q1 = calculateMedian(left)
    q2 = array[temp]
    q3 = calculateMedian(right)
    # print(q1,q2,q3)
    return [q1,q2,q3]

def getS( array , frequency):
    S = []
    for i in range(len(frequency)):
        temp = [array[i]]*frequency[i]
        S.extend(temp)    
    S.sort()

    return S

n = int(input())

if( n>=5 and n<=50):

    X = input().split(" ")
    X = [int(val) for val in X]

    F = input().split(" ")
    F = [int(val) for val in F]

    S = getS(X,F)
    # print(S)

    if(len(S)%2 == 0):
        output = handleEvenLengthArray(S)
    else:
        output = handleOddLengthArray(S)

    interquartilerange = round(float(output[2]-output[0]),1)

    print( interquartilerange )
