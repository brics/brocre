# generated on 2012-10-16

PACKAGE_VERSION = 0.1
DISTNAME = brics_mm-${PACKAGE_VERSION}
PKGNAME = brics_mm-${PACKAGE_VERSION}
CATEGORIES = algorithm
MASTER_SITES = http://brics.inf.h-brs.de/brocre/
MASTER_REPOSITORY = 

MAINTAINER = Walter Nowak
HOMEPAGE = https://trac.best-of-robotics.org/brics/wiki/BRICS_MM
COMMENT = BRICS_MM is the BRICS library for mobile manipulation
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk
