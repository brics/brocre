# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 
import commands

#Ros Stuff
import rospkg

#Pakage Generation Script
import brocre_package_tools

global checkbuttonValues
global listbox
global allPackages
global textField

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

				

def extractPackageDescriptions():
	# Parse Makefile which contains Package Description folders
	packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(file(packageFoldersDescriptionFile))

	packageDescriptionsList = dict()
	
	#load hashmap key=Robotpkg Category/Folder, value = packageList
	for folder in packageDescriptionFolders:
		packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(file(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME))
		
	packageslocal = list()
	
	for folder in packageDescriptionsList.keys():
		for package in packageDescriptionsList[folder]:
			currentpackage = packageDescription()
			parsePKGMakefile(ROBOT_PACKAGE_PATH + folder +"/" +  package + "/Makefile", currentpackage)
			DESCRfile = file(ROBOT_PACKAGE_PATH + folder +"/" +  package +"/DESCR")
			currentpackage.description = DESCRfile.read()
			DESCRfile.close()
			currentpackage.name = package
			currentpackage.folder = folder
			packageslocal.append(currentpackage)
	
	return packageslocal		
	

def displayText():
	""" Display the Entry text value. """
	#Show Error if values are not entered
	error = ""
	toInstalledPackage = []
	
	for value in listbox.curselection():
		toInstalledPackage.append(listbox.get(value))
		
	if len(toInstalledPackage) == 0:
		error = "No package is selected!"
	
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		tkMessageBox.showinfo("Result", "Package " + toInstalledPackage[0] + " will be installed!" )
		

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
				selectedpackages.append(package.name)
				
	selectedpackages = list(set(selectedpackages))
	selectedpackages.sort(cmp=None, key=None, reverse=False)
	
	for package in selectedpackages:
		listbox.insert(END, package)
	listbox.itemconfig(0, background="green")
		
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
		textField.config(state=NORMAL)
		textField.delete(1.0, END)
		textField.insert(END, text)
		textField.config(state=DISABLED)

		
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
	  	


	allPackages = extractPackageDescriptions()
		
	allCategories = list()
	for package in allPackages:
	 	for category in package.categories:
	 		allCategories.append(category)
	 		
	allCategories = list(set(allCategories))
	allCategories.sort(cmp=None, key=None, reverse=False)
	
	checkbuttonRow = 0
	checkbuttonValues = list()
	
	var = StringVar()
	for categorie in allCategories:
		checkbuttonValues.append(StringVar())
		cb = Checkbutton(root, text=categorie, variable=checkbuttonValues[checkbuttonRow], onvalue=categorie, offvalue="", command=selectCategorieEvent)
		cb.grid(row=checkbuttonRow, column=0, sticky=W)
		cb.deselect()
		checkbuttonRow = checkbuttonRow + 1
		
	listbox = Listbox(root, selectmode=SINGLE)
	listbox.grid( sticky=W)

	root.bind("<Button-1>", updateCurrentPackageDescription)
	
	group = LabelFrame(root, text="Group", padx=5, pady=5)
	group.grid(row=checkbuttonRow, column=1, sticky=W)


	packageNameField = StringVar()
	textField = Text(group)
	textField.grid(row=0, column=0, sticky=W)
	


	
	# Buttons
	#buttonOpenFile = Button(root, text="...", command=openFile, height =1)
	#buttonOpenFile.grid(row=0,column=3, sticky=W )

	buttonGO = Button(root, text="Install!", command=displayText)
	buttonGO.grid()

	root.mainloop()
