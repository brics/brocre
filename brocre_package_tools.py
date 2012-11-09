import commands
import string
import os
import sys
import time
from datetime import date

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
        self.brief = ""
        self.dependencies = []
        self.masterSite = "" 
        self.fileToCheckIfInstall = ""
        self.sourcePath = ""


def extractPackagesFromRobotPKGMakefile(MakefilePath):
    COMMENT_IN_MAKEFILE = "#"
    SUBDIR_STRING = "SUBDIR+="
    Makefile = file(MakefilePath)
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
            
    #filehandle.close()


def extractPackageDescriptions():
    # Parse Makefile which contains Package Description folders
    MAKEFILE_NAME = "Makefile"
    ROBOT_PACKAGE_PATH = "./"
    
    packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(ROBOT_PACKAGE_PATH + MAKEFILE_NAME)

    packageDescriptionsList = dict()
    
    #load hashmap key=Robotpkg Category/Folder, value = packageList
    for folder in packageDescriptionFolders:
        packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME)
        
    allPackages = []
    
    for folder in packageDescriptionsList.keys():
        for package in packageDescriptionsList[folder]:
            currentpackage = packageDescription()
            parsePKGMakefile(ROBOT_PACKAGE_PATH + folder +"/" +  package + "/Makefile", currentpackage)
            DESCRfile = file(ROBOT_PACKAGE_PATH + folder +"/" +  package +"/DESCR")
            currentpackage.description = DESCRfile.read()
            DESCRfile.close()
            currentpackage.name = package
            currentpackage.folder = folder
            robotpkgInfoText = commands.getoutput("robotpkg_info -e "+currentpackage.name)
            compareInstalledVersionWithCurrentPackageVersion(robotpkgInfoText,currentpackage)
            allPackages.append(currentpackage)
    
    #check for packages which have been install but the package has been removed from brocre
    robotpkgInfoText = commands.getoutput("robotpkg_info -u")
    robotpkgInfoText = robotpkgInfoText.split("\n")
    for line in robotpkgInfoText:
        packageDescriptionAvailable = False
        for package in allPackages:
            if package.name in line:
                packageDescriptionAvailable = True
        if line == "":
            packageDescriptionAvailable = True
        if packageDescriptionAvailable == False:
          newpackage = packageDescription()
          newpackage.name = line.split(" ")[0]
          newpackage.categories = ["unknown"]    
          newpackage.installedVersion = "-"
          newpackage.version = "-"
          allPackages.append(newpackage)
            
    return allPackages
            

def compareInstalledVersionWithCurrentPackageVersion(inputtext,currentpackage):
    text = inputtext.split("\n")
    for line in text:
        if currentpackage.name in line:
            newline = line.split(" ")
            currentpackage.installedVersion = newline[0][len(currentpackage.name)+1:]

def generateBrocreFiles(package):


    if not os.path.exists(package.folder+'/'+package.name):
        os.makedirs(package.folder+'/'+package.name)
    
    print "create Makefile file"
    makefile = open(package.folder+'/'+package.name+'/Makefile', 'w')
    versionstring = "PACKAGE_VERSION"
    makefile.write("# generated on "+ date.today().__str__() +"\n\n")
    makefile.write(versionstring +" = "+ package.version+"\n")
    makefile.write("DISTNAME = "+ package.name+"-${"+versionstring+"}\n")
    makefile.write("PKGNAME = "+ package.name+"-${"+versionstring+"}\n")      
    makefile.write("CATEGORIES = " + package.categories + "\n")
    makefile.write("MASTER_SITES = "+ package.masterSite+"\n")
    makefile.write("MASTER_REPOSITORY = \n\n")

    makefile.write("MAINTAINER = " + package.maintainer +"\n")
    makefile.write("HOMEPAGE = " + package.homepage +"\n")
    makefile.write("COMMENT = " + package.brief +"\n")
    makefile.write("LICENSE = " + package.license +"\n\n")
    makefile.write("NO_CONFIGURE = yes\nNO_BUILD = yes\nNO_EXTRACT = yes\n\n")
    makefile.write("do-install:\n\t${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}\n\n")
    
    for depend in package.dependencies:
        makefile.write("include ../../" + depend + "/depend.mk\n")
        
    makefile.write("include ../../mk/robotpkg.mk")
    makefile.close()

    DESCR = open(package.folder+'/'+package.name+'/DESCR', 'w')
    DESCR.write(package.description)
    DESCR.close()

    print "create depend.mk file"
    depend_mk = open(package.folder+'/'+package.name+'/depend.mk', 'w')
    depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH}+\n")
    depend_mk.write(package.name + "_DEPEND_MK:= ${" + package.name + "_DEPEND_MK}+\n\n")
    depend_mk.write("ifeq (+,$(DEPEND_DEPTH))\n")
    depend_mk.write("DEPEND_PKG+=        "+package.name+"\n")
    depend_mk.write("endif\n\n")

    depend_mk.write("ifeq (+,$(" + package.name + "_DEPEND_MK))\n")
    depend_mk.write("PREFER." + package.name + "?=    robotpkg\n\n")

    depend_mk.write("DEPEND_USE+=        " + package.name + "\n\n")

    depend_mk.write("DEPEND_ABI." + package.name + "?=    " + package.name + ">=" + package.version + "\n")
    depend_mk.write("DEPEND_DIR." + package.name + "?=    ../../" + package.folder + "/" + package.name + "\n\n")

    depend_mk.write("SYSTEM_SEARCH." + package.name + "="+package.folder+"/"+package.fileToCheckIfInstall + "\n")
    depend_mk.write("endif\n\n")

    depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}\n")
    depend_mk.close()

    print "create tarball"
    tarFileName = package.name +"-"+ package.version+ ".tar.gz"
    commands.getoutput("mkdir "+package.sourcePath+"/../"+package.folder)
    commands.getoutput("ln -s "+package.sourcePath+" "+package.sourcePath+"/../"+package.folder+"/"+package.name)
    commands.getoutput("tar -czf "+tarFileName+" --exclude-vcs -h -C"+ package.sourcePath+"/.. " +package.folder)
    #commands.getoutput("tar -czf "+tarFileName+" --exclude-vcs -C"+ package.sourcePath+"/.. " +package.name)
    commands.getoutput("rm "+package.sourcePath+"/../"+package.folder+"/"+package.name)
    commands.getoutput("rmdir "+package.sourcePath+"/../"+package.folder)

    print "create PLIST file"
    commands.getoutput("tar -tf "+tarFileName+" | grep -P -v '/$' > "+package.folder+'/'+package.name+"/PLIST")

    print "compute checksums"
    distinfo = open(package.folder+'/'+package.name+'/distinfo', 'w')
    line = commands.getoutput("openssl sha1 "+ tarFileName) + "\n"
    line = string.replace(line, "SHA1", "SHA1 ")
    line = string.replace(line, ")=", ") =")
    distinfo.write(line)

    line = commands.getoutput("openssl rmd160 "+ tarFileName) + "\n"
    line = string.replace(line, "RIPEMD160", "RMD160 ")
    line = string.replace(line, ")=", ") =")
    distinfo.write(line)

    filesize = os.path.getsize(tarFileName)
    distinfo.write("Size (" + tarFileName + ") = " + str(filesize) + " bytes")
    distinfo.close()

    print "Finished"


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print "Please specify the parameters:\n"
        print "python gen_brocre_package.py <packagecription class>"
    else:
        parseManifest(sys.argv[1])


