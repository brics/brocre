# robotpkg depend.mk for:	brics-interfaces
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRICS_INTERFACES_DEPEND_MK:= ${BRICS_INTERFACES_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		brics-interfaces
endif

ifeq (+,$(BRICS_INTERFACES_DEPEND_MK))
PREFER.brics-interfaces?=	robotpkg

DEPEND_USE+=		brics-interfaces

DEPEND_ABI.brics-interfaces?=	brics-interfaces>=0.1
DEPEND_DIR.brics-interfaces?=	../../interfaces/brics-interfaces

SYSTEM_SEARCH.brics-interfaces=\
	interfaces/brics-interfaces/brics_actuator/manifest.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
