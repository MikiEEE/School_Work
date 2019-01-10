def mix(trait1,trait2):
    if trait2 == None:
        return trait1
    if len(trait2) != 4:
        raise ValueError
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

def makeOuput(TestInput, fileName):
    '''Testinput - output produced in generateSinglePairs()'''
    '''fileName - outputName'''
    with open(fileName,'w') as f:
        lines = [line + '\n' for line in createTraits(TestInput)]
        f.writelines(lines)
    return
