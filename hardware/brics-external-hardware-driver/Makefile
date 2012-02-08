# robotpkg Makefile for:	hardware/brics-external-hartware-driver
# Created:			Jan Paulus on 17 Aug 2010
#
PACKAGE_VERSION = 0.1
DISTNAME=		brics-external-hardware-driver-${PACKAGE_VERSION}
PKGNAME=		brics-external-hardware-driver-${PACKAGE_VERSION}
CATEGORIES=		hardware
MASTER_SITES=	http://brics.inf.h-brs.de/
MASTER_REPOSITORY= 	git git://github.com/janpaulus/brics-external-packages-ros.git
 
MAINTAINER=		jan.paulus@h-brs.de
HOMEPAGE=		https://github.com/janpaulus/brics-external-packages-ros
COMMENT=		third party software for BRICS hardware driver
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}


include ../../mk/robotpkg.mk

