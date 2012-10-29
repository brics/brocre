DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
b-it-bots_youbot-manipulation_DEPEND_MK:= ${b-it-bots_youbot-manipulation_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        b-it-bots_youbot-manipulation
endif

ifeq (+,$(b-it-bots_youbot-manipulation_DEPEND_MK))
PREFER.b-it-bots_youbot-manipulation?=    robotpkg

DEPEND_USE+=        b-it-bots_youbot-manipulation

DEPEND_ABI.b-it-bots_youbot-manipulation?=    b-it-bots_youbot-manipulation>=0.2
DEPEND_DIR.b-it-bots_youbot-manipulation?=    ../../youbot/b-it-bots_youbot-manipulation

SYSTEM_SEARCH.b-it-bots_youbot-manipulation=youbot/b-it-bots_youbot-manipulation/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
