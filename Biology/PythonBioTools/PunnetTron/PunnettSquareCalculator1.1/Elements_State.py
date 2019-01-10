from functools import reduce
from multiprocessing import Pool

class incrementor(object):
    incrementor = None

    def __init__(self, length):
        self.incrementor = [0 for x in range(length)]

    def increment(self):
        trigger = False
        for index in range(len(self.incrementor)):
            if self.incrementor[index] < 3 and trigger:
                self.incrementor[index]+= 1
                trigger = False
                break
            elif self.incrementor[index] < 3:
                self.incrementor[index]+= 1
                break
            elif self.incrementor[index] == 3:
                self.incrementor[index] = 0
                trigger = True
        return

    def generate(self, elements):
        index = 0
        result = ''
        for element in elements:
            itemIndice = self.incrementor[index]
            if itemIndice > len(element):
                raise IndexError(str(err) + str(index))
            result += element[itemIndice]
            index += 1
        return result

    def __str__(self):
        return str(self.incrementor)

# def createTraits(elements):
#     elements = [elementState(element) for element in elements]
#     length = len(elements)**2
#     result= list()
#
#     lockBracket = [0 for x in range(len(elements) - 1)]
#     lockBracket.insert(0,1)
#
#     for y in range(4):
#         for index in range(len(elements)):
#             elements[index].lockItem(lockBracket[index])
#         for x in range(4):
#             resultant = [element.getItem() for element in reversed(elements)]
#             print('RESULTANT: ',resultant)
#             [result.append(''.join(reduce(lambda y,x: x + y,resultant))) for num in range(4)]
#         for element in elements:
#             element.incrementLocked()
#         lockBracket = shift(lockBracket)
#         for index in range(len(elements)):
#             elements[index].lockItem(lockBracket[index])
#
#     return result
incre = None

def createTraits(elements):
    result = list()
    Traits = tuple(lists for lists in elements)
    incre = incrementor(len(Traits))
    for x in range(4**len(Traits)):
        incre.increment()
        yield incre.generate(Traits)

Traits = None

def multiCreateTraits(elements):
    global incre
    global Traits
    result = list()
    Traits = tuple(lists for lists in elements)
    incre = incrementor(len(Traits))
    p = Pool(processes=4)
    return p.map(maping,range(4**len(Traits)))

def maping(index):
    global incre
    global Traits
    incre.increment()
    return incre.generate(Traits)


if __name__ == '__main__':
    alleles = [
    ['AA', 'Aa', 'Aa', 'aa'],
    ['BB', 'Bb', 'Bb', 'bb']
    ,['cc', 'cc', 'Cc', 'Cc']]#, ['DD', 'Dd', 'DD', 'Dd']]
    result = list(multiCreateTraits(alleles))
    print(result, len(result),':',  )
