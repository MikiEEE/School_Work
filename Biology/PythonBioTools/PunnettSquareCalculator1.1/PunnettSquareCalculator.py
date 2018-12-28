import HelperFunctions as hp

# parent1 = input("Please Input Parent 1's Alleles: ")
# parent2 = input("Please Input Parent 2's Alleles: ")
#
# parent1 = "AabbcCDdEeFfHHIiLlmMnnJJ"
# parent2 = "aaBbccDDeeFFhhiiLlmmNnjj"

parent1 = "AabbcCDd"
parent2 = "aaBbccDd"

numOfParent = 2
potentialChild = list()
Genomes = dict()
potentialChild = hp.generateSinglePairs(len(parent1), parent1, parent2)
print(potentialChild)
potentialChild = [sorted(x) for x in potentialChild]
seperateTraits = hp.chunk(potentialChild, int(len(parent1)/2))

print('generateSinglePairs',potentialChild)
print('CHUNK',seperateTraits)

Traits = seperateTraits[0]
for x in range(1,int(len(parent1)/2)):
    Traits= hp.mix(Traits,seperateTraits[x])

del seperateTraits

Traits = hp.orderListsElements(int(len(parent1)/2), Traits)

keys = set(Genomes.keys())
for y in Traits:
    if y not in keys:
        Genomes[y] = 1
        keys.add(y)
    else:
        Genomes[y] += 1


print("#   Genome  Percentage")
index = 1
for x in Genomes.keys():
    print(str(index) + ".   " + str(x) + "      " + str((Genomes[x]/len(Traits)) * 100) + "%" )
    index+=1
