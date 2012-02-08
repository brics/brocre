# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 
import commands

#Ros Stuff
import rospkg

#Pakage Generation Script
from brocre_package_tools import *

global allPackages
global entryWidgetPackageName
global entryWidgetCategorie
global entryWidgetVersion
global entryWidgetMasterSite
global checkbuttonValues
global listbox


allPackages = []

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
	if labelBrocreFolder.get().strip() == "":
		error = error + "\nInsert BROCRE Folder"  
		
		

	dependencies = []
	for value in listbox.curselection():
		for package in allPackages:
			if listbox.get(value) == package.name:
				dependencies.append(package.folder + "/"+package.name)
		
		
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		tkMessageBox.showinfo("Result", "Package Name: " + entryWidgetPackageName.get().strip() 
			+ "\n Package Categorie: " + entryWidgetCategorie.get().strip() 
			+ "\n Package Version: " + entryWidgetVersion.get().strip()
			+ "\n Package MasterSite: " + entryWidgetMasterSite.get().strip()
			+ "\n BROCRE Folder: " + labelBrocreFolder.get().strip()
			+ "\n Dependencies: " + dependencies.__str__())
		
		generateBrocreFiles(entryWidgetPackageName.get().strip(),
			entryWidgetCategorie.get().strip(),
			entryWidgetMasterSite.get().strip(),
			entryWidgetVersion.get().strip(),
			dependencies,
			labelBrocreFolder.get().strip())
	

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

		
if __name__ == "__main__":
	
	''' Window Creation '''
	root = Tk()
	root.title("BROCRE Package Generator")
	  	
	# Text Lables
	labelPackageName = Label(root, text="Package Name:").grid(row=1, sticky=W)
	labelCategorie = Label(root, text="Category: (separate by spaces)").grid(row=2, sticky=W)
	labelVersion = Label(root, text="Version:").grid(row=3, sticky=W) 
	labelMasterSite = Label(root, text="Master Site:").grid(row=4, sticky=W	) 
	labelBrocreFolder = Label(root, text="BROCRE Folder:").grid(row=5, sticky=W	) 

	# Input fileds
	entryWidgetPackageName = Entry(root, width=25)
	entryWidgetPackageName.grid(row=1, column=1, sticky=W)
	entryWidgetCategorie = Entry(root, width=25)
	entryWidgetCategorie.grid(row=2, column=1, sticky=W)
	entryWidgetVersion = Entry(root, width=25)
	entryWidgetVersion.grid(row=3, column=1, sticky=W)
	entryWidgetMasterSite = Entry(root, width=25)
	entryWidgetMasterSite.grid(row=4, column=1, sticky=W)
	labelBrocreFolder = Entry(root, width=25)
	labelBrocreFolder.grid(row=5, column=1, sticky=W)
	
	entryWidgetPackageName.insert(0, "youbot_driver")
	entryWidgetCategorie.insert(0, "hardware youbot")
	entryWidgetVersion.insert(0, "0.9")
	entryWidgetMasterSite.insert(0, "http://brics.inf.h-brs.de/")
	labelBrocreFolder.insert(0, "hardware")
	
	
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
		cb.grid(row=checkbuttonRow + 6, column=0, sticky=W)
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
