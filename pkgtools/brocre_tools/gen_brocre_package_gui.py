# File: hello1.py

from Tkinter import *

import os
import tkMessageBox

global entryWidgetPackageName
global entryWidgetCategorie
global entryWidgetVersion
global entryWidgetMasterSite
global entryWidgetManifest

def displayText():
	""" Display the Entry text value. """
	
	#Show Error if values are not entered
	error = ""
	if entryWidgetPackageName.get().strip() == "":
		error = error + "Insert Package Name"  
	if entryWidgetCategorie.get().strip() == "":
		error = error + "\nInsert Package Categorie"  
	if entryWidgetVersion.get().strip() == "":
		error = error + "\nInsert Package Version"  
	if entryWidgetMasterSite.get().strip() == "":
		error = error + "\nInsert Package Master Site"  
	if entryWidgetManifest.get().strip() == "":
		error = error + "\nInsert Manifest File" 
	if not error == "":
		tkMessageBox.showerror(message=error)
	else:
		tkMessageBox.showinfo("Result", "Package Name: " + entryWidgetPackageName.get().strip() 
			+ "\n Package Categorie: " + entryWidgetCategorie.get().strip() 
			+ "\n Package Version: " + entryWidgetVersion.get().strip()
			+ "\n Package MasterSite: " + entryWidgetMasterSite.get().strip()
			+ "\n Package Manifest: " + entryWidgetManifest.get().strip())


if __name__ == "__main__":

	SUBDIR_STRING = "SUBDIR+="
	ROBOT_PACKAGE_PATH = "../../"
	
	'''------------------------------------------------------------------------------------------------'
	-- Parse the RobotPKG mainfolder Makefile to identify all folders containing package description --
	-------------------------------------------------------------------------------------------------'''
	
	packageFoldersDescriptionFile = ROBOT_PACKAGE_PATH + "Makefile"
	packageDescriptionFolders = []

	# Open Makefile which contains Package Description folders
	f = file(packageFoldersDescriptionFile)

	#Check every line if it contains SUBDIR+= and is not commented out via '#'
	for line in f:
		if not '#' in line and SUBDIR_STRING in line:		
			packageDescriptionFolders.append(line[len(SUBDIR_STRING):].lstrip().rstrip())
	print packageDescriptionFolders

	for folder in packageDescriptionFolders:
		dirList=os.listdir(ROBOT_PACKAGE_PATH + folder)
		for fname in dirList:
			print fname

	
	# Create the GUI
	  
	root = Tk()
	root.title("BROCRE Package Generator")

	# Frame for lables for the input fields
	lableFrame = Frame(root)
	fontSize = 10 

	labelPackageName = Label(lableFrame, font=("Helvetica", fontSize))
	labelPackageName["text"] = "Package Name:"
	labelPackageName.pack(side=TOP, anchor=W)

	labelCategorie = Label(lableFrame, font=("Helvetica", fontSize))
	labelCategorie["text"] = "Category:"
	labelCategorie.pack(side=TOP, anchor=W)

	labelVersion = Label(lableFrame, font=("Helvetica", fontSize))
	labelVersion["text"] = "Version:"
	labelVersion.pack(side=TOP, anchor=W)

	labelMasterSite = Label(lableFrame, font=("Helvetica", fontSize))
	labelMasterSite["text"] = "Master Site:"
	labelMasterSite.pack(side=TOP, anchor=W)

	labelManifest = Label(lableFrame, font=("Helvetica", fontSize))
	labelManifest["text"] = "ManifestFile:"
	labelManifest.pack(side=TOP, anchor=W)

	lableFrame.pack(side=LEFT, fill=BOTH)


	#Frame input boxes
	entryWidgetFrame = Frame(root)

	entryWidgetPackageName = Entry(entryWidgetFrame)
	entryWidgetPackageName["width"] = 25
	entryWidgetPackageName.pack(side=TOP)

	entryWidgetCategorie = Entry(entryWidgetFrame)
	entryWidgetCategorie["width"] = 25
	entryWidgetCategorie.pack(side=TOP)

	entryWidgetVersion = Entry(entryWidgetFrame)
	entryWidgetVersion["width"] = 25
	entryWidgetVersion.pack(side=TOP)

	entryWidgetMasterSite = Entry(entryWidgetFrame)
	entryWidgetMasterSite["width"] = 25
	entryWidgetMasterSite.pack(side=TOP)

	entryWidgetManifest = Entry(entryWidgetFrame)
	entryWidgetManifest["width"] = 25
	entryWidgetManifest.pack(side=TOP)

	entryWidgetFrame.pack(side=LEFT, fill=BOTH)

	buttonGO = Button(root, text="GO!", command=displayText)
	buttonGO.pack()

	root.mainloop()
