#!/usr/bin/python

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
global INSTALL_PATH
INSTALL_PATH = ""


allPackages = []

def checkIfBROCREisBootstraped(window):
  BROCRE_IS_INSTALLED = False
  try:
    brocreconf = open('./brocre.conf','r')
    for line in  brocreconf:
      if "ROBOTPKG_BASE=" in line:
        global INSTALL_PATH
        INSTALL_PATH = line.replace("ROBOTPKG_BASE=",'')
          
    os.environ["ROBOTPKG_BASE"]=INSTALL_PATH
    if (os.path.isfile(INSTALL_PATH+"/sbin/robotpkg_info")):   
      BROCRE_IS_INSTALLED = True;
  except IOError as e:
    print 'BROCRE is NOT installed'
    
    
  if(not BROCRE_IS_INSTALLED):
		tkMessageBox.showerror("BROCRE installation", "BROCRE is NOT installed!")
		exit()


def displayText():
	""" Display the Entry text value. """	
	#Show Error if values are not entered
	error = ""
	if entryWidgetPackageName.get().strip() == "":
		error = error + "\nInsert Package Name" 
	if entryWidgetCategorie.get().strip() == "":
		error = error + "\nInsert Category"  
	if entryWidgetVersion.get().strip() == "":
		error = error + "\nInsert Version"  
	if entryWidgetMaintainer.get().strip() == "":
		error = error + "\nInsert Maintainer" 
	if entryWidgetHomepage.get().strip() == "":
		error = error + "\nInsert Homepage" 
	if entryWidgetLicense.get().strip() == "":
		error = error + "\nInsert License" 
	if entryWidgetBrief.get().strip() == "":
		error = error + "\nInsert Brief description" 
	if entryWidgetDescription.get(1.0, END).strip() == "":
		error = error + "\nInsert Description" 
	if entryWidgetMasterSite.get().strip() == "":
		error = error + "\nInsert Package Master Site"  
	if entryWidgetBrocreFolder.get().strip() == "":
		error = error + "\nInsert BROCRE Folder"
	if entryWidgetFileToCheckIfInstall.get().strip() == "":
		error = error + "\nInsert File to check if install" 
	if entryWidgetSourcePath.get().strip() == "":
		error = error + "\nInsert Source Path" 

	dependencies = []
	for value in listbox.curselection():
		for package in allPackages:
			if listbox.get(value) == package.name:
				dependencies.append(package.folder + "/"+package.name)
		
		
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		if( tkMessageBox.askokcancel("Generate package", "Package " + entryWidgetPackageName.get().strip() + " will be generated!") == 1):
			package = packageDescription()
			package.name = entryWidgetPackageName.get().strip()
			package.folder = entryWidgetBrocreFolder.get().strip()
			package.version = entryWidgetVersion.get().strip()
			package.categories = entryWidgetCategorie.get().strip()
			package.installedVersion = "" # not needed here
			package.maintainer = entryWidgetMaintainer.get().strip()
			package.homepage = entryWidgetHomepage.get().strip()
			package.license = entryWidgetLicense.get().strip()
			package.description = entryWidgetDescription.get(1.0, END).strip()
			package.brief = entryWidgetBrief.get().strip()
			package.dependencies = dependencies
			package.masterSite = entryWidgetMasterSite.get().strip() 
			package.fileToCheckIfInstall = entryWidgetFileToCheckIfInstall.get().strip()
			package.sourcePath = entryWidgetSourcePath.get().strip()
			
			generateBrocreFiles(package)
		

def readFromROS():
	packageName = entryWidgetPackageName.get().strip()
	try:
		package = rospkg.RosStack()
		package.get_manifest(packageName)
		fileToCheckIfInstall = packageName + "/stack.xml"
		
	#	version = package.get_manifest(packageName).version
	except:
		try:
			package = rospkg.RosPack()
			package.get_manifest(packageName)
			fileToCheckIfInstall = packageName + "/manifest.xml"
		except:
			tkMessageBox.showerror(message="The package name is not a ROS stack or package")
			return
	
	entryWidgetFileToCheckIfInstall.insert(0, fileToCheckIfInstall)
	entryWidgetSourcePath.insert(0, package.get_path(packageName))
	entryWidgetMaintainer.insert(0, package.get_manifest(packageName).author)
	entryWidgetHomepage.insert(0, package.get_manifest(packageName).url)
	entryWidgetLicense.insert(0, package.get_manifest(packageName).license)
	entryWidgetBrief.insert(0, package.get_manifest(packageName).brief)
	entryWidgetDescription.insert(END, package.get_manifest(packageName).description)

		

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
	labelMaintainer = Label(root, text="Maintainer:").grid(row=4, sticky=W) 
	labelHomepage = Label(root, text="Homepage:").grid(row=5, sticky=W) 
	labelLicense = Label(root, text="License:").grid(row=6, sticky=W)
	labelBrief = Label(root, text="Brief description:").grid(row=7, sticky=W) 
	labelDescription = Label(root, text="Description:").grid(row=8, sticky=W) 
	labelMasterSite = Label(root, text="Master Site:").grid(row=9, sticky=W	) 
	labelBrocreFolder = Label(root, text="BROCRE Folder:").grid(row=10, sticky=W	) 
	labelFileToCheckIfInstall = Label(root, text="File to check if install:").grid(row=11, sticky=W	) 
	labelSourcePath = Label(root, text="Source Path:").grid(row=12, sticky=W	) 
	

	# Input fileds
	entryWidgetPackageName = Entry(root, width=40)
	entryWidgetPackageName.grid(row=1, column=1, sticky=W)
	entryWidgetCategorie = Entry(root, width=40)
	entryWidgetCategorie.grid(row=2, column=1, sticky=W)
	entryWidgetVersion = Entry(root, width=40)
	entryWidgetVersion.grid(row=3, column=1, sticky=W)
	entryWidgetMaintainer = Entry(root, width=40)
	entryWidgetMaintainer.grid(row=4, column=1, sticky=W)
	
	entryWidgetHomepage = Entry(root, width=40)
	entryWidgetHomepage.grid(row=5, column=1, sticky=W)
	
	entryWidgetLicense = Entry(root, width=40)
	entryWidgetLicense.grid(row=6, column=1, sticky=W)
	
	entryWidgetBrief = Entry(root, width=40)
	entryWidgetBrief.grid(row=7, column=1, sticky=W)
	
	entryWidgetDescription = Text(root, wrap=WORD, width=46, height=8)
	entryWidgetDescription.grid(row=8, column=1, sticky=W)
	
	entryWidgetMasterSite = Entry(root, width=40)
	entryWidgetMasterSite.grid(row=9, column=1, sticky=W)
	entryWidgetBrocreFolder = Entry(root, width=40)
	entryWidgetBrocreFolder.grid(row=10, column=1, sticky=W)
	
	entryWidgetFileToCheckIfInstall = Entry(root, width=40)
	entryWidgetFileToCheckIfInstall.grid(row=11, column=1, sticky=W)
	
	entryWidgetSourcePath = Entry(root, width=40)
	entryWidgetSourcePath.grid(row=12, column=1, sticky=W)
	
	#entryWidgetPackageName.insert(0, "youbot_driver")
	#entryWidgetCategorie.insert(0, "hardware youbot")
	#entryWidgetVersion.insert(0, "0.9")
	entryWidgetMasterSite.insert(0, "http://brics.inf.h-brs.de/")
	#entryWidgetBrocreFolder.insert(0, "hardware")
	
	checkIfBROCREisBootstraped(root)
	
	allPackages = extractPackageDescriptions(INSTALL_PATH)
	
	allCategories = list()
	for package in allPackages:
		for category in package.categories:
			allCategories.append(category)
	    
	allCategories = list(set(allCategories))
	allCategories.sort(cmp=None, key=None, reverse=False)
	
	checkbuttonRow = 0
	checkbuttonValues = list()
	
	readFromROSButton = Button(root, text="read ROS xml file", command=readFromROS)
	readFromROSButton.grid(row=13, column=0,)
	
	listboxframe = LabelFrame(root, text="Dependencies", bd=2, relief=SUNKEN)
	listboxframe.grid(row=14, column=0, sticky=W, columnspan =2)
	groupCategories = LabelFrame(listboxframe, text="Categories", padx=5, pady=5)
	groupCategories.grid(row=0, column=0, sticky=W)
    
	var = StringVar()
	for categorie in allCategories:
		checkbuttonValues.append(StringVar())
		cb = Checkbutton(groupCategories, text=categorie, variable=checkbuttonValues[checkbuttonRow], onvalue=categorie, offvalue="", command=selectCategorieEvent)
		cb.grid(row=checkbuttonRow, column=0, sticky=W)
		cb.deselect()
		checkbuttonRow = checkbuttonRow + 1
		
	
	listbox = Listbox(listboxframe, selectmode=MULTIPLE)
	listbox.grid(row=0, column=1, sticky=E)
	

	



	
	# Buttons
	#buttonOpenFile = Button(root, text="...", command=openFile, height =1)
	#buttonOpenFile.grid(row=0,column=3, sticky=W )

	buttonGO = Button(root, text="Request Upload!", command=displayText)
	buttonGO.grid()
	
	root.mainloop()
