import math

def calculatespearsonRankCorrelationCofficient( x,y ):

    numerator = 0
    for i in range( len(x) ):
        numerator = numerator + math.pow(x[i][1]-y[i][1] , 2)
    numerator = 6 * numerator
    denominator = len(x)*(len(x)**2 - 1)
    result = 1 - ( numerator/denominator)

    return result


def calculateSigmaXY(x,xmean,y,ymean):
    result = 0
    for i in range(len(x)):
        result = result + (x[i]-xmean)*(y[i]-ymean)

    return result

def calculateCovariance(x,y):
    xmean = round(sum(x)/len(x),2)
    ymean = round(sum(y)/len(y),2)
    numerator = calculateSigmaXY(x,xmean,y,ymean)

    covariance = numerator/len(x)
    return covariance

def calculateStandardDeviation(var):
    result = 0
    varmean = round(sum(var)/len(var),2)
    for vari in var:
        result = result + ((vari-varmean)**2)

    sd = math.sqrt(result/(len(var)))
    return sd

def calculatePearsonCorrelationCoefficient( x,y ):
    cov = calculateCovariance(x,y)
    xsd = calculateStandardDeviation(x)
    ysd = calculateStandardDeviation(y)

    pcc = cov/(xsd * ysd)
    return pcc

def assignRanks( arr ):
    temp = arr
    temp = sorted(temp)
    result = []
    pos = 0
    for i in range(len(arr)):
        if( temp.count(arr[i]) == 1 ):
            pos = temp.index(arr[i])+1
        else:
            pos = temp.index(arr[i])
        result.append([arr[i],pos])
    
    return result

n = int(input())
if( n < 10 or n > 100):
    exit()
X = [float(val) for val in input().split(" ")]
Y = [float(val) for val in input().split(" ")]

if( len(X) == len(set(X)) and len(Y) == len(set(Y)) ):
    X = assignRanks(X)
    Y = assignRanks(Y)
    spearsonCofficient = round(calculatespearsonRankCorrelationCofficient( X , Y ),3)
    print( spearsonCofficient)
else:
    pearsonCofficient = round(calculatePearsonCorrelationCoefficient( X, Y ),3)
    print(pearsonCofficient)

# 10
# 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
# 200 44 32 24 22 17 15 12 8 4