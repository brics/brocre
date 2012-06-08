# generated on 2012-06-08

PACKAGE_VERSION = 0.1
DISTNAME = b-it-bots_youbot-ros-pkg-${PACKAGE_VERSION}
PKGNAME = b-it-bots_youbot-ros-pkg-${PACKAGE_VERSION}
CATEGORIES = youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Frederik Hegger, Jan Paulus
HOMEPAGE = https://github.com/b-it-bots/youbot-ros-pkg
COMMENT = b-it-bots fork youbot-ros-pkg
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../hardware/youbot_driver/depend.mk
include ../../mk/robotpkg.mk