def generateSinglePairs(length,ParentGenome1, ParentGenome2):
    assert len(ParentGenome1) == len(ParentGenome2)
    assert length > 0
    ResultHolder = list()
    for newAlleleStart in range(0,length,2):
        for parent1Allele in ParentGenome1[newAlleleStart:newAlleleStart+2]:
            for parent2Allele in ParentGenome2[newAlleleStart:newAlleleStart+2]:
                ResultHolder.append(parent1Allele + parent2Allele)
    return ResultHolder
