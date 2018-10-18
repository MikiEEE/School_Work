
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
    numberOfSimulations = 6

    for sims in range(0,numberOfSimulations):
        HaploidList = performNaturalSelection(HaploidList, random.random())
        listOfAllles = [HaploidList[i].getAlleles() for i in range(len(HaploidList))]
        listOffrequencies.append(getFrequency(listOfAllles, Fieldnames))
    closeAndWrite(listOffrequencies,Fieldnames,title[1])

main()
