import rospkg
import commands
import string
import os

ros_root = rospkg.get_ros_root()

r = rospkg.RosPack()
depends = r.get_depends('roscpp')
path = r.get_path('rospy')

package = rospkg.RosPack()

# infos which are needed

packageName  = "brics_3d"
fileToCheckIfInstall  = "brics_3d/manifest.xml"
categorie  = "algorithm"
masterSite = "http://brics.inf.h-brs.de/"

version = "0.1"

folderName = packageName
tarFileName = packageName +"-"+ version+ ".tar.gz"

print "create Makefile file"
makefile = open('Makefile', 'w')
versionstring = packageName + "_version"
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
makefile.write("include ../../mk/robotpkg.mk")
makefile.close()

DESCR = open('DESCR', 'w')
DESCR.write(package.get_manifest(packageName).description)
DESCR.close()

print "create depend.mk file"
depend_mk = open('depend.mk', 'w')
depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH}+\n")
depend_mk.write(packageName + "_DEPEND_MK:= ${" + packageName + "_DEPEND_MK}+\n\n")
depend_mk.write("ifeq (+,$(DEPEND_DEPTH))\n")
depend_mk.write("DEPEND_PKG+=        "+packageName+"\n")
depend_mk.write("endif\n\n")

depend_mk.write("ifeq (+,$(" + packageName + "_DEPEND_MK))\n")
depend_mk.write("PREFER." + packageName + "?=    robotpkg\n\n")

depend_mk.write("DEPEND_USE+=        " + packageName + "\n\n")

depend_mk.write("DEPEND_ABI." + packageName + "?=    " + packageName + ">=" + version + "\n")
depend_mk.write("DEPEND_DIR." + packageName + "?=    ../../" + categorie + "/" + packageName + "\n\n")

depend_mk.write("SYSTEM_SEARCH." + packageName + "=\ \n")
depend_mk.write("    "+fileToCheckIfInstall + "\n")
depend_mk.write("endif\n\n")

depend_mk.write("DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}\n")
depend_mk.close()

print "create PLIST file"
commands.getoutput("find "+ folderName+"/* -type f -not -iwholename '*.svn*' > PLIST")

print "create tarball"
commands.getoutput("tar -czf "+tarFileName+" --exclude=\".svn\" "+ folderName)

print "compute checksums"
distinfo = open('distinfo', 'w')
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



