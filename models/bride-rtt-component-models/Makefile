# robotpkg Makefile for:	youbot/youbot-applications
#

PACKAGE_VERSION=	0.1
DISTNAME=		bride-rtt-component-models-${PACKAGE_VERSION}
PKGNAME=		bride-rtt-component-models-${PACKAGE_VERSION}
CATEGORIES=		OROCOS-RTT models
MASTER_SITES=		http://brics.inf.h-brs.de/
#MASTER_REPOSITORY= 	git git://github.com/b-it-bots/youbot-stack.git

MAINTAINER=		Azamat Shakhimardanov
HOMEPAGE=		https://github.com/nicoh/BRICS_Components
COMMENT=		OROCOS RTT component models
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk

