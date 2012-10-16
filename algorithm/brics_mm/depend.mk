DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics_mm_DEPEND_MK:= ${brics_mm_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics_mm
endif

ifeq (+,$(brics_mm_DEPEND_MK))
PREFER.brics_mm?=    robotpkg

DEPEND_USE+=        brics_mm

DEPEND_ABI.brics_mm?=    brics_mm>=0.1
DEPEND_DIR.brics_mm?=    ../../algorithm/brics_mm

SYSTEM_SEARCH.brics_mm=algorithm/brics_mm/CMakeLists.txt
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
