import sys
sys.path.append("../")
import nose.tools as nose
from  HelperFunctions import createTraits
from Elements_State import createTraits as uut
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
    ['AA', 'Aa', 'Aa', 'aa'],
    ['BB', 'Bb', 'Bb', 'bb'],
     ['cc', 'cc', 'Cc', 'Cc'],
    # ['DD', 'DD', 'Dd', 'Dd']
    ]
    fileName = 'Tests/createTraitsOutput_4.txt'
    makeOuput(TestInput,fileName )
    CorrectOuput = [lines.strip('\n') for lines in open(fileName,'r').readlines()]
    return

@nose.with_setup(setupOutput)
def test_createTraits():
    nose.assert_equal(sorted(uut(TestInput)),sorted(CorrectOuput))
    return

@nose.with_setup(setupOutput)
def test_invalidInput():
    fatalInput = ['Ee']
    nose.assert_raises(ValueError,uut, TestInput + fatalInput)
