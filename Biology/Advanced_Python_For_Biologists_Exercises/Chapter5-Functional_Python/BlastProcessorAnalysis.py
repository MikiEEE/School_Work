
def mismatchFilter(lines):
    lines = lines.split("\t")
    if float(lines[4]) < 20:
        return float(lines[4])

def dataFilter(lines):
    if not lines.startswith('#'):
        return lines

def identicalSort(lines):
    return float(lines.split("\t")[2])

def COX1filter(lines):
    lines = lines.split("\t")
    if "COX1" in lines[1]:
        return lines[1]


data = list(filter(dataFilter, open('blast_result.txt', 'r') ))

#get hits that have fewer mismatches than 20
mismatches = list(filter(mismatchFilter, data))

#Find the subject sequence names of the 10 matches with the lowest percentage of identity
lowestIdentical = sorted(data, key=identicalSort)
lowestIdentical = list(map(lambda x : x.split("\t")[1],lowestIdentical[0:10]))

#Find the index of COX1 in subject sequence and display it as a proportion of len of match
containsCOX1 = list(filter(COX1filter, data))
COX1Proportion = map(lambda sequence: sequence.index("COX1")/ len(sequence),containsCOX1)
print(list(COX1Proportion))
