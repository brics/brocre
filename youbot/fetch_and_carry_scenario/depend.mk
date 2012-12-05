DEPEND_DEPTH:=        ${DEPEND_DEPTH}+
fetch_and_carry_scenario_DEPEND_MK:= ${fetch_and_carry_scenario_DEPEND_MK}+

ifeq (+,$(DEPEND_DEPTH))
DEPEND_PKG+=        fetch_and_carry_scenario
endif

ifeq (+,$(fetch_and_carry_scenario_DEPEND_MK))
PREFER.fetch_and_carry_scenario?=    robotpkg

DEPEND_USE+=        fetch_and_carry_scenario

DEPEND_ABI.fetch_and_carry_scenario?=    fetch_and_carry_scenario>=0.1
DEPEND_DIR.fetch_and_carry_scenario?=    ../../youbot/fetch_and_carry_scenario

SYSTEM_SEARCH.fetch_and_carry_scenario=youbot/fetch_and_carry_scenario/README.md
endif

DEPEND_DEPTH:=        ${DEPEND_DEPTH:+=}
