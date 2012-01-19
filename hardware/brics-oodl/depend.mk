# robotpkg depend.mk for:	brics-oodl
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRICS_OODL_DEPEND_MK:= ${BRICS_OODL_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		brics-oodl
endif

ifeq (+,$(BRICS_OODL_DEPEND_MK))
PREFER.brics-oodl?=	robotpkg

DEPEND_USE+=		brics-oodl

DEPEND_ABI.brics-oodl?=	brics-oodl>=0.9
DEPEND_DIR.brics-oodl?=	../../hardware/brics-oodl

SYSTEM_SEARCH.brics-oodl=\
	BRICS_OODL/stack.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
