DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
hbrs-ros-pkg_DEPEND_MK:= ${hbrs-ros-pkg_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        hbrs-ros-pkg
endif

ifeq (+,$(hbrs-ros-pkg_DEPEND_MK))
PREFER.hbrs-ros-pkg?=    robotpkg

DEPEND_USE+=        hbrs-ros-pkg

DEPEND_ABI.hbrs-ros-pkg?=    hbrs-ros-pkg>=0.2
DEPEND_DIR.hbrs-ros-pkg?=    ../../algorithm/hbrs-ros-pkg

SYSTEM_SEARCH.hbrs-ros-pkg=algorithm/hbrs-ros-pkg/repository.rosinstall
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
