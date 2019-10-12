
def sameOrNot( initial , current ):
        if( initial == current ):
            return 0

def checkList( current , value):
    for each in current:
        if( each[0] == value):
            return each[1]

def checkFromBack( initial , current ):

    back = len(initial)-2
    while( back != -1 ):
        print("back from prev ",back ," back " , back+1 , " initial ",initial)
        back += 1
        if( initial[back][0] == current[back][0]):
            back -= 2
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
            back -= 1
            

    return initial




tests = int(input("Enter number of test cases : ") )

current = []
order = []
output = []
for i in range(tests):
    t = int(input("enter t : "))
    order.append(t)
    current.append([t,[]])
    for j in range(t):
        current[i][1].append([int(input("enter val : ")),j,0])
# print("current : \n" ,current )

for eachOccur in current:
    initial = []
    for j in range(1,eachOccur[0]+1):
        initial.append([j,j-1,0])
<<<<<<< HEAD

    present = []
    present = eachOccur[1]    

    # print("initial : \n" , initial )
    # print("present : \n" , present )
=======
   
    print("initial : \n" , initial)
>>>>>>> 5ae14b810d1d56df306f9eb74f893ab606cbea8e

    if ( present == initial ):
        output.append( sameOrNot( initial , present ) )
    else:
        result = checkFromBack( initial , present )
        # print("result : \n",result)
        if( result == False):
            output.append("Too Chaotic")
        else:
            present = result
            count = 0
            for each in result:
                count += each[2]
            output.append(count)
    
print( "\n Output : " , output )