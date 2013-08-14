# generated on 2012-02-10

PACKAGE_VERSION = 0.1
DISTNAME = brics-oodl-${PACKAGE_VERSION}
PKGNAME = brics-oodl-${PACKAGE_VERSION}
CATEGORIES = hardware
MASTER_SITES = http://brics.inf.h-brs.de/brocre/
MASTER_REPOSITORY = 

MAINTAINER = BRSU
HOMEPAGE = https://github.com/janpaulus/BRICS_OODL
COMMENT = brics-oodl
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk
