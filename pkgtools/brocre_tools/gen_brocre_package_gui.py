# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 

#Ros Stuff
import rospkg

#Pakage Generation Script
import gen_brocre_package

global listBoxPackageName
global entryWidgetCategorie
global entryWidgetVersion
global entryWidgetMasterSite
global entryWidgetManifest

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
	
	#Show Error if values are not entered
	error = ""
	if listBoxPackageName.get().strip() == "":
		error = error + "Insert Package Name"  
	if entryWidgetCategorie.get().strip() == "":
		error = error + "\nInsert Package Categorie"  
	if entryWidgetVersion.get().strip() == "":
		error = error + "\nInsert Package Version"  
	if entryWidgetMasterSite.get().strip() == "":
		error = error + "\nInsert Package Master Site"  
	if entryWidgetManifest.get().strip() == "":
		error = error + "\nInsert Manifest File" 
	elif not os.path.isfile(entryWidgetManifest.get().strip()):
		error = error + "\nGiven Manifest file doesn't exist" 
		
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		tkMessageBox.showinfo("Result", "Package Name: " + entryWidgetPackageName.get().strip() 
			+ "\n Package Categorie: " + entryWidgetCategorie.get().strip() 
			+ "\n Package Version: " + entryWidgetVersion.get().strip()
			+ "\n Package MasterSite: " + entryWidgetMasterSite.get().strip()
			+ "\n Package Manifest: " + entryWidgetManifest.get().strip())
		
		gen_brocre_package.parseManifest(entryWidgetPackageName.get().strip(),
			entryWidgetManifest.get().strip(),
			entryWidgetCategorie.get().strip(),
			entryWidgetMasterSite.get().strip(),
			entryWidgetVersion.get().strip())

'''
Let the user choose a manifest file
'''
def openFile():
	ftypes = [('Manifest files', '*.xml'), ('All files', '*')]
	dlg = tkFileDialog.Open(root, filetypes = ftypes)
	fl = dlg.show()
	entryWidgetManifest.insert(0, fl)

		
if __name__ == "__main__":
	
	''' Get all ROS stacks '''
	rosStackCommand = rospkg.RosStack() 	# get ref to rosstack
	rosStacksList = rosStackCommand.list() 	# get all available stacks

	''' Find all RobotPKG  package descriptions '''
	# Makefile Parser Definitions
	ROBOT_PACKAGE_PATH = "../../"
	MAKEFILE_NAME = "Makefile"

	packageFoldersDescriptionFile = ROBOT_PACKAGE_PATH + MAKEFILE_NAME
	
	# Parse Makefile which contains Package Description folders
	packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(file(packageFoldersDescriptionFile))
	packageDescriptionsList = dict()
	
	for folder in packageDescriptionFolders:
		packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(file(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME))
				
				
	''' Window Creation '''
	root = Tk()
	root.title("BROCRE Package Generator")
	  	
	# Text Lables
	labelPackageName = Label(root, text="Package Name:").grid(row=1, sticky=W)
	labelManifest = Label(root, text="ManifestFile:").grid(row=0, sticky=W)
	labelCategorie = Label(root, text="Category:").grid(row=2, sticky=W)
	labelVersion = Label(root, text="Version:").grid(row=3, sticky=W) 
	labelMasterSite = Label(root, text="Master Site:").grid(row=4, sticky=W	) 

	# Input fileds
	listBoxPackageName = Listbox(root, selectmode=BROWSE, relief=SUNKEN, width=25, height=5)
	for rosStack in rosStacksList:
		listBoxPackageName.insert(END, rosStack)
	
	listBoxPackageName.grid(row=1, column=1, sticky=W)
	entryWidgetManifest = Entry(root, width=25)
	entryWidgetManifest.grid(row=0, column=1, sticky=W)
	entryWidgetCategorie = Entry(root, width=25)
	entryWidgetCategorie.grid(row=2, column=1, sticky=W)
	entryWidgetVersion = Entry(root, width=25)
	entryWidgetVersion.grid(row=3, column=1, sticky=W)
	entryWidgetMasterSite = Entry(root, width=25)
	entryWidgetMasterSite.grid(row=4, column=1, sticky=W)
	
	# Buttons
	buttonOpenFile = Button(root, text="...", command=openFile, height =1)
	buttonOpenFile.grid(row=0,column=3, sticky=W )

	buttonGO = Button(root, text="GO!", command=displayText)
	buttonGO.grid()

	root.mainloop()
