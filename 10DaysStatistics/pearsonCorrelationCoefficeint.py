# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Pearson Correlation Coefficent

formula : r(x,y) = cov(x,y)/sd(x)sd(y)

covariance : cov(x,y) = 1/n *(sigmai (xi-xbar)(yi-ybar))

standard deviation: sd = sqrt(sigma(xi-x)^2/N)

"""
import math


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


n = int(input())
if( n < 10 or n > 100):
    exit()
# X = [float(val) for val in input().split(" ")]
# Y = [float(val) for val in input().split(" ")]
x = input().split(" ")
X =[]
for each in x:
    val = float(each)
    X.append(val)

y = input().split(" ")
Y =[]
for each in y:
    val = float(each)
    Y.append(val)


pearsonCofficient = round(calculatePearsonCorrelationCoefficient( X, Y ),3)

print(pearsonCofficient)

# 10
# 10 9.8 8 7.8 7.7 7 6 5 4 2 
# 200 44 32 24 22 17 15 12 8 4