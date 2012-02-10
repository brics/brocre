DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics-oodl_DEPEND_MK:= ${brics-oodl_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics-oodl
endif

ifeq (+,$(brics-oodl_DEPEND_MK))
PREFER.brics-oodl?=    robotpkg

DEPEND_USE+=        brics-oodl

DEPEND_ABI.brics-oodl?=    brics-oodl>=0.1
DEPEND_DIR.brics-oodl?=    ../../hardware/brics-oodl

SYSTEM_SEARCH.brics-oodl=hardware/brics-oodl/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
