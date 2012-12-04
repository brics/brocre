DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
bride_DEPEND_MK:= ${bride_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        bride
endif

ifeq (+,$(bride_DEPEND_MK))
PREFER.bride?=    robotpkg

DEPEND_USE+=        bride

DEPEND_ABI.bride?=    bride>=0.1.2
DEPEND_DIR.bride?=    ../../ide/bride

SYSTEM_SEARCH.bride=ide/bride/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
