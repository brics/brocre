# generated on 2012-02-10

PACKAGE_VERSION = 0.1
DISTNAME = brics-external-packages-ros-${PACKAGE_VERSION}
PKGNAME = brics-external-packages-ros-${PACKAGE_VERSION}
CATEGORIES = hardware
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Maintained by Jan Paulus
HOMEPAGE = https://github.com/janpaulus/brics-external-packages-ros
COMMENT = brics-external-hardware-driver
LICENSE = modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk