#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_bhistoryased
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plguins=nameofplugin -v"

from .agent_based_api.v1 import *

def discover_tvoice_establishedCallsRateOutMax(section):
    name = "Tasa maxima de llamadas salientes establecidas"
    yield Service(item=name)

def check_stvoice_establishedCallsRateOutMax(item, section):
    if item == "Tasa maxima de llamadas salientes establecidas":

        for fila in section:

            for i in fila:
                max_value = max(int(item[0]) for item in section)
            if not i:
                yield Result(state = State.CRIT, summary = f"No system info")
                return
            else:
                yield Metric("established_ratecalls_out_max", int(max_value))
                yield Metric("established_ratecalls_out_max_telefonica", int(fila[0]))
                yield Metric("established_ratecalls_out_max_teams", int(fila[1]))
                yield Metric("established_ratecalls_out_max_3cx", int(fila[2]))
                yield Metric("established_ratecalls_out_max_sbcmx", int(fila[3]))
                yield Result(state = State.OK,
                                details = f"Telefonica: {fila[0]} - Teams: {fila[1]} - 3CX: {fila[2]} - SBC_MX: {fila[3]}",
                                summary = f"Tasa maxima de llamadas salientes establecidas: {max_value:.0f}")
                return

register.check_plugin(
    name="tvoice_sbc_establishedCallsRateOutMax",
    service_name="%s",
    discovery_function = discover_tvoice_establishedCallsRateOutMax,
    check_function=check_stvoice_establishedCallsRateOutMax,
)

register.snmp_section(
    name = "tvoice_sbc_establishedCallsRateOutMax",
    detect = exists(".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.19"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.19",
        oids=[
            "1",
            "2",
            "3",
            "4",
],
    ),
)
