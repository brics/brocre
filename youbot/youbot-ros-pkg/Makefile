# generated on 2013-03-13

PACKAGE_VERSION = 0.2c
DISTNAME = youbot-ros-pkg-${PACKAGE_VERSION}
PKGNAME = youbot-ros-pkg-${PACKAGE_VERSION}
CATEGORIES = youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Sebastian Blumenthal, Walter Nowak
HOMEPAGE = https://github.com/youbot/youbot-ros-pkg
COMMENT = ROS Stacks for the KUKA youBot
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../hardware/youbot_driver/depend.mk
include ../../mk/robotpkg.mk