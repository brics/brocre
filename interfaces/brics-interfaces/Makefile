# robotpkg Makefile for:	youbot/brics-interfaces
#

PACKAGE_VERSION=	0.1
DISTNAME=		brics-interfaces-${PACKAGE_VERSION}
PKGNAME=		brics-interfaces-${PACKAGE_VERSION}
CATEGORIES=		interfaces
MASTER_SITES=		http://brics.inf.h-brs.de/brocre/
#MASTER_REPOSITORY= 	git git://github.com/b-it-bots/youbot-stack.git

MAINTAINER=		Alexander Bubeck
HOMEPAGE=		http://www.best-of-robotics.org/
COMMENT=		Interfaces used in the BRICS project
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}


include ../../mk/robotpkg.mk

