# generated on 2013-03-11

PACKAGE_VERSION = 0.1.2
DISTNAME = fetch_and_carry_scenario-${PACKAGE_VERSION}
PKGNAME = fetch_and_carry_scenario-${PACKAGE_VERSION}
CATEGORIES = youbot
MASTER_SITES = http://brics.inf.h-brs.de/brocre/
MASTER_REPOSITORY = 

MAINTAINER = Frederik Hegger, Jan Paulus
HOMEPAGE = http://www.b-it-bots.de
COMMENT = Fetch&Carry scenario of the Bonn-Rhein-Sieg University
LICENSE = gnu-lgpl-v2.1 modified-bsd

NO_CONFIGURE = yes
NO_BUILD = yes
NO_EXTRACT = yes

do-install:
	${RUN} tar -C $(ROBOTPKG_BASE) -xvf ${DISTDIR}/${DISTNAME}${EXTRACT_SUFX}

include ../../interfaces/brics-interfaces/depend.mk
include ../../algorithm/brics_3d/depend.mk
include ../../models/brics_3d_bride_models/depend.mk
include ../../algorithm/brics_3d_experimental/depend.mk
include ../../algorithm/hbrs-ros-pkg/depend.mk
include ../../youbot/youbot-manipulation/depend.mk
include ../../youbot/youbot-ros-pkg/depend.mk
include ../../hardware/youbot_driver/depend.mk
include ../../mk/robotpkg.mk
