#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_bhistoryased
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plguins=nameofplugin -v"

from .agent_based_api.v1 import *

def discover_tvoice_activecallsin(section):
    name = "Total de llamadas entrantes Activas"
    yield Service(item=name)

def check_stvoice_activecallsin(item, section):
    for i in section:
        if item == "Total de llamadas entrantes Activas":
            if not i:
                yield Result(state = State.CRIT, summary = f"No system info")
                return
            else:
                yield Result(state = State.OK, summary = f"Total de llamadas entrantes Activas: {i[0]}")
                yield Metric("total_activecalls_in", int(i[0]))
                return

register.check_plugin(
    name="tvoice_sbc_activecallsin",
    service_name="%s",
    discovery_function = discover_tvoice_activecallsin,
    check_function=check_stvoice_activecallsin,
)

register.snmp_section(
    name = "tvoice_sbc_activecallsin",
    detect = exists(".1.3.6.1.4.1.5003.15.3.1.1.2.2.1.3"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.5003.15.3.1.1.2.2.1.3",
        oids=[
            "0", 
],
    ),  
)