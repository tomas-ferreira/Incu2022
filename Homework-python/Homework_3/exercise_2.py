#!/usr/bin/env python3

import ncclient.manager
from ncclient.operations import TimeoutExpiredError
import xml.dom.minidom

#Author : Tomas Ferreira

#Exercise 2 of the third Cisco Automation track class

#This little script aims to configure a feature of CSR router - the creation of a VLAN

try:
    device_connection = ncclient.manager.connect(
        host = '10.10.20.48',
        username = 'developer',
        password = 'C1sco12345',
        port = '830',
        device_params = {'name':"csr"}
        )
    print("Connected to the device!")
except:
    print("Failure...")
       

update_interface_config_string = '''
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet1</name>
                <description>New description</description>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>10.0.0.14</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
</config>
'''

device_connection.edit_config(target='running', config=update_interface_config_string)
