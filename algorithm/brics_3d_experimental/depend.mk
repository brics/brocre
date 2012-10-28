DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics_3d_experimental_DEPEND_MK:= ${brics_3d_experimental_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics_3d_experimental
endif

ifeq (+,$(brics_3d_experimental_DEPEND_MK))
PREFER.brics_3d_experimental?=    robotpkg

DEPEND_USE+=        brics_3d_experimental

DEPEND_ABI.brics_3d_experimental?=    brics_3d_experimental>=0.1
DEPEND_DIR.brics_3d_experimental?=    ../../algorithm/brics_3d_experimental

SYSTEM_SEARCH.brics_3d_experimental=algorithm/brics_3d_experimental/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
