# robotpkg depend.mk for:	bride-rtt-component-models
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRIDE_RTT_COMPONENT_MODELS_DEPEND_MK:= ${BRIDE_RTT_COMPONENT_MODELS_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		bride-rtt-component-models
endif

ifeq (+,$(BRIDE_RTT_COMPONENT_MODELS_DEPEND_MK))
PREFER.bride-rtt-component-models?=	robotpkg

DEPEND_USE+=		bride-rtt-component-models

DEPEND_ABI.bride-rtt-component-models?=	bride-rtt-component-models>=0.1
DEPEND_DIR.bride-rtt-component-models?=	../../rtt-component-models/bride-rtt-component-models

SYSTEM_SEARCH.bride-rtt-component-models=\
	gripper-bride-rtt-component-model/.project
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
