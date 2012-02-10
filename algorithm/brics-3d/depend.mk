DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics-3d_DEPEND_MK:= ${brics-3d_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics-3d
endif

ifeq (+,$(brics-3d_DEPEND_MK))
PREFER.brics-3d?=    robotpkg

DEPEND_USE+=        brics-3d

DEPEND_ABI.brics-3d?=    brics-3d>=0.1
DEPEND_DIR.brics-3d?=    ../../algorithm/brics-3d

SYSTEM_SEARCH.brics-3d=algorithm/brics-3d/manifest.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
