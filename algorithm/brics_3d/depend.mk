DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics_3d_DEPEND_MK:= ${brics_3d_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics_3d
endif

ifeq (+,$(brics_3d_DEPEND_MK))
PREFER.brics_3d?=    robotpkg

DEPEND_USE+=        brics_3d

DEPEND_ABI.brics_3d?=    brics_3d>=0.3.2
DEPEND_DIR.brics_3d?=    ../../algorithm/brics_3d

SYSTEM_SEARCH.brics_3d=algorithm/brics_3d/manifest.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
