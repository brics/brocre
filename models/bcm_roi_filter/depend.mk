DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
bcm_roi_filter_DEPEND_MK:= ${bcm_roi_filter_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        bcm_roi_filter
endif

ifeq (+,$(bcm_roi_filter_DEPEND_MK))
PREFER.bcm_roi_filter?=    robotpkg

DEPEND_USE+=        bcm_roi_filter

DEPEND_ABI.bcm_roi_filter?=    bcm_roi_filter>=0.1
DEPEND_DIR.bcm_roi_filter?=    ../../models/bcm_roi_filter

SYSTEM_SEARCH.bcm_roi_filter=models/models/bcm_roi_filter/model/roi_filter.bcmx
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
