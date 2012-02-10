DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics-mm_DEPEND_MK:= ${brics-mm_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics-mm
endif

ifeq (+,$(brics-mm_DEPEND_MK))
PREFER.brics-mm?=    robotpkg

DEPEND_USE+=        brics-mm

DEPEND_ABI.brics-mm?=    brics-mm>=0.1
DEPEND_DIR.brics-mm?=    ../../algorithm/brics-mm

SYSTEM_SEARCH.brics-mm=algorithm/brics_mm/CMakeLists.txt
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
