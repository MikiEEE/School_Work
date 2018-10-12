gene_sets = {
        'arsenic' : {1,2,3,4,5,6,8,12},
        'cadmium' : {2,12,6,4},
        'copper' : {7,6,10,4,8},
        'mercury' : {3,2,4,5,1}
}
## The Purpose of This Program is to generate a distance matrix of expression 
matrix = dict()

for metal1,set1 in gene_sets.items():
    matrix[metal1] = {}
    for metal2, set2 in gene_sets.items():
        if(metal1 != metal2):
            similarity = len(set1.intersection(set2))/len(set1.union(set2))
            matrix[metal1][metal2] = similarity
print(matrix.items())
