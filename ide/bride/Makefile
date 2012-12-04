# generated on 2012-12-04

PACKAGE_VERSION = 0.1.2
DISTNAME = bride-${PACKAGE_VERSION}
PKGNAME = bride-${PACKAGE_VERSION}
CATEGORIES = IDE
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Maintained by Alexander Bubeck
HOMEPAGE = http://www.best-of-robotics.org
COMMENT = BRICS IDE for model driven engineering in ROS
LICENSE = modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk
