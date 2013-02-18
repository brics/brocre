DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
brics_3d_bride_models_DEPEND_MK:= ${brics_3d_bride_models_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        brics_3d_bride_models
endif

ifeq (+,$(brics_3d_bride_models_DEPEND_MK))
PREFER.brics_3d_bride_models?=    robotpkg

DEPEND_USE+=        brics_3d_bride_models

DEPEND_ABI.brics_3d_bride_models?=    brics_3d_bride_models>=0.1.2
DEPEND_DIR.brics_3d_bride_models?=    ../../models/brics_3d_bride_models

SYSTEM_SEARCH.brics_3d_bride_models=models/brics_3d_bride_models/stack.xml
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
