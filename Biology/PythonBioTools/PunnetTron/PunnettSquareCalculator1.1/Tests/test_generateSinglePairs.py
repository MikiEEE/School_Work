import sys
sys.path.append("../")
import nose.tools as nose
from  HelperFunctions import generateSinglePairs

parent1 = ''
parent2 = ''
correctoutput = list()


##SETUP FUNCTIONS
def setupFor2Pairs():
    global parent1
    global  parent2
    global correctoutput

    parent2 = "aaBb"
    parent1 = "Aabb"
    correctoutput = ['Aa', 'Aa', 'aa', 'aa', 'bB', 'bb', 'bB', 'bb']
    return

def setupFor8Pairs():
    global parent1
    global  parent2
    global correctoutput
    parent1 = "AabbcCDdEeFfHHIi"
    parent2 = "aaBbccDDeeFFhhii"
    correctoutput = [ 'Aa', 'Aa', 'aa', 'aa', 'bB', 'bb', 'bB', 'bb', 'cc',
        'cc', 'Cc', 'Cc', 'DD', 'DD', 'dD', 'dD', 'Ee', 'Ee', 'ee', 'ee', 'FF',
         'FF','fF', 'fF', 'Hh', 'Hh', 'Hh', 'Hh', 'Ii', 'Ii', 'ii', 'ii']

def SetupBadInputs():
    global parent1
    global parent2
    parent1 = 'ABb'
    parent2 = 'AaBb'
    return

##TESTS FOR generateSinglePairs()
#Tests for correct pairs given parents
@nose.with_setup(setupFor2Pairs)
def test_CorrectPairs_2():
    nose.assert_equal(generateSinglePairs(parent1,parent2), correctoutput)
    return

@nose.with_setup(setupFor2Pairs)
def testlength_2():
    nose.assert_equal(len(generateSinglePairs(parent1,parent2)), len(correctoutput))
    return

#################################################################################

#Tests for correct pairs given parents
@nose.with_setup(setupFor8Pairs)
def test_CorrectPairs_8():
    nose.assert_equal(generateSinglePairs(parent1,parent2), correctoutput)
    return

#Tests for correct Length of list returned
@nose.with_setup(setupFor8Pairs)
def test_length_8():
    nose.assert_equal(len(generateSinglePairs(parent1,parent2)), len(correctoutput))
    return

#Test For Invalid inputs
@nose.with_setup(SetupBadInputs)
def test_BadInput():
    nose.assert_raises(ValueError,generateSinglePairs,parent1,parent2)
    return
