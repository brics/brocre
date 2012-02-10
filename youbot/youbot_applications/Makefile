# generated on 2012-02-10

PACKAGE_VERSION = 0.1
DISTNAME = youbot_applications-${PACKAGE_VERSION}
PKGNAME = youbot_applications-${PACKAGE_VERSION}
CATEGORIES = youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Maintained by Sebastian Blumenthal
HOMEPAGE = https://github.com/youbot/youbot_applications
COMMENT = youbot_applications
LICENSE = modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../hardware/youbot_driver/depend.mk
include ../../mk/robotpkg.mk
