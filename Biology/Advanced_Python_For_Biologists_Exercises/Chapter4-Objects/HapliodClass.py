import csv
import random
import re
import copy as replicate

CSVDict = {}
# fieldnames= ('A' , 'a' , 'B' , 'b' , 'C' , 'c')
with open('alleles.csv', mode='r') as allelesFile:
    Fieldnames = 'A','a','B','b','C','c'
    reader = csv.DictReader(allelesFile, restkey=None, delimiter=',',skipinitialspace=False)
    rownumber = 0
    for row in reader:
        print(row)
        CSVDict[rownumber] =  row
        rownumber = rownumber + 1

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

def main():
    HaploidList = [Haploid(CSVDict[i]) for i in CSVDict]
    Frequency = {}
    FrequencySim = {}
    numberOfSimulations = 1
    for SimNumber in range(numberOfSimulations):
        for x in range(len(HaploidList)):
            if not HaploidList[x].Selection():
                listRange = list(range(0,x)) + list(range(x,len(HaploidList)))
                HaploidList[x] = replicate.deepcopy(HaploidList[random.choice(listRange)])

        for x in range(len(HaploidList)):
            Frequency[x] = HaploidList[x].getAlleles()

        FrequencySim[SimNumber] = Frequency

    with open('Simulation.csv', 'w') as Outputfile:
        Fieldnames = 'A','a','B','b','C','c'
        writer = csv.DictWriter(Outputfile, fieldnames=Fieldnames,extrasaction='ignore')
        for SimNum, Haploids in FrequencySim.items():
            for Index, Alleles in Haploids.items():
                writer.writerow(Alleles)

main()
