DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot_driver_DEPEND_MK:= ${youbot_driver_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot_driver
endif

ifeq (+,$(youbot_driver_DEPEND_MK))
PREFER.youbot_driver?=    robotpkg

DEPEND_USE+=        youbot_driver

DEPEND_ABI.youbot_driver?=    youbot_driver>=0.95
DEPEND_DIR.youbot_driver?=    ../../hardware/youbot_driver

SYSTEM_SEARCH.youbot_driver=hardware/youbot_driver/manifest.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
