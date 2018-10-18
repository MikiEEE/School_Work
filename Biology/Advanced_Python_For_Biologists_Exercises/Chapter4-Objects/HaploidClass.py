import re
import random
from HelperFunctions import chunk


'''
@Class Haploid - Contains the alleles and fitness scores of the instances
@param AllelesEnetered - Alleles of parent, one of eahch pair gets passed down to haploid 
@var fitnessScore - multiplicative scoring calculated with allele  fitness levels
@var AllelesOfHaploid - 1 of each of the alleles in the parental pairs (selected at random)
'''
class Haploid(object):
    fitnessScore = 1
    AllelesOfHaploid = None

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
