import rospkg
import commands
import string
import os
import sys

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
    ROBOT_PACKAGE_PATH = "../../"
    
    packageDescriptionFolders = extractPackagesFromRobotPKGMakefile(ROBOT_PACKAGE_PATH + MAKEFILE_NAME)

    packageDescriptionsList = dict()
    
    #load hashmap key=Robotpkg Category/Folder, value = packageList
    for folder in packageDescriptionFolders:
        packageDescriptionsList[folder] = extractPackagesFromRobotPKGMakefile(ROBOT_PACKAGE_PATH + folder +"/"+ MAKEFILE_NAME)
        
    allPackages = []

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
            
    return allPackages
            

def parseRobotpkgInfo(inputtext,currentpackage):
    text = inputtext.split("\n")
    for line in text:
        if currentpackage.name in line:
            newline = line.split(" ")
            currentpackage.installedVersion = newline[0][len(currentpackage.name)+1:]

def generateBrocreFiles(packageName, categorie, masterSite, version, dependencies, brocrefolder):

    try:
        package = rospkg.RosStack()
        package.get_manifest(packageName)
        fileToCheckIfInstall = packageName + "/stack.xml"
    #    version = package.get_manifest(packageName).version
    except:
        try:
            package = rospkg.RosPack()
            package.get_manifest(packageName)
            fileToCheckIfInstall = packageName + "/manifest.xml"
        except:
            print "it is not a ros stack or package"
            exit(0)
    

    folderName = package.get_path(packageName)
    tarFileName = packageName +"-"+ version+ ".tar.gz"
    
    if not os.path.exists(brocrefolder+'/'+packageName):
        os.makedirs(brocrefolder+'/'+packageName)
    
    print "create Makefile file"
    makefile = open(brocrefolder+'/'+packageName+'/Makefile', 'w')
    versionstring = "PACKAGE_VERSION"
    makefile.write(versionstring +" = "+ version+"\n")
    makefile.write("DISTNAME = "+ packageName+"-${"+versionstring+"}\n")
    makefile.write("PKGNAME = "+ packageName+"-${"+versionstring+"}\n")
    makefile.write("CATEGORIES = " + categorie + "\n")
    makefile.write("MASTER_SITES = "+ masterSite+"\n")
    makefile.write("MASTER_REPOSITORY = \n\n")

    makefile.write("MAINTAINER = " + package.get_manifest(packageName).author +"\n")
    makefile.write("HOMEPAGE = " + package.get_manifest(packageName).url +"\n")
    makefile.write("COMMENT = " + package.get_manifest(packageName).brief +"\n")
    makefile.write("LICENSE = " + package.get_manifest(packageName).license +"\n\n")
    makefile.write("NO_CONFIGURE = yes\nNO_BUILD = yes\nNO_EXTRACT = yes\n\n")
    makefile.write("do-install:\n\t${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}\n\n")
    
    for depend in dependencies:
        makefile.write("include ../../" + depend + "/depend.mk\n")
        
    makefile.write("include ../../mk/robotpkg.mk")
    makefile.close()

    DESCR = open(brocrefolder+'/'+packageName+'/DESCR', 'w')
    DESCR.write(package.get_manifest(packageName).description)
    DESCR.close()

    print "create depend.mk file"
    depend_mk = open(brocrefolder+'/'+packageName+'/depend.mk', 'w')
    depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH}+\n")
    depend_mk.write(packageName + "_DEPEND_MK:= ${" + packageName + "_DEPEND_MK}+\n\n")
    depend_mk.write("ifeq (+,$(DEPEND_DEPTH))\n")
    depend_mk.write("DEPEND_PKG+=        "+packageName+"\n")
    depend_mk.write("endif\n\n")

    depend_mk.write("ifeq (+,$(" + packageName + "_DEPEND_MK))\n")
    depend_mk.write("PREFER." + packageName + "?=    robotpkg\n\n")

    depend_mk.write("DEPEND_USE+=        " + packageName + "\n\n")

    depend_mk.write("DEPEND_ABI." + packageName + "?=    " + packageName + ">=" + version + "\n")
    depend_mk.write("DEPEND_DIR." + packageName + "?=    ../../" + brocrefolder + "/" + packageName + "\n\n")

    depend_mk.write("SYSTEM_SEARCH." + packageName + "=\ \n")
    depend_mk.write("    "+fileToCheckIfInstall + "\n")
    depend_mk.write("endif\n\n")

    depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}\n")
    depend_mk.close()

    print "create tarball"
    commands.getoutput("mkdir "+folderName+"/../"+brocrefolder)
    commands.getoutput("ln -s "+folderName+" "+folderName+"/../"+brocrefolder+"/"+packageName)
    commands.getoutput("tar -czf "+tarFileName+" --exclude-vcs -h -C"+ folderName+"/.. " +brocrefolder)
    #commands.getoutput("tar -czf "+tarFileName+" --exclude-vcs -C"+ folderName+"/.. " +packageName)
    commands.getoutput("rm "+folderName+"/../"+brocrefolder+"/"+packageName)
    commands.getoutput("rmdir "+folderName+"/../"+brocrefolder)

    print "create PLIST file"
    commands.getoutput("tar -tf "+tarFileName+" | grep -P -v '/$' > "+brocrefolder+'/'+packageName+"/PLIST")

    print "compute checksums"
    distinfo = open(brocrefolder+'/'+packageName+'/distinfo', 'w')
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
        print "python gen_brocre_package.py <packageName> <categorie> <masterSite> <version> <brocre_folder>"
    else:
        parseManifest(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


