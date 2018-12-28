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

#Takes in Parentalal Genomes and generates Possible Pairs
def generateSinglePairs(length,ParentGenome1, ParentGenome2):
    assert len(ParentGenome1) == len(ParentGenome2)
    assert length > 0
    ResultHolder = list()
    for newAlleleStart in range(0,length,2):
        for parent1Allele in ParentGenome1[newAlleleStart:newAlleleStart+2]:
            for parent2Allele in ParentGenome2[newAlleleStart:newAlleleStart+2]:
                ResultHolder.append(parent1Allele + parent2Allele)
    return ResultHolder

def mix(trait1,trait2):
    childList = list()
    assert len(trait2) == 4
    for x in trait1:
            childList.append(x + trait2[0])
            childList.append(x + trait2[1])
            childList.append(x + trait2[2])
            childList.append(x + trait2[3])
    return childList
