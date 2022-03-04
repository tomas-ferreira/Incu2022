#!/usr/bin/env python3

from netmiko import ConnectHandler

#Author : Tomas Ferreira

#Exercise 1 of the third Cisco Automation track class

#This little script aims to get the CSR's hostname, which is hosted at DevNet Sandbox

try:
    device_connection = ConnectHandler ( #Open the connection
            device_type = "cisco_ios",
            host = "10.10.20.48",
            username = "developer",
            password = "C1sco12345",
            secret = "cisco"
    )
    print("Connected to the device!")

except:
    print("Failed to connect...")

ssh_output = device_connection.send_command("sho run | inc hostname") #Sends request to get the hostname of the CSR

print(ssh_output) #Outputs the reply from CSR

device_connection.disconnect() #Graceful disconnection
