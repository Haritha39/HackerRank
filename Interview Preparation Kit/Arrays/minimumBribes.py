
def sameOrNot( initial , current ):
        if( initial == current ):
            return 0


tests = int(input("Enter number of test current : ") )

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

print( current )

for eachKey in order:
    initial = [[] for _ in range(eachKey)]
    for j in range(1,eachKey):
        initial[j].append(j)
        initial[j].append(j)
        initial[j].append(0)

    print(initial)

    if ( current == initial ):
        output.append( sameOrNot( initial , current[eachKey] ) )
        print(output)
            