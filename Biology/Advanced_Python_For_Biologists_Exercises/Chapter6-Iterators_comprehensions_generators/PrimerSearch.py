

# Write a generator which will generate all possible primers of a given
# length (hint: look back at the chapter on recursion for an example of a
# function that will act as a starting point). Write a second generator which
# uses the first to generate all possible pairs of such primers.


def PrimerGenerator(length):
    finalSequence = list()
    if length == 1:
        for base in ['A','T','C','G']:
            yield base
    else:
        for primer in PrimerGenerator(length - 1):
            for base in ['A','T','C','G']:
                yield primer + base

def PrimerPairGenerator(listOFPrimers):
    pair = list()
    for sequence in listOFPrimers:
        pair = ""
        for base in sequence:
            if base == 'T':
                pair = pair + 'A'
            elif base == 'C':
                pair = pair + 'G'
            elif base == 'A':
                pair = pair + 'T'
            elif base == 'G':
                pair = pair + 'C'
            else:
                print(base + ":Is not a valid input")
                raise ValueError
        yield pair

length = 3
generate = PrimerGenerator(length)

#holds all generated pairs
pairs = [generatedPairs for generatedPairs in PrimerPairGenerator(generate)]

print(pairs)
