#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/master/local/lib/check_mk/base/plugins/agent_based
#chown in the script for the user site (name of site)
#execute in OMD "cmk -vvI --detect-plugin=nombreplugin host" > cmk -O

from .agent_based_api.v1 import *

def discover_syscpu_usage(section):
    name = "CPU Usage"
    yield Service(item=name)

def check_syscpu_usage(item, section):
    for i in section:
        if item == "CPU Usage":
            yield Metric("cpu_used", int(i[0]))
            if int(i[0]) >= 90:
                yield Result(state = State.CRIT, summary = f"CPU Usage: {float(i[0]):.2f}%")
            elif int(i[0]) >= 80:
                yield Result(state = State.WARN, summary = f"CPU Usage: {float(i[0]):.2f}%")
            else:
                yield Result(state = State.OK, summary = f"CPU Usage: {float(i[0]):.2f}%")
        return

register.check_plugin(
    name="fortiswitch_syscpu_usage",
    service_name="%s",
    discovery_function = discover_syscpu_usage,
    check_function=check_syscpu_usage,
)

register.snmp_section(
    name = "fortiswitch_syscpu_usage",
    detect = exists(".1.3.6.1.4.1.12356.106.4.1.2"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.12356.106.4.1.2",
        oids=[
            "0", 
],
    ),
)                                                                    

                                                                     
                                                                     
                                                                     
