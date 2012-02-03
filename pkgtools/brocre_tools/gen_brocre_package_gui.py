# File: hello1.py

from Tkinter import *

import os
import tkMessageBox
import tkFileDialog 

import gen_brocre_package

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

	
	SUBDIR_STRING = "SUBDIR+="
	ROBOT_PACKAGE_PATH = "../../"
	
	root = Tk()
	root.title("BROCRE Package Generator")
	
	# Create the GUI
	  	
	# Frame for lables for the input fields
	labelManifest = Label(root, text="ManifestFile:").grid(row=0, sticky=W)
	labelPackageName = Label(root, text="Package Name:").grid(row=1, sticky=W)
	labelCategorie = Label(root, text="Category:").grid(row=2, sticky=W)
	labelVersion = Label(root, text="Version:").grid(row=3, sticky=W) 
	labelMasterSite = Label(root, text="Master Site:").grid(row=4, sticky=W	) 

	#Frame input boxes
	entryWidgetManifest = Entry(root, width=25)
	entryWidgetManifest.grid(row=0, column=1, sticky=W)
	entryWidgetPackageName = Entry(root, width=25)
	entryWidgetPackageName.grid(row=1, column=1, sticky=W)
	entryWidgetCategorie = Entry(root, width=25)
	entryWidgetCategorie.grid(row=2, column=1, sticky=W)
	entryWidgetVersion = Entry(root, width=25)
	entryWidgetVersion.grid(row=3, column=1, sticky=W)
	entryWidgetMasterSite = Entry(root, width=25)
	entryWidgetMasterSite.grid(row=4, column=1, sticky=W)

	#File Dialog button
	buttonOpenFile = Button(root, text="...", command=openFile, height =1)
	buttonOpenFile.grid(row=0,column=3, sticky=W )

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

	packageDescriptionFileList=[]
	mycolumn = -1
	# Iterate over Folders to collect all files and create a checkbox for each
	for folder in packageDescriptionFolders:
		mycolumn = mycolumn+1
		packageDescriptionFileList=os.listdir(ROBOT_PACKAGE_PATH + folder)
		# add lable above
		myrow=6
		labelManifest = Label(root, text=folder).grid(sticky=W, column=mycolumn, row=myrow)
		for fname in packageDescriptionFileList:
			myrow=myrow+1
			if not fname.strip() == "Makefile": 
				var = StringVar()
				c = Checkbutton(root, text=fname, variable=fname, onvalue="RGB", offvalue="L")
				c.deselect()
				c.grid(sticky=W, column=mycolumn, row=myrow)
			else:
				myrow = myrow-1


	buttonGO = Button(root, text="GO!", command=displayText)
	buttonGO.grid()
	

	root.mainloop()
