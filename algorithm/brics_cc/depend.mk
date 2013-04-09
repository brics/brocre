DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics_cc_DEPEND_MK:= ${brics_cc_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics_cc
endif

ifeq (+,$(brics_cc_DEPEND_MK))
PREFER.brics_cc?=    robotpkg

DEPEND_USE+=        brics_cc

DEPEND_ABI.brics_cc?=    brics_cc>=1.0
DEPEND_DIR.brics_cc?=    ../../algorithm/brics_cc

SYSTEM_SEARCH.brics_cc=algorithm/brics_cc/manifest.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
