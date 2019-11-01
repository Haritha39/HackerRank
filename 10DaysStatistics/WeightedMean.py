# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculateWeightedMean( values , weights ):

    """ 
    Formula :

        sigma i(values(i) * weights(i) )
        ________________________________
                sigma(weights)
    
    """
    numerator = 0
    for i in range(len(values)):

        numerator = numerator + (values[i]*weights[i])

    denominator = sum(weights)

    weightedMean = round(numerator / denominator,1)

    return weightedMean

    



N = int(input())

if( N >=5 and N <=50 ):
    
    X = input().split(" ")
    X = [int(val) for val in X]

    W = input().split(" ")
    W = [int(val) for val in W]

    weightedMean = calculateWeightedMean(X ,W)

    print(weightedMean)