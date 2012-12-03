DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot_applications_DEPEND_MK:= ${youbot_applications_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot_applications
endif

ifeq (+,$(youbot_applications_DEPEND_MK))
PREFER.youbot_applications?=    robotpkg

DEPEND_USE+=        youbot_applications

DEPEND_ABI.youbot_applications?=    youbot_applications>=0.2
DEPEND_DIR.youbot_applications?=    ../../youbot/youbot_applications

SYSTEM_SEARCH.youbot_applications=youbot/youbot_applications/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
