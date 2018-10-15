import re
import random

class Haploid(object):
    fitnessScore = 1
    AllelesOfHaploid = None
    def __init__(self, AllelesEnetered):
        self.AllelesOfHaploid = AllelesEnetered
        try:
            if isinstance(AllelesEnetered, dict):
                for alleles,value in AllelesEnetered.items():
                    if alleles != '':
                        value = re.sub(' 0.\s+','', value)
                        value = value.lstrip('0')
                        if value == '0.0':
                            self.fitnessScore = 0
                        else:
                            self.fitnessScore =  float(value) * self.fitnessScore
            else:
                raise ValueError
        except ValueError:
            print("The Alleles weren't put in the right format")

    def getAlleles(self):
        return  self.AllelesOfHaploid

    def Selection(self,number = -1):
        if number == -1:
            number = random.uniform(0,1)
        if number < self.fitnessScore:
            return True
        return False
