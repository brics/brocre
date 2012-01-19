# robotpkg depend.mk for:	youbot-driver
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
YOUBOT_DRIVER_DEPEND_MK:= ${YOUBOT_DRIVER_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		youbot-driver
endif

ifeq (+,$(YOUBOT_DRIVER_DEPEND_MK))
PREFER.youbot-driver?=	robotpkg

DEPEND_USE+=		youbot-driver

DEPEND_ABI.youbot-driver?=	youbot-driver>=0.9
DEPEND_DIR.youbot-driver?=	../../hardware/youbot-driver

SYSTEM_SEARCH.youbot-driver=\
	youbot_driver/manifest.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
