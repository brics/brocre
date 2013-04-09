# generated on 2013-04-09

PACKAGE_VERSION = 1.0
DISTNAME = brics_cc-${PACKAGE_VERSION}
PKGNAME = brics_cc-${PACKAGE_VERSION}
CATEGORIES = control_coordination
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Markus Klotzbuecher
HOMEPAGE = https://github.com/kmarkus/rFSM
COMMENT = rFSM is a reduced (lightweight) Statechart implementation written in pure Lua.
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk