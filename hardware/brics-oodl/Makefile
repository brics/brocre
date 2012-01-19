# robotpkg Makefile for:	hardware/brics-oodl
#

BRICS_OODL_VERSION=	0.1
DISTNAME=		brics-oodl-${BRICS_OODL_VERSION}
PKGNAME=		brics-oodl-${BRICS_OODL_VERSION}
CATEGORIES=		hardware
MASTER_SITES=		http://brics.inf.h-brs.de/
MASTER_REPOSITORY= 	git git://github.com/janpaulus/BRICS_OODL.git

MAINTAINER=		jan.paulus@h-brs.de
HOMEPAGE=		www.youbot-store.com
COMMENT=		BRICS OODL
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}


include ../../mk/robotpkg.mk

