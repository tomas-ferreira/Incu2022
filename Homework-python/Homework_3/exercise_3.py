#!/usr/bin/env python3

import requests

#Author : Tomas Ferreira

#Exercise 3 of the third Cisco Automation track class

#This script aims to verify the configuration of Exercise 2's feature using RESTCONF

url = "https://10.10.20.48:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1/"

headers = {'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'} 

response = requests.get(url, auth=('developer', 'C1sco12345'), headers=headers, verify=False)

print(response.text)
