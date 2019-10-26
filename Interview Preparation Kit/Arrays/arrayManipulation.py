inputVals = input().split(" ")
arraySize = int(inputVals[0])
tests = int(inputVals[1])

array = [0 for i in range(arraySize+1)]
print(array)
testsArray = []
for i in range(tests):
    temp = input().split(" ")
    temp = [int(j) for j in temp]
    testsArray.append(temp)
print( testsArray )

for each in testsArray:
    a = each[0]
    b = each[1]
    k = each[2]

    for i in range(a,b+1):
        array[i] += k
    print(array)

array.remove(array[0])
print("\n\n :: ", array )
output = max(array)
print(output)
