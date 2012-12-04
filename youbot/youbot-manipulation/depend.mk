DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot-manipulation_DEPEND_MK:= ${youbot-manipulation_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot-manipulation
endif

ifeq (+,$(youbot-manipulation_DEPEND_MK))
PREFER.youbot-manipulation?=    robotpkg

DEPEND_USE+=        youbot-manipulation

DEPEND_ABI.youbot-manipulation?=    youbot-manipulation>=0.2
DEPEND_DIR.youbot-manipulation?=    ../../youbot/youbot-manipulation

SYSTEM_SEARCH.youbot-manipulation=youbot/youbot-manipulation/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
