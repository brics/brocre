# robotpkg depend.mk for:	youbot-stack-utwente
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
YOUBOT_STACK_UTWENTE_DEPEND_MK:= ${YOUBOT_STACK_UTWENTE_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		youbot-stack-utwente
endif

ifeq (+,$(YOUBOT_STACK_UTWENTE_DEPEND_MK))
PREFER.youbot-stack-utwente?=	robotpkg

DEPEND_USE+=		youbot-stack-utwente

DEPEND_ABI.youbot-stack-utwente?=	youbot-stack-utwente>=0.9
DEPEND_DIR.youbot-stack-utwente?=	../../youbot/youbot-stack-utwente

SYSTEM_SEARCH.youbot-stack-utwente=\
	youbot-stack-utwente/stack.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
