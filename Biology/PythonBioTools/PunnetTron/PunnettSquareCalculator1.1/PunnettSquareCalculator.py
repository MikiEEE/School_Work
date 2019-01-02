import HelperFunctions as hp
from functools import reduce
##ADD find phenotypes ,FindGenotype, Sexlink


def calculateGeneticTraits(parent1, parent2):
    potentialChild = list()
    potentialChild = hp.generateSinglePairs(parent1, parent2)
    potentialChild = [''.join(sorted(x)) for x in potentialChild]
    seperateTraits = hp.chunk(potentialChild, int(len(parent1)/2))
    Traits = hp.createTraits(seperateTraits)
    del seperateTraits
    Genomes = hp.buildGenome(Traits)
    del Traits
    return Genomes

def printGenomes(Genomes):
    traitLength = reduce(lambda x,y: x + y, Genomes.values())
    index = 1
    for x in Genomes.keys():
        print(str(index) + ".","  ",str(x),"      ",str((Genomes[x]/traitLength) * 100) + "%" )
        index+=1
    del Genomes
    return

if __name__ == '__main__':
    parent1 = "AabbcCDdEeFfHHIiLljjMm"
    parent2 = "aaBbccDDeeFFhhiiLlJjmm"
    # parent1 = "AABBCCDD"
    # parent2 = "AaBbCcDd"
    # parent1 = "AABb"
    # parent2 = "aaBB"
    genome = calculateGeneticTraits(parent1, parent2)
    printGenomes(genome)
