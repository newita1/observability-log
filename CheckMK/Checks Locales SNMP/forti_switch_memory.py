#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/master/local/lib/check_mk/base/plugins/agent_based
#chown in the script for the user site (name of site)
#execute in OMD "cmk -vvI --detect-plugin=nombreplugin host" > cmk -O

from .agent_based_api.v1 import *
import pprint
import re

def discover_fortiswitch_memory(section):
    yield Service(item="Memory used")

def check_fortiswitch_memory(item, section):
    for i in section:
        if item == "Memory used":
            yield Metric("mem_used", int(i[0]))
            used_memory = int(i[0])
            total_memory = int(i[1])
            memory_percentage = int((used_memory / total_memory) * 100)
            if memory_percentage >= 90:
                yield Result(state = State.CRIT, summary = f"Memory used - {memory_percentage:.2f}%")
                return
            elif memory_percentage >= 85:
                yield Result(state = State.WARN, summary = f"Memory used - {memory_percentage:.2f}%")
                return
            else:
                yield Result(state = State.OK, summary = f"Memory used - {memory_percentage:.2f}%")
                return

register.check_plugin(
    name="fortiswitch_memory",
    service_name="%s",
    discovery_function = discover_fortiswitch_memory,
    check_function= check_fortiswitch_memory,
)

register.snmp_section(
    name = "fortiswitch_memory",
    detect = exists(".1.3.6.1.4.1.12356.106.4.1.3"),
    fetch = SNMPTree(
        base=".1.3.6.1.4.1.12356.106.4.1",
        oids=[
            "3.0",
            "4.0"],
    ),
)

