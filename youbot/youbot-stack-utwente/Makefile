# robotpkg Makefile for:	youbot/youbot-stack-utwente
#

YOUBOT_STACK_UTWENTE_VERSION=	0.1
DISTNAME=		youbot-stack-utwente-${YOUBOT_STACK_UTWENTE_VERSION}
PKGNAME=		youbot-stack-utwente-${YOUBOT_STACK_UTWENTE_VERSION}
CATEGORIES=		hardware
MASTER_SITES=		http://brics.inf.h-brs.de/
#MASTER_REPOSITORY= 	git git://github.com/b-it-bots/youbot-stack.git

MAINTAINER=		Robert Wilterdink
HOMEPAGE=		http://github.com/b-it-bots/youbot-stack
COMMENT=		youBot contol stack of the University of Twente
LICENSE=		gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE=		yes
NO_BUILD=		yes
NO_EXTRACT=		yes
#NO_INSTALL= 		no


do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../mk/robotpkg.mk

