DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics-external-packages-ros_DEPEND_MK:= ${brics-external-packages-ros_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics-external-packages-ros
endif

ifeq (+,$(brics-external-packages-ros_DEPEND_MK))
PREFER.brics-external-packages-ros?=    robotpkg

DEPEND_USE+=        brics-external-packages-ros

DEPEND_ABI.brics-external-packages-ros?=    brics-external-packages-ros>=0.1
DEPEND_DIR.brics-external-packages-ros?=    ../../hardware/brics-external-packages-ros

SYSTEM_SEARCH.brics-external-packages-ros=hardware/brics-external-packages-ros/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
