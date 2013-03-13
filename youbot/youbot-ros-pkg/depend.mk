DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
youbot-ros-pkg_DEPEND_MK:= ${youbot-ros-pkg_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        youbot-ros-pkg
endif

ifeq (+,$(youbot-ros-pkg_DEPEND_MK))
PREFER.youbot-ros-pkg?=    robotpkg

DEPEND_USE+=        youbot-ros-pkg

DEPEND_ABI.youbot-ros-pkg?=    youbot-ros-pkg>=0.2c
DEPEND_DIR.youbot-ros-pkg?=    ../../youbot/youbot-ros-pkg

SYSTEM_SEARCH.youbot-ros-pkg=youbot/youbot-ros-pkg/README.md
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
