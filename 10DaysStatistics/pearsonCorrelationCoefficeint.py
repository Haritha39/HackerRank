# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Pearson Correlation Coefficent

formula : r(x,y) = cov(x,y)/sd(x)sd(y)

covariance : cov(x,y) = 1/n *(sigmai (xi-xbar)(yi-ybar))

standard deviation: sd = sqrt(sigma(xi-x)^2/N-1)

"""
import math


def calculateSigmaXY(x,xmean,y,ymean):
    result = 0
    for i in range(len(x)):
        result = result + (x[i]-xmean)*(y[i]-ymean)

    return result

def calculateCovariance(x,y):
    xmean = sum(x)/len(x)
    ymean = sum(y)/len(y)

    numerator = calculateSigmaXY(x,xmean,y,ymean)

    covariance = numerator/len(x)

    print("covarinace : ",covariance)

    return covariance

def calculateStandardDeviation(var):
    result = 0
    varmean = sum(var)/len(var)
    for vari in var:
        result = result + ((vari-varmean)**2)

    sd = math.sqrt(result/(len(var)-1))

    print("standard deviation "%var,sd )
    return sd

def calculatePearsonCorrelationCoefficient( x,y ):
    cov = calculateCovariance(x,y)
    xsd = calculateStandardDeviation(x)
    ysd = calculateStandardDeviation(y)

    pcc = cov/(xsd * ysd)

    print("pearson : ",pcc)
    return pcc


n = int(input())
if( n < 10 or n > 100):
    exit()
X = [float(val) for val in input().split(" ")]
Y = [float(val) for val in input().split(" ")]

pearsonCofficient = round(calculatePearsonCorrelationCoefficient( X, Y ),3)

print(pearsonCofficient)

# 10
# 10 9.8 8 7.8 7.7 7 6 5 4 2 
# 200 44 32 24 22 17 15 12 8 4