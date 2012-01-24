# robotpkg Makefile for:	algorithm/brics-3d
#

BRICS_3d_VERSION=	0.1
DISTNAME=		brics-3d-${BRICS_3d_VERSION}
PKGNAME=		brics-3d-${BRICS_3d_VERSION}
CATEGORIES=		hardware
MASTER_SITES=		https://github.com/youbot/youbot_driver/wiki/
MASTER_REPOSITORY= 	svn https://svn.best-of-robotics.org/brics/BROCRE/BRICS_3D/trunk

MAINTAINER=		Sebastian Blumenthal
HOMEPAGE=		https://trac.best-of-robotics.org/brics/wiki/BRICS_3D/Mainpage
COMMENT=		BRICS_3D is the BRICS library for 3D perception and modeling
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk

