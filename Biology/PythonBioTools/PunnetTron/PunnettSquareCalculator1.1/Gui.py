from tkinter import *
from tkinter import ttk
from functools import reduce
import PunnettSquareCalculator as pc

def callCalculateGeneticTraits():
    text.delete('1.0',END)
    genomes = pc.calculateGeneticTraits(parent1Entry.get(),parent2Entry.get())
    genomelength = reduce(lambda x,y: x + y, genomes.values())
    line = '1.0'
    for alleles, occurr in genomes.items():
         text.insert(line ,str(alleles) + ':' + str(occurr/genomelength)+ '%' + '\n')
    return

root = Tk()
root.title('Standard Punnett')

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack()

parent1Label = Label(root,text='parent1')
parent1Label.pack()

parent1Entry = Entry(root)
parent1Entry.pack()

parent2Label = Label(root,text='parent2')
parent2Label.pack()

parent2Entry = Entry(root)
parent2Entry.pack()

text = Text(root, width=40, height=10)
text.pack()

calculatePunnett = Button(root,text='Calculate!',command=callCalculateGeneticTraits  )
calculatePunnett.pack()
root.mainloop()
