# robotpkg depend.mk for:	brics-3d
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRICS_3d_DEPEND_MK:= ${BRICS_3d_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		brics-3d
endif

ifeq (+,$(BRICS_3d_DEPEND_MK))
PREFER.brics-3d?=	robotpkg

DEPEND_USE+=		brics-3d

DEPEND_ABI.brics-3d?=	brics-3d>=0.9
DEPEND_DIR.brics-3d?=	../../algorithm/brics-3d

SYSTEM_SEARCH.brics-3d=\
	BRICS_3d/CMakeLists.txt
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
