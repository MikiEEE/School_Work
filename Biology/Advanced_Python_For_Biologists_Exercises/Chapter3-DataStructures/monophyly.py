##The purpose of this program is to be able to go through a tree and test for monophyly
#write a function that determines if two texa are more closely related to eachother than a thrid taxa
tree = ['dog', ['raccoon','bear'], [['sea_lion','seal'],['monkey','cat'], 'weasel']]

'''
@Contain-Goes through a given list to see if the list contains the element in the array
@param listEntry-List that contains will find the element in
@param entry-Target to be found in listEntry
@return Type Bool - returns true is the element is in the list
'''
def contains(listEntry, entry):
    for element in listEntry:
        if(isinstance(element, list)):
            if contains(element, entry):
                return True;
        elif element == entry:
            return True
    return False

'''
@closer_related -  uses the contains fucntion to go through all of the sublists of the of the main tree
    to determine if the first two taxa given are closer related than the third taxa
@param taxa1 - List entry given
@param taxa2 - List entry given
@param taxa3 - List entry given
@return Type Bool returns true if the Taxa1 and Taxa2 are closer_related than Taxa3
'''
def closer_related(listEntry, taxa1, taxa2,taxa3):
    if contains(listEntry,taxa1) and contains(listEntry,taxa2) and not contains(listEntry,taxa3):
        return True
    for elements in listEntry:
        if isinstance(elements, list):
            if closer_related(elements, taxa1, taxa2,taxa3):
                return True
    return False

assert closer_related(tree, 'raccoon', 'bear', 'weasel') == False
