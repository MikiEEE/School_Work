


TaxonomyOfPrimates = {
'Pongo abeli':'Hominoidea','Pan troglodytes':'Hominoidea',
'Hominoidea':'Simiiformes', 'Simiiformes':'Haplorrhini',
'Haplorrhini':'Primates', 'Tarsius tarsier':'Tarsiiformes',
'Tarsiiformes':'Haplorrhini', 'Strepsirrhini':'Primates',
'Lorisidae':'Strepsirrhini', 'Loris tardigradous':'Lorisidae',
'Lemuriformes':'Strepsirrhini','Allocebus trichotis':'Lemuriformes',
'Lorisiformes':'Strepsirrhini','Galago alleni':'Lorisiformes',
'Galago moholi':'Lorisiformes'
}

## Iterative way to find the Least Common Ancestor

def compareResults(result):
    temp = result[0]
    for x in range(1,len(result)):
        if temp == result[x]:
            continue
        else:
            return False
    return True

def getLCAParent(Taxonomy, taxa):
    result = taxa
    while not compareResults(result):
        for x in range(len(result)):
            if Taxonomy.get(result[x]) is not None:
                result[x] = Taxonomy.get(result[x])
    return result[0]


## Recursive Way
def getLCAParentRecursive(Taxonomy, taxa):
    if taxa[0] == None:
        return 'Primates'
    elif not compareResults(taxa):
        for x in range(len(taxa)):
            taxa[x] = Taxonomy.get(taxa[x])
        getLCAParentRecursive(Taxonomy,taxa)
    return taxa[0]

apes = list()
apes.append('Loris tardigradous')
apes.append('Galago alleni')
apes.append('Allocebus trichotis')

print(str(getLCAParent(TaxonomyOfPrimates,apes)))
print(str(getLCAParentRecursive(TaxonomyOfPrimates,apes)))
