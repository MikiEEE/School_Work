import csv
import random
import copy as replicate


'''
@Function performNaturalSelection() - generates a random number and compares it to the fitness level of the haploid individual.
    If the fitness score is greater, then the organism is killed and replaced by an existing organism (natural selection process)
    No genetic Recombination
@param numberOfSimulations - the number of times this natural selection process goes on.
@param HaploidList - The list of individuals that participate in similation (list of Haploid Objects)
@return Returns Total Data from Simulations ///Needs to be hanged to return frequency
'''
def performNaturalSelection(numberOfSimulations,HaploidList):
    FrequencySim = {}
    for SimNumber in range(numberOfSimulations):
        Frequency = {}
        for x in range(len(HaploidList)):
            if not HaploidList[x].Selection():
                listRange = list(range(0,x)) + list(range(x,len(HaploidList)))
                HaploidList[x] = replicate.deepcopy(HaploidList[random.choice(listRange)])
        for x in range(len(HaploidList)):
            Frequency[x] = HaploidList[x].getAlleles()
        FrequencySim[SimNumber] = Frequency
    return FrequencySim

'''
@Function openAndRead() - Opens CSV given title and reads information into dictionary
@param title - contains the name of the document to be opened and read
@returns a 2D dictionary holding the values of the CSV files
'''
def openAndRead(title):
    CSVDict = {}
    with open(title, mode='r') as allelesFile:
        reader = csv.DictReader(allelesFile, restkey=None, delimiter=',',skipinitialspace=False)
        rownumber = 0
        for row in reader:
            CSVDict[rownumber] =  row
            rownumber = rownumber + 1
    return CSVDict
'''
@Functon closeAndWrite() writes processed data to a file of the title given
@param FrequencySim - Data given to print out
@param title - title of file to be open
@return void
'''
def closeAndWrite(FrequencySim,Fieldnames, title):
    with open(title, 'w') as Outputfile:
        writer = csv.DictWriter(Outputfile, fieldnames=Fieldnames,extrasaction='ignore')
        for SimNum, Haploids in FrequencySim.items():
            for Index, Alleles in Haploids.items():
                writer.writerow(Alleles)
