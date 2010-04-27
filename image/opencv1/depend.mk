#
# Copyright (c) 2008-2010 LAAS/CNRS
# All rights reserved.
#
# Redistribution  and  use in source   and binary forms,  with or without
# modification, are permitted provided that  the following conditions are
# met:
#
#   1. Redistributions  of  source code must  retain  the above copyright
#      notice and this list of conditions.
#   2. Redistributions in binary form must  reproduce the above copyright
#      notice  and this list of  conditions in the documentation   and/or
#      other materials provided with the distribution.
#
#                                       Anthony Mallet on Fri May 14 2008
#

DEPEND_DEPTH:=		${DEPEND_DEPTH}+
OPENCV1_DEPEND_MK:=	${OPENCV1_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=		opencv1
endif

ifeq (+,$(OPENCV1_DEPEND_MK)) # --------------------------------------------

PREFER.opencv1?=		robotpkg

DEPEND_USE+=		opencv1

DEPEND_ABI.opencv1?=	opencv1>=1.1pre1
DEPEND_DIR.opencv1?=	../../image/opencv1

SYSTEM_SEARCH.opencv1=\
	include/opencv/cv.h		\
	'lib/pkgconfig/opencv.pc:/Version/s/[^.0-9]//gp'

endif # OPENCV1_DEPEND_MK --------------------------------------------------

DEPEND_DEPTH:=		${DEPEND_DEPTH:+=}