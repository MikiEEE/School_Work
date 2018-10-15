
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
    Fieldnames = 'A','a','B','b','C','c'
    title = 'alleles.csv', 'Simulation.csv'
    CSVDict = openAndRead(title[0])
    HaploidList = [Haploid(CSVDict[i]) for i in CSVDict]
    numberOfSimulations = 100
    FrequencySim = performNaturalSelection(numberOfSimulations,HaploidList)
    closeAndWrite(FrequencySim,Fieldnames,title[1])

main()
