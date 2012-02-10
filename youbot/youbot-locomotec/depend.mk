DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot-locomotec_DEPEND_MK:= ${youbot-locomotec_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot-locomotec
endif

ifeq (+,$(youbot-locomotec_DEPEND_MK))
PREFER.youbot-locomotec?=    robotpkg

DEPEND_USE+=        youbot-locomotec

DEPEND_ABI.youbot-locomotec?=    youbot-locomotec>=0.1
DEPEND_DIR.youbot-locomotec?=    ../../youbot/youbot-locomotec

SYSTEM_SEARCH.youbot-locomotec=youbot/youbot-ros-pkg/youbot_common/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
