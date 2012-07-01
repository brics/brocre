DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
artoolkitplusstack_DEPEND_MK:= ${artoolkitplusstack_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        artoolkitplusstack
endif

ifeq (+,$(artoolkitplusstack_DEPEND_MK))
PREFER.artoolkitplusstack?=    robotpkg

DEPEND_USE+=        artoolkitplusstack

DEPEND_ABI.artoolkitplusstack?=    artoolkitplusstack>=1
DEPEND_DIR.artoolkitplusstack?=    ../../algorithm/artoolkitplusstack

SYSTEM_SEARCH.artoolkitplusstack=algorithm/artoolkitplusstack/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
