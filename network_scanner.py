#!/usr/bin/env python

import scapy.all as scapy
import argparse

#To scan the network and return all the clients connected
def scan(ip):
    #scapy.ls(scapy.ARP())
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #Creating arp request packet
    arp_packet = arp_broadcast/arp_request
    #sending and recieving response of the packet
    #srp returns two lists of answered packets response and unanswered
    answered_list,unanswered_list = scapy.srp(arp_packet, timeout=1, verbose=False)
    clients_list = []
    for elements in answered_list:
        #.psrc is the ip address of each element and hwsrc is macc address
        client_dict = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

#To print the ip and mac address of the clients
def print_result(result_list):
    print("IP\t\tMAC ADDRESS\n------------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

#to extract the comandline arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Specify TargetIP/IP range")
    options = parser.parse_args()
    return options

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
