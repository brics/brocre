# generated on 2012-06-05

PACKAGE_VERSION = 0.2
DISTNAME = youbot-ros-pkg-${PACKAGE_VERSION}
PKGNAME = youbot-ros-pkg-${PACKAGE_VERSION}
CATEGORIES = youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Alexey Zakharov, Sebastian Blumenthal
HOMEPAGE = https://github.com/youbot/youbot-ros-pkg
COMMENT = youbot-ros-pkg
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk