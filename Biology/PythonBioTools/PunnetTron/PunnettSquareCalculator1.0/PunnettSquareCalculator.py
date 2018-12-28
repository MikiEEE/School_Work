import pdb
def chunk(xs, n):
    '''Split the list, xs, into n chunks'''
    L = len(xs)
    assert 0 < n <= L
    s = L//n
    return [xs[p:p+s] for p in range(0, L, s)]

def orderListsElements(length, traitList):
    for d in range(0,len(traitList)):
        temp1 = list()
        temp = chunk(traitList[d], int(length))
        for x in range(0, len(temp)):
            temp[x] = ''.join(sorted(temp[x]))
        for x in temp:
            temp1 += x
        traitList[d] = ''.join(temp1)
    return traitList

def generateSinglePairs(length,ParentGenome1, ParentGenome2):
    assert len(ParentGenome1) == len(ParentGenome2)
    ResultHolder = list()
    for newAlleleStart in range(0,length,2):
        for parent1Allele in ParentGenome1[newAlleleStart:newAlleleStart+2]:
            for parent2Allele in ParentGenome2[newAlleleStart:newAlleleStart+2]:
                ResultHolder.append(parent1Allele + parent2Allele)
    return ResultHolder

def mix(trait1,trait2):
    childList = list()
    for x in trait1:
        for y in trait2:
            childList.append(x + y)
    return childList

# parent1 = input("Please Input Parent 1's Alleles: ")
# parent2 = input("Please Input Parent 2's Alleles: ")

# parent1 = "Aabb"
# parent2 = "aaBb"

# parent1 = "AabbcCDdEeFfHHIiLlmMnnJJ"
# parent2 = "aaBbccDDeeFFhhiiLlmmNnjj"
#
parent1 = "AabbcCDd"
parent2 = "aaBbccDd"

numOfParent = 2
potentialChild = list()
seperateGenomes = list()
seperateGenomesCount = list()
potentialChild = generateSinglePairs(len(parent1), parent1, parent2)
seperateTraits = chunk(potentialChild, int(len(parent1)/2))

for x in range(1,int(len(parent1)/2)):
    seperateTraits[0]= mix(seperateTraits[0],seperateTraits[x])

Traits = orderListsElements(int(len(parent1)/2), seperateTraits[0])

for y in Traits:
    if y not in seperateGenomes:
        seperateGenomes.append(y)
        seperateGenomesCount.append(0)
# def generateListOfIndependents()

for x in range(0,len(seperateGenomes)):
    for y in Traits:
        if seperateGenomes[x] == y:
            seperateGenomesCount[x]+=1


print("#   Genome  Percentage")
for x in range(0, len(seperateGenomes)):
    print(str(x + 1) + "   " + str(seperateGenomes[x]) + "      " + str((seperateGenomesCount[x]/len(Traits)) * 100) + "%" )

#print('Parent1 allele amount must be equal to Parent2 allele amount')
