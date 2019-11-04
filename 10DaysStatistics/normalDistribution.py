import math

def calculateCumulativeNormalDistribution(mue,sigma,x):
    cumulative = 0.5*( 1+ math.erf((x-mue)/(sigma*math.sqrt(2))))
    return cumulative

mean , standardDeviation = [ int(val)  for val in input().split(" ")]
q1Value = float(input())
q2LowerRange , q2UpperRange = [int(val) for val in input().split(" ")]

q1Probability = calculateCumulativeNormalDistribution ( mean , standardDeviation ,q1Value)

q2Probability = calculateCumulativeNormalDistribution( mean , standardDeviation,q2UpperRange) - calculateCumulativeNormalDistribution(mean,standardDeviation,q2LowerRange)

q1Probability = round(q1Probability , 3)
q2Probability = round(q2Probability , 3)

print(q1Probability)
print(q2Probability)

