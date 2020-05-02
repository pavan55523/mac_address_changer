#!/usr/bin/env python

import subprocess

#To execute the system specific commands
interface=input("Enter the interface to change mac address > ")
new_mac=input("Enter the new mac address > ")

print("[+] Changing mac address to "+ new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] MAC address of "+interface+" changed to "+new_mac)
