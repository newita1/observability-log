#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#move the plugin to the folder /opt/omd/sites/nameofsite/local/lib/check_mk/base/plugins/agent_based
#chown in the script for the user site (name of site)
#execute in OMD "cmk --debug -I --detect-plugins=nameofplugin -v"
#Executi in OMD "cmk -O" for apply changes
from .agent_based_api.v1 import *


def discover_ping_rmq(section):
    for i in section:
        yield Service(item=f"Ping to {i[0]}")

def check_ping_rmq(item, section):
    for i in section:
        if str(i[0]) in str(item):
            if "error" in section:
                yield Result(state = State.CRIT, summary = f'{i[2]}')
                return
            else:
                yield Result(state = State.OK, summary = f'{i[2]} {i[3]}')
                return


register.agent_section(
    name = "Ips_ping",
)

register.check_plugin(
    name="Ips_ping",
    service_name="%s",
    discovery_function = discover_ping_rmq,
    check_function= check_ping_rmq,
)
