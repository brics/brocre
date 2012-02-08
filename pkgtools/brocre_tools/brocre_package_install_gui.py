# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 
import commands

#Ros Stuff
import rospkg
import operator

#Pakage Generation Script
import brocre_package_tools

global checkbuttonValues
global listbox
global allPackages
global textField
global consoleOutput
global buttonInstall
global buttonUninstall

allPackages = []

class packageDescription:
    def __init__(self):
        self.name = ""
        self.folder = ""
        self.version = ""
        self.categories = []
        self.installedVersion = ""
        self.maintainer = ""
        self.homepage = ""
        self.license = ""
        self.description = ""

def extractPackagesFromRobotPKGMakefile(Makefile):
    COMMENT_IN_MAKEFILE = "#"
    SUBDIR_STRING = "SUBDIR+="
    
    packageDescriptionFolder = []
    #Check every line if it contains SUBDIR+= and is not commented out via '#'
    for line in  Makefile:
        if not COMMENT_IN_MAKEFILE in line and SUBDIR_STRING in line:        
            # parse line
            packageDescriptionFolder.append(line[len(SUBDIR_STRING):].strip())
    Makefile.close()
    return packageDescriptionFolder


def parsePKGMakefile(filename,currentpackage):
    COMMENT_IN_MAKEFILE = "#"
    filehandle = file(filename)
    for line in filehandle:
        if not COMMENT_IN_MAKEFILE in line and "CATEGORIES" in line:
            categories = line[line.find("=")+1:].strip()
            currentpackage.categories = categories.split(" ")
        if not COMMENT_IN_MAKEFILE in line and "PACKAGE_VERSION" in line and currentpackage.version == "":
            currentpackage.version = line[line.find("=")+1:].strip()
        if not COMMENT_IN_MAKEFILE in line and "MAINTAINER" in line and currentpackage.maintainer == "":
            currentpackage.maintainer = line[line.find("=")+1:].strip()
        if not COMMENT_IN_MAKEFILE in line and "HOMEPAGE" in line and currentpackage.homepage == "":
            currentpackage.homepage = line[line.find("=")+1:].strip()
        if not COMMENT_IN_MAKEFILE in line and "LICENSE" in line and currentpackage.license == "":
            currentpackage.license = line[line.find("=")+1:].strip()
            
def parseRobotpkgInfo(inputtext,currentpackage):
    text = inputtext.split("\n")
    for line in text:
        if currentpackage.name in line:
            newline = line.split(" ")
            currentpackage.installedVersion = newline[0][len(currentpackage.name)+1:]


def extractPackageDescriptions():
    # Parse Makefile which contains Package Description folders
    packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(file(packageFoldersDescriptionFile))

    packageDescriptionsList = dict()
    
    #load hashmap key=Robotpkg Category/Folder, value = packageList
    for folder in packageDescriptionFolders:
        packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(file(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME))
        
    del allPackages[:]

    robotpkgInfoText = commands.getoutput("robotpkg_info")
    
    for folder in packageDescriptionsList.keys():
        for package in packageDescriptionsList[folder]:
            currentpackage = packageDescription()
            parsePKGMakefile(ROBOT_PACKAGE_PATH + folder +"/" +  package + "/Makefile", currentpackage)
            DESCRfile = file(ROBOT_PACKAGE_PATH + folder +"/" +  package +"/DESCR")
            currentpackage.description = DESCRfile.read()
            DESCRfile.close()
            currentpackage.name = package
            currentpackage.folder = folder
            parseRobotpkgInfo(robotpkgInfoText,currentpackage)
            allPackages.append(currentpackage)
     
    

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
            consoleOutput.config(state=NORMAL)
            consoleOutput.insert(END, commands.getoutput("make -C " + ROBOT_PACKAGE_PATH + currentPackage.folder +"/" +  currentPackage.name  + " update"))
            consoleOutput.yview_moveto(1)
            consoleOutput.config(state=DISABLED)
            extractPackageDescriptions()
            selectCategorieEvent()
            event =""
            updateCurrentPackageDescription(event)
        
        
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
            consoleOutput.config(state=NORMAL)
            consoleOutput.insert(END, commands.getoutput("robotpkg_delete " +  currentPackage.name))
            consoleOutput.yview_moveto(1)
            consoleOutput.config(state=DISABLED)
            extractPackageDescriptions()
            selectCategorieEvent()
            event =""
            updateCurrentPackageDescription(event)
        
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
            consoleOutput.config(state=NORMAL)
            consoleOutput.insert(END, commands.getoutput("rosmake " + currentPackage.name))
            consoleOutput.yview_moveto(1)
            consoleOutput.config(state=DISABLED)

        
def updateBROCREbutton():
    #Show Error if values are not entered
 #   tkMessageBox.showinfo("Result", "BROCRE will be updated!" )
    if( tkMessageBox.askokcancel("BROCRE update", "BROCRE will be updated!") == 1):
        consoleOutput.config(state=NORMAL)
        consoleOutput.insert(END, commands.getoutput("git pull origin master"))
        consoleOutput.yview_moveto(1)
        consoleOutput.config(state=DISABLED)
        python = sys.executable
        os.execl(python, python, * sys.argv)

  

'''
Open File dialog
'''
def openFile():
    ftypes = [('Manifest files', '*.xml'), ('All files', '*')]
    dlg = tkFileDialog.Open(root, filetypes = ftypes)
    fl = dlg.show()
    entryWidgetManifest.insert(0, fl)


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
    
    ''' Find all RobotPKG  package descriptions '''
    # Makefile Parser Definitions
    ROBOT_PACKAGE_PATH = "../../"
    MAKEFILE_NAME = "Makefile"

    #Definition for Softwaretype Radiobuttons
    PACKAGE = "Package"
    STACK = "Stack"
    
    packageFoldersDescriptionFile = ROBOT_PACKAGE_PATH + MAKEFILE_NAME
                    
    ''' Window Creation '''
    root = Tk()
    root.title("BROCRE Package Installer")
          
    

    extractPackageDescriptions()
        
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
        
    listboxframe = LabelFrame(root, text="Packages / Stacks", bd=2, relief=SUNKEN)
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
 #   buttonCompile = Button(root, text="Compile", command=compilebutton)
 #   buttonCompile.grid()
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
    

#    consoleOutput = Text(root, wrap=WORD, height = 10, width = 110, yscrollcommand=scrollbar.set)
 #   consoleOutput.grid(row=10,columnspan=2, column=0, sticky=W)
    
    selectCategorieEvent()

    root.mainloop()
