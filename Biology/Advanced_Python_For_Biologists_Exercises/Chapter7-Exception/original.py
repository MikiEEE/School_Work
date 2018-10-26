# A Python programmer has written a piece of code that reads a DNA
# sequence from a file and splits it up into a set number of equal-sized
# pieces (ignoring any incomplete pieces at the end of the sequence). It asks
# the user to enter the name of the file and the number of pieces, calculates
# the length of each piece (by dividing the total length by the number of
# pieces), then uses a range() to print out each piece:

try:
    # check for valid filename
    input_file = input('enter filename:\n')
    f = open(input_file)
    dna = f.read().rstrip("\n")
    # check for valid number
    pieces = raw_input('enter number of pieces:\n')
    # check that number is not zero or negative
    pieces = int(pieces)
except IOError:
    print(input_file + ' :not a valid filename')
except ValueError:
    if not isinstance(int(), pieces):
        print(pieces + ': is not a valid number')
    elif pieces <= 0:
        print('Value entered must be positive nonzero integer')
else:
    # do the processing
    piece_length = len(dna) / pieces
    print('piece length is ' + str(piece_length))
    for start in range(0, len(dna)-piece_length+1, piece_length):
        print(dna[start:start+piece_length])
