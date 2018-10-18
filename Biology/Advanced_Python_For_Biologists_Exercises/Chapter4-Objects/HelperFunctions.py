import csv
import random
import copy as replicate


'''
@Function performNaturalSelection() - generates a random number and compares it to the fitness level of the haploid individual.
    If the fitness score is greater, then the organism is killed and replaced by an existing organism (natural selection process)
    No genetic Recombination
@param fitnessOfGeneration - fitness score of generation that all haploids will be tested against
@param HaploidList - The list of individuals that participate in similation (list of Haploid Objects)
@return - Returns the remaining Haploid List and the number of Deaths
'''
def performNaturalSelection(HaploidList, fitnessOfGeneration):
    FrequencySim = {}
    Frequency = {}
    NumberOfDeaths = 0
    for x in HaploidList:
        if not x.Selection(fitnessOfGeneration):
            HaploidList.remove(x)
            NumberOfDeaths = NumberOfDeaths + 1
    return HaploidList, NumberOfDeaths

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
@param listOfDicts - Data given to print out
@param title - title of file to be open
@return void
'''
def closeAndWrite(listOfDicts,Fieldnames, title):
    with open(title, 'w') as Outputfile:
        writer = csv.DictWriter(Outputfile, fieldnames=Fieldnames,extrasaction='ignore')
        writer.writeheader()
        for element in listOfDicts:
            writer.writerow(element)

'''
@Function getFrequency() -  takes in A list of items and returns the frequencies
    of each item in the list
@param listOfItems - list of sublists that contain lists or indepndent items
@param Fieldnames - optional List of fieldnames for the list elements,
    if left blank, one will be generated but there will be ',,' in place of zeroes
@param divisor - optional variable that holds the divisor of the frequencies
    ie: occurences_of_fields/divisor
@return - returns a dictionary {field:OccurenceofField / divisor}
'''
def getFrequency(listOfItems, Fieldnames=None, divisor=100):
    frequencies = dict()
    Names = set()
    field = 0
    if Fieldnames != None:
        field = 1
        for name in Fieldnames:
            frequencies[name] = 0
    for subList in listOfItems:
        if isinstance(subList ,list):
            for element in subList:
                if field == 0 and element not in Names:
                    Names.add(element)
                    frequencies[element] = 1
                else:
                    frequencies[element] = frequencies[element] + 1
        else:
            if field == 0 and subList not in Names:
                Names.add(subList)
                frequencies[subList] = 1
            else:
                frequencies[subList] = frequencies[subList] + 1
    for key , value in frequencies.items():
        frequencies[key] = value / divisor

    return frequencies
