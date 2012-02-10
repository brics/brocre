# generated on 2012-02-10

PACKAGE_VERSION = 0.1
DISTNAME = brics-3d-${PACKAGE_VERSION}
PKGNAME = brics-3d-${PACKAGE_VERSION}
CATEGORIES = algorithm perception
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Sebastian Blumenthal/blumenthal@gps-stuttgart.de
HOMEPAGE = https://trac.best-of-robotics.org/brics/wiki/BRICS_3D/Mainpage
COMMENT = brics_3d
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk