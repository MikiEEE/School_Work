import re
import random

def chunk(xs, n):
    '''Split the list, xs, into n chunks'''
    L = len(xs)
    assert 0 < n <= L
    s = L//n
    return [xs[p:p+s] for p in range(0, L, s)]

class Haploid(object):
    fitnessScore = 1
    AllelesOfHaploid = None

    def pickAlleles(self,AllelesOfParent):
        Allalleles = list()
        selectedAlleles = list()
        for Allele in AllelesOfParent:
            if Allele != '':
                Allalleles.append(Allele)
        Allalleles = chunk(Allalleles,int(len(Allalleles)/2))
        for allelesPairs in Allalleles:
            selectedAlleles.append(allelesPairs[random.randint(0,1)])
        return selectedAlleles

    def __init__(self, AllelesEnetered):
        self.AllelesOfHaploid = self.pickAlleles(AllelesEnetered)
        try:
            if isinstance(AllelesEnetered, dict):
                for x in self.AllelesOfHaploid:
                    temp = AllelesEnetered[x]
                    temp = re.sub(' 0.\s+','', temp)
                    temp = temp.lstrip('0')
                    if temp == '0.0':
                        self.fitnessScore = 0
                        break
                    else:
                        self.fitnessScore =  float(temp) * self.fitnessScore
            else:
                raise ValueError
        except ValueError:
            print("The Alleles weren't put in the right format")

    def getAlleles(self):
        return  self.AllelesOfHaploid

    def getFitness(self):
        return self.fitnessScore

    def Selection(self,number = -1):
        if number == -1:
            number = random.random()
        if number < self.fitnessScore:
            return True
        return False
