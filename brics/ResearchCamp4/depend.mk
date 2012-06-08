DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
ResearchCamp4_DEPEND_MK:= ${ResearchCamp4_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        ResearchCamp4
endif

ifeq (+,$(ResearchCamp4_DEPEND_MK))
PREFER.ResearchCamp4?=    robotpkg

DEPEND_USE+=        ResearchCamp4

DEPEND_ABI.ResearchCamp4?=    ResearchCamp4>=0.9
DEPEND_DIR.ResearchCamp4?=    ../../brics/ResearchCamp4

SYSTEM_SEARCH.ResearchCamp4=brics/ResearchCamp4/raw_scenarios/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
