# robotpkg depend.mk for:	brics-mm
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRICS_MM_DEPEND_MK:= ${BRICS_MM_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		brics-mm
endif

ifeq (+,$(BRICS_MM_DEPEND_MK))
PREFER.brics-mm?=	robotpkg

DEPEND_USE+=		brics-mm

DEPEND_ABI.brics-mm?=	brics-mm>=0.1
DEPEND_DIR.brics-mm?=	../../algorithm/brics-mm

SYSTEM_SEARCH.brics-mm=\
	BRICS_MM/CMakeLists.txt
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
