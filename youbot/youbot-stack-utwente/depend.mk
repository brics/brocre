DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot-stack-utwente_DEPEND_MK:= ${youbot-stack-utwente_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot-stack-utwente
endif

ifeq (+,$(youbot-stack-utwente_DEPEND_MK))
PREFER.youbot-stack-utwente?=    robotpkg

DEPEND_USE+=        youbot-stack-utwente

DEPEND_ABI.youbot-stack-utwente?=    youbot-stack-utwente>=0.1
DEPEND_DIR.youbot-stack-utwente?=    ../../youbot/youbot-stack-utwente

SYSTEM_SEARCH.youbot-stack-utwente=youbot/youbot-stack-utwente/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
