# generated on 2013-04-22

PACKAGE_VERSION = 0.1
DISTNAME = bcm_roi_filter-${PACKAGE_VERSION}
PKGNAME = bcm_roi_filter-${PACKAGE_VERSION}
CATEGORIES = bride_models
MASTER_SITES = http://brics.inf.h-brs.de/brocre/
MASTER_REPOSITORY = 

MAINTAINER = Alexander Bubeck
HOMEPAGE = https://github.com/abubeck
COMMENT = BCM model for a region of interest filter (ROI)
LICENSE = modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk
