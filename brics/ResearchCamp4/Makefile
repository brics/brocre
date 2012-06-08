# generated on 2012-06-08

PACKAGE_VERSION = 0.9
DISTNAME = ResearchCamp4-${PACKAGE_VERSION}
PKGNAME = ResearchCamp4-${PACKAGE_VERSION}
CATEGORIES = hardware youbot
MASTER_SITES = http://brics.inf.h-brs.de/
MASTER_REPOSITORY = 

MAINTAINER = Frederik Hegger, Jan Paulus, Nico Hochgeschwender, Azamat Shakhimardanov
HOMEPAGE = https://github.com/b-it-bots/ResearchCamp4
COMMENT = BRICS Research Camp 4 software
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../youbot/b-it-bots_youbot-ros-pkg/depend.mk
include ../../youbot/b-it-bots_youbot-manipulation/depend.mk
include ../../hardware/youbot_driver/depend.mk
include ../../mk/robotpkg.mk
