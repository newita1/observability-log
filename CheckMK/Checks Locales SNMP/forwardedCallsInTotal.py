#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_bhistoryased
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plguins=nameofplugin -v"

from .agent_based_api.v1 import *

def discover_tvoice_forwardedCallsInTotal(section):
    name = "Total de llamadas entrantes desviadas"
    yield Service(item=name)

def check_stvoice_forwardedCallsInTotal(item, section):
    if item == "Total de llamadas entrantes desviadas":
        for fila in section:
            sum_value = sum(int(item) for item in fila)

        for telefonica, teams, ecx, sbcmx in section:
            if not sum_value:
                yield Result(state = State.CRIT, summary = f"No system info")
                return
            else:
                yield Metric("forwarded_totalcalls_in", int(sum_value))
                yield Metric("forwarded_totalcalls_in_telefonica", int(telefonica))
                yield Metric("forwarded_totalcalls_in_teams", int(teams))
                yield Metric("forwarded_totalcalls_in_3cx", int(ecx))
                yield Metric("forwarded_totalcalls_in_sbcmx", int(sbcmx))
                yield Result(state = State.OK,
                             details = f"Telefonica: {telefonica} - Teams: {teams} - 3CX: {ecx} - SBC_MX: {sbcmx}",
                             summary = f"Total de llamadas entrantes desviadas: {sum_value:.0f}")
                return

register.check_plugin(
    name="tvoice_sbc_forwardedCallsInTotal",
    service_name="%s",
    discovery_function = discover_tvoice_forwardedCallsInTotal,
    check_function=check_stvoice_forwardedCallsInTotal,
)

register.snmp_section(
    name = "tvoice_sbc_forwardedCallsInTotal",
    detect = exists(".1.3.6.1.4.1.5003.15.3.1.1.2.1.1.15"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.5003.15.3.1.1.2.1.1.15",
        oids=[
            "1", 
            "2",
            "3",
            "4",
],
    ),
)