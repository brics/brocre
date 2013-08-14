# generated on 2013-03-11

PACKAGE_VERSION = 0.2
DISTNAME = hbrs-ros-pkg-${PACKAGE_VERSION}
PKGNAME = hbrs-ros-pkg-${PACKAGE_VERSION}
CATEGORIES = algorithm
MASTER_SITES = http://brics.inf.h-brs.de/brocre/
MASTER_REPOSITORY = 

MAINTAINER = Frederik Hegger
HOMEPAGE = https://github.com/b-it-bots/hbrs-ros-pkg
COMMENT = ROS stacks of the Bonn-Rhein-Sieg University
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk
