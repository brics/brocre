# generated on 2013-03-13

PACKAGE_VERSION = 0.1.2
DISTNAME = brics_3d_experimental-${PACKAGE_VERSION}
PKGNAME = brics_3d_experimental-${PACKAGE_VERSION}
CATEGORIES = algorithm
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Sebastian Blumenthal
HOMEPAGE = https://github.com/blumenthal/brics_3d_experimental
COMMENT = BRICS_3D helper tools for the ROS framework
LICENSE = modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../algorithm/brics_3d/depend.mk
include ../../mk/robotpkg.mk