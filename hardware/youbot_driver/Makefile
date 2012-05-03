# generated on 2012-02-10

PACKAGE_VERSION = 0.9
DISTNAME = youbot_driver-${PACKAGE_VERSION}
PKGNAME = youbot_driver-${PACKAGE_VERSION}
CATEGORIES = hardware youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Jan Paulus/jan.paulus@h-brs.de
HOMEPAGE = https://github.com/youbot/youbot_driver
COMMENT = youbot_driver
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../hardware/brics-external-packages-ros/depend.mk
include ../../mk/robotpkg.mk
