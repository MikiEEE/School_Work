import pdb
from functools import reduce

def chunk(xs, n):
    '''Split the list, xs, into n chunks'''
    L = len(xs)
    assert 0 < n <= L
    s = L//n
    return [xs[p:p+s] for p in range(0, L, s)]

#Takes in Parentalal Genomes and generates Possible Pairs
def generateSinglePairs(ParentGenome1, ParentGenome2):
    '''Takes in Parentalal Genomes and generates Possible Pairs'''
    if  len(ParentGenome1) != len(ParentGenome2):
        raise ValueError('Lengths of Parental Genomes must be the same.')
        return []
    length = len(ParentGenome1)
    ResultHolder = list()
    for newAlleleStart in range(0,length,2):
        for parent1Allele in ParentGenome1[newAlleleStart:newAlleleStart+2]:
            for parent2Allele in ParentGenome2[newAlleleStart:newAlleleStart+2]:
                ResultHolder.append(parent1Allele + parent2Allele)
    return ResultHolder

def mix(trait1,trait2):
    if len(trait2) != 4:
        raise ValueError('length of Trait2 must be equal t 4')
    if trait1 == None:
        return trait2
    childList = list()
    for x in trait1:
        childList.append(x + trait2[0])
        childList.append(x + trait2[1])
        childList.append(x + trait2[2])
        childList.append(x + trait2[3])
    return childList

def createTraits(seperateTraits):
    result = seperateTraits[0]
    for alleles in seperateTraits[1:]:
        result = mix(result, alleles)
    return result

def buildGenome(Traits):
    Genomes = dict()
    for y in Traits:
        if Genomes.get(y, -1) == -1:
            Genomes[y] = 1
        else:
            Genomes[y] += 1
    return Genomes
