

# Rewrite your solutions to the BLAST processor exercises from the
# previous chapter to use list comprehensions. Here's a reminder of the
# questions we want to answer:
# • How many hits have fewer than 20 mismatches?
# • List the subject sequence names for the ten matches with the
#   lowest percentage of identical positions
# • For matches where the subject sequence name includes the string
# "COX1", list the start position on the query as a proportion of the
# length of the match

with open('blast_result.txt', 'r') as f:
    data = [line for line in f if not line.startswith('#')]

    #mismatches less than 20
    mismatches = [line for line in data if int(line.split('\t')[4]) < 20 ]

    #10 subject sequence names with lowest percentage of identical positions
    lowestID10 =  sorted(data, key = lambda x: x.split('\t')[2])
    lowestID10 = lowestID10[0:10]
    lowestID10 = [line.split('\t')[1] for line in lowestID10]

    #Find COX1 list start position as proportion of the length of match
    COX1 = [
            line.split('\t')[1].index('COX1')/len(line.split('\t')[1])
            for line in data
            if 'COX1' in line.split('\t')[1]
            ]

            
