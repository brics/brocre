DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
b-it-bots_youbot-ros-pkg_DEPEND_MK:= ${b-it-bots_youbot-ros-pkg_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        b-it-bots_youbot-ros-pkg
endif

ifeq (+,$(b-it-bots_youbot-ros-pkg_DEPEND_MK))
PREFER.b-it-bots_youbot-ros-pkg?=    robotpkg

DEPEND_USE+=        b-it-bots_youbot-ros-pkg

DEPEND_ABI.b-it-bots_youbot-ros-pkg?=    b-it-bots_youbot-ros-pkg>=0.1
DEPEND_DIR.b-it-bots_youbot-ros-pkg?=    ../../youbot/b-it-bots_youbot-ros-pkg

SYSTEM_SEARCH.b-it-bots_youbot-ros-pkg=youbot/youbot-ros-pkg/youbot_common/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
