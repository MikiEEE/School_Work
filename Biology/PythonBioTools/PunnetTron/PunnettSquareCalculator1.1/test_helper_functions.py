import nose.tools as nose
import speedup as hp


##TESTS FOR generateSinglePairs()
correctoutput = ['Aa', 'Aa', 'aa', 'aa', 'bB', 'bb', 'bB', 'bb']
parent1 = "Aabb"
parent2 = "aaBb"

#Tests for correct pairs given parents
def test_CorrectPairs_2():
    nose.assert_equal(hp.generateSinglePairs(len(parent1),parent1,parent2), correctoutput)

def testlength_2():
    nose.assert_equal(len(hp.generateSinglePairs(len(parent1),parent1,parent2)), len(correctoutput))

parent1 = "AabbcCDdEeFfHHIi"
parent2 = "aaBbccDDeeFFhhii"
correctoutput = [ 'Aa', 'Aa', 'aa', 'aa', 'bB', 'bb', 'bB', 'bb', 'cc',
    'cc', 'Cc', 'Cc', 'DD', 'DD', 'dD', 'dD', 'Ee', 'Ee', 'ee', 'ee', 'FF',
     'FF','fF', 'fF', 'Hh', 'Hh', 'Hh', 'Hh', 'Ii', 'Ii', 'ii', 'ii']

#Tests for correct pairs given parents
def test_CorrectPairs_8():
    nose.assert_equal(hp.generateSinglePairs(len(parent1),parent1,parent2), correctoutput)

#Tests for correct Length of list returned
def test_length_8():
    nose.assert_equal(len(hp.generateSinglePairs(len(parent1),parent1,parent2)), len(correctoutput))
