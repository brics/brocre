# generated on 2012-12-04

PACKAGE_VERSION = 0.1
DISTNAME = hbrs-ros-pkg-${PACKAGE_VERSION}
PKGNAME = hbrs-ros-pkg-${PACKAGE_VERSION}
CATEGORIES = algorithm
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Frederik Hegger
HOMEPAGE = robotics.inf.h-brs.de
COMMENT = ROS stacks from the Bonn-Rhein-Sieg University
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk