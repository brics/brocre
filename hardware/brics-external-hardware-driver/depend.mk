# robotpkg depend.mk for:	brics-external-hardware-driver
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
BRICS_EXTERNAL_DRIVERS_DEPEND_MK:= ${BRICS_EXTERNAL_DRIVERS_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		brics-external-hardware-driver
endif

ifeq (+,$(BRICS_EXTERNAL_DRIVERS_DEPEND_MK))
PREFER.brics-external-hardware-driver?=	robotpkg

DEPEND_USE+=		brics-external-hardware-driver

DEPEND_ABI.brics-external-hardware-driver?=	brics-external-hardware-driver>=0.1
DEPEND_DIR.brics-external-hardware-driver?=	../../hardware/brics-external-hardware-driver

SYSTEM_SEARCH.brics-external-hardware-driver=\
	brics-external-hardware-driver/stack.xml
endif

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}
