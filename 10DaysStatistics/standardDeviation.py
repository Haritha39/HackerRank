
""" Standard Deviation Formula : squareroot( summationof((xi - mue)^2) / N)"""
import math

def calculateMean( array ):

    mean = 0
    for val in array:
        mean = mean + val
    mean = mean/len(array)
    return mean

def sumOfSquaredDistanceFromMean( array , mean):

    numerator = 0
    for each in array:
        numerator = numerator + (each-mean)**2
    
    return numerator



N = int(input())

if( N >=5 and N <=100):

    X = input().split(" ")
    X = [int(val) for val in X]

    mean = calculateMean(X)
    numerator = sumOfSquaredDistanceFromMean( X , mean)
    
    standardDeviation = round(math.sqrt(numerator / N) ,1)

    print( standardDeviation )

