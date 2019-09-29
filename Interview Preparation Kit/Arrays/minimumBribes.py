
def sameOrNot( initial , current ):
        if( initial == current ):
            return 0

def checkList( current , value):
    for each in current:
        if( each[0] == value):
            return each[1]

def checkFromBack( initial , current ):

    for back in range(len(initial)-1,0,-1):
        if( initial[back][0] == current[back][0]):
            continue
        else:
            curIndex = checkList(current , initial[back][0])
            diff = initial[back][1] - curIndex
            if( diff > 2):
                return False
            else:
                for swap in range(initial[back][1],curIndex,-1):
                    temp = initial[swap][0]
                    initial[swap][0] = initial[swap-1][0]
                    initial[swap-1][0] = temp

                    temp = initial[swap][2]
                    initial[swap][2] = initial[swap-1][2]
                    initial[swap-1][2] = temp

                    initial[swap-1][2] += 1
                    if( initial[swap-1][2]  > 2):
                        return False
            back += 1

    return initial

                    




tests = int(input("Enter number of test cases : ") )

current = {}
order = []
output = []
for i in range(tests):
    t = int(input("enter t : "))
    order.append(t)
    current[t]=[[] for _ in range(t)]
    for j in range(t):
        current[t][j].append(int(input("enter val : ")))
        current[t][j].append(j)
        current[t][j].append(0)
print("current : \n" ,current )

for eachKey in order:
    initial = []
    for j in range(1,eachKey+1):
        initial.append([j,j-1,0])
        

    print("initial : \n" , initial)

    if ( current[eachKey] == initial ):
        output.append( sameOrNot( initial , current[eachKey] ) )
    else:
        result = checkFromBack( initial , current[eachKey] )
        print("result : \n",result)
        if( result == False):
            output.append("Too Chaotic")
        else:
            current[eachKey] = result
            count = 0
            for each in result:
                count += each[2]
            output.append(count)
    
print( "\n Output : " , output )