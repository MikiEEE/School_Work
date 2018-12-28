import HelperFunctions as hp

# parent1 = input("Please Input Parent 1's Alleles: ")
# parent2 = input("Please Input Parent 2's Alleles: ")
#
parent1 = "AabbcCDdEeFfHHIiLljjMm"
parent2 = "aaBbccDDeeFFhhiiLlJjmm"


# parent1 = "AabbcCDd"
# parent2 = "aaBbccDd"

potentialChild = list()
potentialChild = hp.generateSinglePairs(len(parent1), parent1, parent2)
Genomes = dict()
potentialChild = [''.join(sorted(x)) for x in potentialChild]
seperateTraits = hp.chunk(potentialChild, int(len(parent1)/2))

print('generateSinglePairs',potentialChild)
print('CHUNK',seperateTraits)

Traits = seperateTraits[0]

for x in range(1,int(len(parent1)/2)):
    Traits= hp.mix(Traits,seperateTraits[x])

del seperateTraits

for y in Traits:
    if Genomes.get(y, -1) == -1:
        Genomes[y] = 1
    else:
        Genomes[y] += 1

traitLength = len(Traits)
del Traits


print("#   Genome  Percentage")
index = 1
for x in Genomes.keys():
    print(str(index)".","  ",str(x),"      ",str((Genomes[x]/traitLength) * 100) + "%" )
    index+=1

del Genomes
