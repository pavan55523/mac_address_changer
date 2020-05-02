#!/usr/bin/env python


import subprocess
import optparse

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
    print("[+] MAC address of " + interface + " changed to " + new_mac)

options = get_arguments()
mac_changer(options.interface , options.new_mac)