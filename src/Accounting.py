'''
Created on May 24, 2016

@author: AS017303
'''
from tkinter import *

columnIdx = 0

def createArea(display):
    global columnIdx
    entryValue = StringVar()
    totalValue = StringVar()
    total = 0.0
    
    def add(self):
        nonlocal total
        listbox.insert(END, entryValue.get())
        total = total + float(entryValue.get())
        entryValue.set("")
        calculate()
    def calculate():
        totalValue.set(total)
    def delete(self):
        nonlocal total
        total = total - float(listbox.get(ANCHOR))
        listbox.delete(ANCHOR)
        calculate()
    
    otherLabelFrame = LabelFrame(mainframe, text=display)
    otherLabelFrame.grid(row=0, column=columnIdx, sticky=N+S, padx=10, pady=20)
    entry = Entry(otherLabelFrame,textvariable=entryValue)
    entry.grid(sticky=N, padx=5)        
    entry.bind('<Return>', add)
    listbox = Listbox(otherLabelFrame, width=20, height=30)
    listbox.grid(sticky=N+S)
    listbox.bind('<Delete>', delete)
    button = Button(otherLabelFrame, text="Calculate", command=calculate)
    button.grid(sticky=S, padx=5)
    totalEntry = Entry(otherLabelFrame,textvariable=totalValue)
    totalEntry.grid(sticky=S, padx=5, pady=10)
        
    columnIdx = columnIdx + 1
    
    return listbox

### BEGIN ##########################################################################################################    
mainframe = Tk()

groceryList = createArea('Groceries')
eatOutList = createArea('Eat out')
gasList = createArea('Gas')
amazonList = createArea('Amazon/Dept Stores')
otherList = createArea('Other')

mainframe.mainloop()
### END ########################################################################################################## 
