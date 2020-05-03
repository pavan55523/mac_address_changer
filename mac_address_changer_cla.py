#!/usr/bin/env python


import subprocess
import optparse
import re

#To extract the options and values passed as the command line arguments and validate them
def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Please enter the interface to change MAC address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="Please enter the new MAC address")
    (options ,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("Please enter a valid interface name")
    elif not options.new_mac:
        parser.error("Please enter a valid new MAC address")
    return options

def mac_changer(interface , new_mac):
    print("[+] Changing mac address to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not read MAC address...")
        
options = get_arguments()
current_mac = get_current_mac(options.interface)
print(" Current MAC address " + str(current_mac))
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC address of " + options.interface + " changed to " + options.new_mac)
else:
    print("[-] MAC address did not change")
