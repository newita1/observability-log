#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_bhistoryased
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plguins=nameofplugin -v"

from .agent_based_api.v1 import *

def discover_tvoice_establishedCallsRateOutAvg(section):
    name = "Tasa media de llamadas salientes establecidas"
    yield Service(item=name)

def check_stvoice_establishedCallsRateOutAvg(item, section):
    suma = 0
    count = 0
    if item == "Tasa media de llamadas salientes establecidas":
        for fila in section:

            for i in fila:
                suma += int(i)
                count += 1
                result = suma / count
            if not i:
                yield Result(state = State.CRIT, summary = f"No system info")
                return
            else:
                yield Metric("established_ratecalls_out_avg", int(result))
                yield Metric("established_ratecalls_out_avg_telefonica", int(fila[0]))
                yield Metric("established_ratecalls_out_avg_teams", int(fila[1]))
                yield Metric("established_ratecalls_out_avg_3cx", int(fila[2]))
                yield Metric("established_ratecalls_out_avg_sbcmx", int(fila[3]))
                yield Result(state = State.OK,
                                details = f"Telefonica: {fila[0]} - Teams: {fila[1]} - 3CX: {fila[2]} - SBC_MX: {fila[3]}",
                                summary = f"Tasa media de llamadas salientes establecidas: {result:.0f}")
                return

register.check_plugin(
    name="tvoice_sbc_establishedCallsRateOutAvg",
    service_name="%s",
    discovery_function = discover_tvoice_establishedCallsRateOutAvg,
    check_function=check_stvoice_establishedCallsRateOutAvg,
)

register.snmp_section(
    name = "tvoice_sbc_establishedCallsRateOutAvg",
    detect = exists(".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.18"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.5003.15.3.1.2.2.1.1.18",
        oids=[
            "1",
            "2",
            "3",
            "4",
],
    ),
)
