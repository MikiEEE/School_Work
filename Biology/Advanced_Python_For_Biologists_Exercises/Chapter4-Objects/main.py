
from HelperFunctions import *
import HaploidClass
from HaploidClass import Haploid

#need Find Frequency Function


'''
@Funcion main() - Opens file and reads data from it, performs natural selection
to kill off non-fit haploids and replaces them with haploids that lived through the natural
Selection to simulate reproduction.
Prints frequency of traits after desired number of simulationCycles .
'''
def main():
    listOffrequencies = list()
    frequency = dict()
    Fieldnames = 'A','a','B','b','C','c'
    title = 'alleles.csv', 'Simulation.csv'
    CSVDict = openAndRead(title[0])
    HaploidList = [Haploid(CSVDict[i]) for i in CSVDict]
    numberOfSimulations = 100
    Deaths = 0
    sample_size = len(HaploidList)
    for sims in range(0,numberOfSimulations):
        HaploidList, Deaths = performNaturalSelection(HaploidList, random.random())
        listOfAllles = [HaploidList[i].getAlleles() for i in range(len(HaploidList))]
        for rebirth in range((Deaths)):
            HaploidList.append(HaploidList[random.randint(0, len(HaploidList) - 1)])
        listOffrequencies.append(getFrequency(listOfAllles, Fieldnames))
    closeAndWrite(listOffrequencies,Fieldnames,title[1])

main()
