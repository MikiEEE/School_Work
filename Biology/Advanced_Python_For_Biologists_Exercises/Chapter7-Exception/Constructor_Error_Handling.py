import re

class BlankEntryError(Exception):
    pass

class InvalidBaseError(Exception):
    pass
class FormatError(Exception):
    pass

class SequenceRecord(object):
    def __init__(self, sequence, gene_name, species_name):
            if sequence == '' or gene_name == '' or species_name == '':
                raise BlankEntryError('One Entry is blank')
            if not(isinstance(sequence, str) and isinstance(gene_name, str) and isinstance(species_name,str)):
                raise ValueError('Atleast one of the initializtion values are not the correct type')
            if re.search('[^ATGC]',sequence):
                raise InvalidBaseError('Sequence bases entered aren\'t valid')
            if not re.match('[A-Z]+[a-z]+ [a-z]', species_name):
                raise FormatError('species_name is not in correct format')
                
            self.sequence = sequence
            self.gene_name = gene_name
            self.species_name = species_name



seq = SequenceRecord('ATGCGGTGA', 'COX1' , 'homo sapiens')
