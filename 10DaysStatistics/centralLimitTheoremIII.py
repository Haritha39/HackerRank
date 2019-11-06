""" 
This problem deals with calculating the upper and lower values to get probability of 0.95 by giving mean and standard deviation.
sample mean is mean of population 
sample standard deviation  = given sd / sqrt(n)
z score = (X - mean) / (sd/sqrt(n))

"""

import math

n = int(input())
mean = int(input())
sd = int(input())
distributionPercentage = float(input())
zscore = float(input())

sample_sd = sd/math.sqrt(n)

A = round(mean-zscore*sample_sd,2)
B = round(mean+zscore*sample_sd,2)

print(A)
print(B)