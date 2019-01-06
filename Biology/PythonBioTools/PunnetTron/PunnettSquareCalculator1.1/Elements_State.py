from functools import reduce

class elementState(object):
    '''This class is designed to keep track of elements and states'''
    Entry = None
    lock = None
    state = None
    length = None
    def __init__(self, entry):
        if len(entry) != 4:
            raise ValueError()
        self.Entry = entry
        self.length = len(self.Entry)
        self.state = 0
        self.lock = False
        self.rounds = 0

    def incrementState(self,override=False):
        if override:
            if self.state < self.Entry.index(self.Entry[-1]):
                self.state += 1
            else:
                self.state = self.rounds
        elif self.getLock() == 1:
            print('INLOCKED',self)
            return
        else:
            if self.state < self.Entry.index(self.Entry[-1]):
                self.state += 1
            else:
                self.state = self.rounds
        return

    def incrementLocked(self):
        if self.getLock():
            self.incrementState(True)
        return

    def getItem(self):
        try:
            result = self.Entry[self.state]
            self.incrementState(False)
            return result
        except  IndexError:
            print('exception!')
            return self.Entry[-1]

    def zeroState(self, override=False):
        if override:
            self.state = 0
        elif self.getLock():
            return
        else:
            self.state = self.rounds
        return

    def getLock(self):
        return self.lock

    def lockItem(self, entry=0):
        if entry:
            self.lock = True
        else:
            self.lock = False
        return

    def incrementRound(self):
        self.rounds += 1
        return

    def getState(self):
        return self.state

    def __str__(self):
        return str(self.Entry)

def shift(entry):
    entry.insert(0,entry[-1])
    return entry[:len(entry) - 1]

def createTraits(elements):
    elements = [elementState(element) for element in elements]
    length = len(elements)**2
    result= list()

    lockBracket = [0 for x in range(len(elements) - 1)]
    lockBracket.insert(0,1)
    for index in range(len(elements)):
        elements[index].lockItem(lockBracket[index])
    for x in range(4):
        [
        result.append(''.join(reduce(lambda y,x: x + y, [element.getItem() for element in reversed(elements)])))
        for num in range(4)
        ]
        for element in elements:
            if element.getLock():
                element.incrementLocked()
    lockBracket = shift(lockBracket)
    for index in range(len(elements)):
        elements[index].lockItem(lockBracket[index])

    return result

if __name__ == '__main__':
    alleles = [
    ['AA', 'Aa', 'Aa', 'aa'],
    ['BB', 'Bb', 'Bb', 'bb']
    ,['cc', 'cc', 'Cc', 'Cc']]#, ['DD', 'Dd', 'DD', 'Dd']]
    result = createTraits(alleles)
    print(result, len(result))
