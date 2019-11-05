import math

def calculateCumulativeNormalDistribution(mue,sigma,x):
    cumulative = 0.5*( 1+ math.erf((x-mue)/(sigma*math.sqrt(2))))
    return cumulative
    
mean , standardDeviation = [ int(val)  for val in input().split(" ")]
q1Value = int(input())
q2q3Value = int(input())

q1Probability = 1-calculateCumulativeNormalDistribution ( mean , standardDeviation ,q1Value)
q1Percentage = round(q1Probability*100,2)

q2q3Probability = calculateCumulativeNormalDistribution( mean , standardDeviation,q2q3Value )
q2Percentage = round((1-q2q3Probability)*100,2)
q3Percentage = round(q2q3Probability*100,2)

print( q1Percentage )
print( q2Percentage )
print( q3Percentage )


