# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import commands
from threading import Thread

import operator
import subprocess

#Pakage Generation Script
from brocre_package_tools import *

global checkbuttonValues
global listbox
global allPackages
global textField
global consoleOutput
global buttonInstall
global buttonUninstall


allPackages = []
MAKEFILE_NAME = "Makefile"
ROBOT_PACKAGE_PATH = "../../"

def runProcess(exe):  
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline()
        yield line
        if(retcode is not None):
            # if process ends read all line with still remain in the pipe 
            newline = ""
            while(True):
                newline = p.stdout.readline()
                if newline == "":
                    break
                line = line + newline
                yield line
            break

def executeCommand(exe):
    buttonInstall.config(state=DISABLED)
    buttonUninstall.config(state=DISABLED)
    buttonupdateBROCRE.config(state=DISABLED)

    data = runProcess(exe) 
    for i in data:
        printIntoConsoleBox(i)

    printIntoConsoleBox("Done!\n")
    updateAllPackageDescriptions()
    buttonupdateBROCRE.config(state=NORMAL)
    
def printIntoConsoleBox(line):
    consoleOutput.config(state=NORMAL)
    consoleOutput.insert(END,line)
    consoleOutput.yview_moveto(1)  
    consoleOutput.config(state=DISABLED)
    
def executeCommandWithRestart(exe):
    executeCommand(exe)
    python = sys.executable
    os.execl(python, python, * sys.argv)


def updateAllPackageDescriptions():
    global allPackages
    allPackages = extractPackageDescriptions()
    selectCategorieEvent()
    event =""
    updateCurrentPackageDescription(event)


def installbutton():
    #Show Error if values are not entered
    error = ""
    toInstalledPackage = []
    
    if len(listbox.curselection()) == 0:
        error = "No package is selected!"
    else:        
        currentPackage = packageDescription()
        for package in allPackages:
            if package.name ==listbox.get(listbox.curselection()):
                currentPackage = package
    
    
    if not error == "":
        tkMessageBox.showerror(message=error)
    else:
        if( tkMessageBox.askokcancel("Install package", "Package " + currentPackage.name + " will be installed!") == 1):
            command = ['make', '-C', ROBOT_PACKAGE_PATH + currentPackage.folder +"/" +  currentPackage.name, 'update']
            t = Thread(target=executeCommand, args=(command,))
            t.start()
        
        
def uninstallbutton():
    #Show Error if values are not entered
    error = ""
    toInstalledPackage = []
    
    if len(listbox.curselection()) == 0:
        error = "No package is selected!"
    else:        
        currentPackage = packageDescription()
        for package in allPackages:
            if package.name ==listbox.get(listbox.curselection()):
                currentPackage = package
    
    if not error == "":
        tkMessageBox.showerror(message=error)
    else:
        if( tkMessageBox.askokcancel("Uninstall package", "Package " + currentPackage.name + " will be uninstalled!") == 1):
            command = ["robotpkg_delete", currentPackage.name]
            t = Thread(target=executeCommand, args=(command,))
            t.start()
        
def compilebutton():
    #Show Error if values are not entered
    error = ""
    toInstalledPackage = []
    
    if len(listbox.curselection()) == 0:
        error = "No package is selected!"
    else:        
        currentPackage = packageDescription()
        for package in allPackages:
            if package.name ==listbox.get(listbox.curselection()):
                currentPackage = package
    
    if not error == "":
        tkMessageBox.showerror(message=error)
    else:
        if( tkMessageBox.askokcancel("Compile package", "Package " + currentPackage.name + " will be compiled!") == 1):
            command = ["rosmake" , currentPackage.name]
            t = Thread(target=executeCommand, args=(command,))
            t.start()

        
def updateBROCREbutton():
    #Show Error if values are not entered
 #   tkMessageBox.showinfo("Result", "BROCRE will be updated!" )
    if( tkMessageBox.askokcancel("BROCRE update", "BROCRE will be updated!") == 1):
        printIntoConsoleBox("Updating ...")
        command = ["git","pull", "origin", "master"]
        t = Thread(target=executeCommandWithRestart, args=(command,))
        t.start()

  
def selectCategorieEvent():
    listbox.delete(0,END)
    selectedpackages = []
    for package in allPackages:
        for selectedCategories in checkbuttonValues:
            if package.categories.count(selectedCategories.get()) > 0:
                selectedpackages.append(package)
    
    selectedpackages = list(set(selectedpackages))
    selectedpackages.sort(cmp=None, key=operator.attrgetter('name'), reverse=False)
    
    for package in selectedpackages:
        listbox.insert(END, package.name)
        if not package.installedVersion == "":
            if package.installedVersion == package.version:
                listbox.itemconfig(END, background="green")
            if float(package.installedVersion) < float(package.version):
                listbox.itemconfig(END, background="orange")
                    
        
def updateCurrentPackageDescription(event):
    if not len(listbox.curselection()) == 0:
        currentPackage = packageDescription()
        
        for package in allPackages:
            if package.name ==listbox.get(listbox.curselection()):
                currentPackage = package
                
        text = "Package: " + currentPackage.name + "\n" + \
        "Version: " + currentPackage.version +"\n" \
        "Installed version: " + currentPackage.installedVersion +"\n" \
        "Categories: " + currentPackage.categories.__str__() +"\n" \
        "Maintainer: " + currentPackage.maintainer +"\n" \
        "Homepage: " + currentPackage.homepage +"\n" \
        "License: " + currentPackage.license +"\n\n" \
        "Description: " + currentPackage.description +"\n"
        if currentPackage.installedVersion == "":
            buttonInstall.config(state=NORMAL)
            buttonUninstall.config(state=DISABLED)
        else:
            buttonUninstall.config(state=NORMAL)
            buttonInstall.config(state=DISABLED)
        textField.config(state=NORMAL)
        textField.delete(1.0, END)
        textField.insert(END, text)
        textField.config(state=DISABLED)
    else:
        textField.config(state=NORMAL)
        textField.delete(1.0, END)
        textField.config(state=DISABLED)
        buttonInstall.config(state=DISABLED)
        buttonUninstall.config(state=DISABLED)
        

        
if __name__ == "__main__":
                    
    ''' Window Creation '''
    root = Tk()
    root.title("BROCRE Package Installer")
          
    
    allPackages = extractPackageDescriptions()
        
    allCategories = list()
    for package in allPackages:
         for category in package.categories:
             allCategories.append(category)
             
    allCategories = list(set(allCategories))
    allCategories.sort(cmp=None, key=None, reverse=False)
    
    checkbuttonRow = 0
    checkbuttonValues = list()
    
    groupCategories = LabelFrame(root, text="Categories", padx=5, pady=5)
    groupCategories.grid(row=0, column=0, sticky=W)
    
    var = StringVar()
    for categorie in allCategories:
        checkbuttonValues.append(StringVar())
        cb = Checkbutton(groupCategories, text=categorie, variable=checkbuttonValues[checkbuttonRow], onvalue=categorie, offvalue="", command=selectCategorieEvent)
        cb.grid(row=checkbuttonRow, column=0, sticky=W)
        cb.select()
        checkbuttonRow = checkbuttonRow + 1
        
    listboxframe = LabelFrame(root, text="BROCRE Packages", bd=2, relief=SUNKEN)
    listbox = Listbox(listboxframe, selectmode=SINGLE, height = 12, width = 30)
    listbox.grid( sticky=W)
    listboxframe.grid( sticky=W)

    root.bind("<Button-1>", updateCurrentPackageDescription)
    root.bind("<Key>", updateCurrentPackageDescription)
    
    descriptionFrame = LabelFrame(root, text="Description", padx=5, pady=5)
    descriptionFrame.grid(row=0, column=1,rowspan=2, sticky=N)
    textField = Text(descriptionFrame, height = 20)
    textField.grid(row=0, column=0, sticky=W)
    


    
    # Buttons
    #buttonOpenFile = Button(root, text="...", command=openFile, height =1)
    #buttonOpenFile.grid(row=0,column=3, sticky=W )

    buttonInstall = Button(descriptionFrame, text="Install", command=installbutton)
    buttonInstall.grid( row=1,column=0,rowspan=2, sticky=W)
    buttonUninstall = Button(descriptionFrame, text="Uninstall", command=uninstallbutton)
    buttonUninstall.grid( row=1,column=0, sticky=N)
   # buttonCompile = Button(root, text="Compile", command=compilebutton)
   # buttonCompile.grid()
    buttonupdateBROCRE = Button(descriptionFrame, text="Update BROCRE", command=updateBROCREbutton)
    buttonupdateBROCRE.grid( row=1,column=0, sticky=E)
    
    buttonInstall.config(state=DISABLED)
    buttonUninstall.config(state=DISABLED)
    
    
    consoleframe = LabelFrame(root, text="Console", bd=2, relief=SUNKEN)
    
    consoleframe.grid_rowconfigure(0, weight=1)
    consoleframe.grid_columnconfigure(0, weight=1)
    
    xscrollbar = Scrollbar(consoleframe, orient=HORIZONTAL)
    xscrollbar.grid(row=1, column=0, sticky=E+W)
    
    yscrollbar = Scrollbar(consoleframe)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    
    consoleOutput = Text(consoleframe, wrap=WORD, bd=0, height = 10, width = 115,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)
    
    consoleOutput.grid(row=0, column=0, sticky=N+S+E+W)
    
    
    xscrollbar.config(command=consoleOutput.xview)
    yscrollbar.config(command=consoleOutput.yview)
    consoleframe.grid(row=10,columnspan=2, column=0, sticky=W)
    

    
    selectCategorieEvent()

    root.mainloop()
