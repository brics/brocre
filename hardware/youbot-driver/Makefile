# robotpkg Makefile for:	hardware/youbot-driver
# Created:			Jan Paulus on 17 Aug 2010
#

YOUBOT_DRIVER_VERSION=	0.91
DISTNAME=		youbot-driver-${YOUBOT_DRIVER_VERSION}
PKGNAME=		youbot-driver-${YOUBOT_DRIVER_VERSION}
CATEGORIES=		hardware
MASTER_SITES=		https://github.com/youbot/youbot_driver/wiki/
MASTER_REPOSITORY= 	git git://github.com/youbot/youbot_driver.git

MAINTAINER=		jan.paulus@h-brs.de
HOMEPAGE=		http://github.com/youbot/youbot_driver
COMMENT=		Drivers for the KUKA youBot robot
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../hardware/brics-external-hardware-driver/depend.mk
include ../../mk/robotpkg.mk

