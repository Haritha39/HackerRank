array = input().split(" ")
array1 = []
for i in array:
    array1.append(int(i))
# print(array1)

count = 0 
for i in range(len(array1)):
    temp = []
    for j in range(i,len(array1)):
        temp.append(array1[j])
    print(temp)
    mini = min(temp)
    minIndex = array1.index(mini)
    if( array1[minIndex] == array1[i] ):
        continue
    else:
        array1[minIndex],array1[i] = array1[i],array1[minIndex]
        count += 1
    print(array1)
print( count )