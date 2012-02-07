# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 
import commands

#Ros Stuff
import rospkg

#Pakage Generation Script
import brocre_package_generator

global entryWidgetPackageName
global entryWidgetCategorie
global entryWidgetVersion
global entryWidgetMasterSite
global checkbuttonValues
global listbox

def extractPackagesFromRobotPKGMakefile(Makefile):
	COMMENT_IN_MAKEFILE = "#"
	SUBDIR_STRING = "SUBDIR+="
	
	packageDescriptionFolder = []
	#Check every line if it contains SUBDIR+= and is not commented out via '#'
	for line in  Makefile:
		if not COMMENT_IN_MAKEFILE in line and SUBDIR_STRING in line:		
			# parse line
			packageDescriptionFolder.append(line[len(SUBDIR_STRING):].strip())
	return packageDescriptionFolder

def extractCategoryPerPackage():
	# Parse Makefile which contains Package Description folders
	packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(file(packageFoldersDescriptionFile))
	packageDescriptionsList = dict()
	
	#load hashmap key=Robotpkg Category/Folder, value = packageList
	for folder in packageDescriptionFolders:
		packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(file(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME))
		
	categoriesPerPackage = dict()
	
	for folder in packageDescriptionsList.keys():
		for package in packageDescriptionsList[folder]:
			categories = commands.getoutput("make -s -C " + ROBOT_PACKAGE_PATH + folder +"/" +  package  + " show-var VARNAME=CATEGORIES")
			categoriesAsList = categories.split(" ")
			categoriesPerPackage[package] = categoriesAsList 
	
	return categoriesPerPackage		
			
	#result = commands.getoutput("make -s -C " + ROBOT_PACKAGE_PATH + " show-var VARNAME=CATEGORIES | grep -v '===>'")
	##return list(set(result.split("\n")))
	#result = list(set(result))	
	

def displayText():
	""" Display the Entry text value. """
	rosStackCommnad = rospkg.RosStack()
	availableStacks = rosStackCommnad.list()
	rosPackageCommand = rospkg.RosPack()
	availablePackages=rosPackageCommand.list()
	
	#Show Error if values are not entered
	error = ""
	if not entryWidgetPackageName.get().strip() in availableStacks and not entryWidgetPackageName.get().strip() in availablePackages:
		error = error + entryWidgetPackageName.get().strip() + " is not a valid ROS stack or package"  
		
	if entryWidgetCategorie.get().strip() == "":
		error = error + "\nInsert Package Categorie"  
	if entryWidgetVersion.get().strip() == "":
		error = error + "\nInsert Package Version"  
	if entryWidgetMasterSite.get().strip() == "":
		error = error + "\nInsert Package Master Site"  
		
		

	dependencies = []
	for value in listbox.curselection():
		dependencies.append(listbox.get(value))
	
	
		
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		tkMessageBox.showinfo("Result", "Package Name: " + entryWidgetPackageName.get().strip() 
			+ "\n Package Categorie: " + entryWidgetCategorie.get().strip() 
			+ "\n Package Version: " + entryWidgetVersion.get().strip()
			+ "\n Package MasterSite: " + entryWidgetMasterSite.get().strip())
		
		brocre_package_generator.parseManifest(entryWidgetPackageName.get().strip(),
			entryWidgetCategorie.get().strip(),
			entryWidgetMasterSite.get().strip(),
			entryWidgetVersion.get().strip(),
			dependencies)

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
	for package in categoriesPerPackage.keys():
		for selectedCategories in checkbuttonValues:
			if categoriesPerPackage[package].count(selectedCategories.get()) > 0:
				selectedpackages.append(package)
				
	selectedpackages = list(set(selectedpackages))
	selectedpackages.sort(cmp=None, key=None, reverse=False)
	
	for package in selectedpackages:
		listbox.insert(END, package)

		
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
	root.title("BROCRE Package Generator")
	  	
	# Text Lables
	labelPackageName = Label(root, text="Package Name:").grid(row=1, sticky=W)
	labelCategorie = Label(root, text="Category:").grid(row=2, sticky=W)
	labelVersion = Label(root, text="Version:").grid(row=3, sticky=W) 
	labelMasterSite = Label(root, text="Master Site:").grid(row=4, sticky=W	) 

	# Input fileds
	entryWidgetPackageName = Entry(root, width=25)
	entryWidgetPackageName.grid(row=1, column=1, sticky=W)
	entryWidgetCategorie = Entry(root, width=25)
	entryWidgetCategorie.grid(row=2, column=1, sticky=W)
	entryWidgetVersion = Entry(root, width=25)
	entryWidgetVersion.grid(row=3, column=1, sticky=W)
	entryWidgetMasterSite = Entry(root, width=25)
	entryWidgetMasterSite.grid(row=4, column=1, sticky=W)
	
	categoriesPerPackage = extractCategoryPerPackage()
		
	allCategories = list()
	for sublist in categoriesPerPackage.values():
	 	for subsublist in sublist:
	 		allCategories.append(subsublist)
	allCategories = list(set(allCategories))
	allCategories.sort(cmp=None, key=None, reverse=False)
	
	checkbuttonRow = 0
	checkbuttonValues = list()
	
	var = StringVar()
	for categorie in allCategories:
		checkbuttonValues.append(StringVar())
		cb = Checkbutton(root, text=categorie, variable=checkbuttonValues[checkbuttonRow], onvalue=categorie, offvalue="", command=selectCategorieEvent)
		cb.grid(row=checkbuttonRow + 5, column=0, sticky=W)
		cb.deselect()
		checkbuttonRow = checkbuttonRow + 1
		
	listbox = Listbox(root, selectmode=MULTIPLE)
	listbox.grid( sticky=W)

	



	
	# Buttons
	#buttonOpenFile = Button(root, text="...", command=openFile, height =1)
	#buttonOpenFile.grid(row=0,column=3, sticky=W )

	buttonGO = Button(root, text="GO!", command=displayText)
	buttonGO.grid()

	root.mainloop()
