# robotpkg depend.mk for:	youbot-stack-locomotec
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
YOUBOT_STACK_LOCOMOTEC_DEPEND_MK:= ${YOUBOT_STACK_LOCOMOTEC_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		youbot-stack-locomotec
endif

ifeq (+,$(YOUBOT_STACK_LOCOMOTEC_DEPEND_MK))
PREFER.youbot-stack-locomotec?=	robotpkg

DEPEND_USE+=		youbot-stack-locomotec

DEPEND_ABI.youbot-stack-locomotec?=	youbot-stack-locomotec>=0.1
DEPEND_DIR.youbot-stack-locomotec?=	../../youbot/youbot-stack-locomotec

SYSTEM_SEARCH.youbot-stack-locomotec=\
	youbot-ros-pkg/youbot_common/stack.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
