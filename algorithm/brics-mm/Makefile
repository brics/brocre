# robotpkg Makefile for:	algorithm/brics-mm
#

PACKAGE_VERSION=	0.1
DISTNAME     =		brics_mm-${PACKAGE_VERSION}
PKGNAME=		brics-mm-${PACKAGE_VERSION}
CATEGORIES=		algorithm
MASTER_SITES=		http://brics.inf.h-brs.de/
MASTER_REPOSITORY= 	svn https://svn.best-of-robotics.org/brics/BROCRE/BRICS_MM/trunk

MAINTAINER=		Walter Nowak
HOMEPAGE=		https://trac.best-of-robotics.org/brics/wiki/BRICS_MM/Mainpage
COMMENT=		BRICS_MM is the BRICS library for mobile manipulation
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes



do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk

