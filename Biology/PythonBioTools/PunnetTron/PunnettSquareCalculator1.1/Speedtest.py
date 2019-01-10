import Elements_State as uut
import HelperFunctions as hp
import timeit as t

parent1 = "AabbcCDdEeFfHHIiLljjMmNn"
parent2 = "aaBbccDDeeFFhhiiLlJjmmnn"
thing = hp.generateSinglePairs(parent1,parent2)
thing = hp.chunk(thing, int(len(parent1)/2))

def testNew():
    global thing
    list(uut.createTraits(thing))

def testOld():
    global thing
    hp.createTraits(thing)

if __name__ == '__main__':
    print('NEW:', t.timeit('testNew()',setup="from __main__ import testNew",number=1))
    print('OLD:', t.timeit('testOld()',setup="from __main__ import testOld",number=1))
