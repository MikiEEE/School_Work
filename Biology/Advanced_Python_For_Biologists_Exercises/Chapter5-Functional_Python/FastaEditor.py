import re

# #The sequence is in lower case and you need it in upper case
# #The sequence contains unknown bases that should be removed
# #The headers contain spaces that should be changed to underscores
# #The headers are too long and need to be truncated to ten characters
# #Append the length of the sequence to the header
# #Append the AT content of the sequence to the header
# #If the sequence starts with ATG and ends with a poly-A tail, append
# #the phrase "putative transcript" to the header
#
# #Read in headers of fasta
# header = filter(lambda line: line.startswith('>'),open('sequences.fasta','r'))
#
# #replace spaces with underscores
# newheader = map(lambda line: line.replace(' ',"_"),  header)
# del header
# #truncate headers to 10 characters
# newheader = map(lambda line: line[0:10] if len(line) > 10 else line, newheader)
#
# #Extract Data
# data = filter(lambda line: re.match("^[a-zA-Z]+.*", line) , open('sequences.fasta','r'))
#
# #Remove Newlines and Make Uppercase
# data = map(lambda line: line.strip('\n').upper(), data)
# data = map(lambda line: re.sub('[^ACTG+]', '', line), data)

def truncate(line,size = 10, begin=0,end= 10 ):
    if len(line) > size:
        line = line[begin:end]
    return line

def processHead(line):
    line.replace(' ','_')
    line = truncate(line)
    return line

def putativeTranscript(line,header,key):
    if re.search('^ATG+[A-Z]+A+$', line):
        return key
    else:
        return header

def writeHeader(header,lineLength,key,Appends):
    if header == key:
        return '>' + header + '\n'
    else:
        return header + str(lineLength) + str(Appends) + '\n'

def FastaCopy(file,ATG_AAA='putativetranscript'):
    header = None
    ATContent = None
    with open('corrected.fasta','w') as f:
        for line in file:
            if line.startswith('>'):
                header = processHead(line)
            else:
                line = re.sub('[^ACTG+]','', line.upper())
                ATContent = len(re.findall('AT+', line))
                header = putativeTranscript(line,header,ATG_AAA)
                f.write(writeHeader(header,len(line), ATG_AAA,ATContent))
                f.write(line + '\n')


FastaCopy(open('sequences.fasta', 'r'))
