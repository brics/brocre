# generated on 2012-10-29

PACKAGE_VERSION = 0.2
DISTNAME = b-it-bots_youbot-manipulation-${PACKAGE_VERSION}
PKGNAME = b-it-bots_youbot-manipulation-${PACKAGE_VERSION}
CATEGORIES = hardware youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Sven Schneider
HOMEPAGE = http://ros.org/wiki/youbot-manipulation
COMMENT = youbot-manipulation
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk