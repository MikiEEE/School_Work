import sys
sys.path.append("../")
import nose.tools as nose
from  HelperFunctions import createTraits
#Only use to make test output
from filePrinter import makeOuput

#TESTS FOR createTraits()
TestInput = None
CorrectOuput = None
fileName = None
def setupOutput():
    global TestInput
    global CorrectOuput
    global fileName
    TestInput = [
    ['AB', 'Aa', 'aa', 'aa'],
    ['Bb', 'bb', 'Bb', 'bb'],
    ['cc', 'cc', 'Cc', 'Cc'],
    ['DD', 'DD', 'Dd', 'Dd']
    ]
    fileName = 'createTraitsOutput_4.txt'
    makeOuput(TestInput,fileName )
    CorrectOuput = [lines.strip('\n') for lines in open(fileName,'r').readlines()]
    return

@nose.with_setup(setupOutput)
def test_createTraits():
    nose.assert_equal(createTraits(TestInput),CorrectOuput)
    return

@nose.with_setup(setupOutput)
def test_invalidInput():
    fatalInput = ['Ee']
    nose.assert_raises(ValueError,createTraits, TestInput + fatalInput)
