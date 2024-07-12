#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_bhistoryased
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plguins=nameofplugin -v"

from .agent_based_api.v1 import *

def discover_tvoice_activeCallsOutMax(section):
    name = "Max de llamadas salientes Activas"
    yield Service(item=name)

def check_stvoice_activeCallsOutMax(item, section):


    if item == "Max de llamadas salientes Activas":
        max_value = 0
        for fila in section:
            
            max_value = max(int(item[0]) for item in section)


            if not max_value:
                yield Result(state = State.CRIT, summary = f"No system info")
                return
            else:
                yield Metric("max_activecalls_out", int(max_value))
                yield Metric("max_activecalls_out_telefonica", int(fila[0]))
                yield Metric("max_activecalls_out_teams", int(fila[1]))
                yield Metric("max_activecalls_out_3cx", int(fila[2]))
                yield Metric("max_activecalls_out_sbcmx", int(fila[3]))

                yield Result(state = State.OK,
                             details = f"Telefonica: {fila[0]} - Teams: {fila[1]} - 3CX: {fila[2]} - SBC_MX: {fila[3]}",
                             summary = f"Maximo de llamadas salientes Activas: {int(max_value)}")
                return

register.check_plugin(
    name="tvoice_sbc_activeCallsOutMax",
    service_name="%s",
    discovery_function = discover_tvoice_activeCallsOutMax,
    check_function=check_stvoice_activeCallsOutMax,
)

register.snmp_section(
    name = "tvoice_sbc_activeCallsOutMax",
    detect = exists(".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.7"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.7",
        oids=[
            "1",
            "2",
            "3",
            "4",
],
    ),
)
