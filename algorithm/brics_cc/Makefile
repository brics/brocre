# generated on 2013-04-09

PACKAGE_VERSION = 1.0
DISTNAME = brics_cc-${PACKAGE_VERSION}
PKGNAME = brics_cc-${PACKAGE_VERSION}
CATEGORIES = algorithm
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Markus Klotzbuecher, markus.klotzbuecher@mech.kuleuven.be
HOMEPAGE = http://people.mech.kuleuven.be/~mklotzbucher/rfsm/README.html
COMMENT = rFSM reduced Statecharts
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk