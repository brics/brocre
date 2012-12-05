# generated on 2012-12-05

PACKAGE_VERSION = 0.1.1
DISTNAME = brics_3d_bride_models-${PACKAGE_VERSION}
PKGNAME = brics_3d_bride_models-${PACKAGE_VERSION}
CATEGORIES = bride_models perception
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Sebastian Blumenthal/blumenthal@gps-stuttgart.de
HOMEPAGE = http://ros.org/wiki/brics_3d_bride_models
COMMENT = brics_3d_bride_models
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../algorithm/brics_3d/depend.mk
include ../../algorithm/brics_3d_experimental/depend.mk
include ../../mk/robotpkg.mk