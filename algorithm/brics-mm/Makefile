# robotpkg Makefile for:	algorithm/brics-mm
#

BRICS_MM_VERSION=	0.1
DISTNAME=		brics-mm-${BRICS_MM_VERSION}
PKGNAME=		brics-mm-${BRICS_MM_VERSION}
CATEGORIES=		hardware
MASTER_SITES=		https://github.com/youbot/youbot_driver/wiki/
MASTER_REPOSITORY= 	svn https://svn.best-of-robotics.org/brics/BROCRE/BRICS_MM/trunk

MAINTAINER=		Sebastian Blumenthal
HOMEPAGE=		https://trac.best-of-robotics.org/brics/wiki/BRICS_MM/Mainpage
COMMENT=		BRICS_MM is the BRICS library for mobile manipulation
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk

