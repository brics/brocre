# robotpkg depend.mk for:	youbot-applications
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
YOUBOT_APPLICATIONS_DEPEND_MK:= ${YOUBOT_APPLICATIONS_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		youbot-applications
endif

ifeq (+,$(YOUBOT_APPLICATIONS_DEPEND_MK))
PREFER.youbot-applications?=	robotpkg

DEPEND_USE+=		youbot-applications

DEPEND_ABI.youbot-applications?=	youbot-applications>=0.1
DEPEND_DIR.youbot-applications?=	../../youbot/youbot-applications

SYSTEM_SEARCH.youbot-applications=\
	youbot_applications/stack.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
