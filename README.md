# mac_address_changer
This mac_address_changer repository is a python script that changes the MAC address of the device. escpecially for linux based systems.

HOW TO USE:
>cd mac_address_changer
>python3 mac_address_changer.py
>give the required input to the program.
  
# mac_address_changer_cla
This mac_address_changer_cla is a python script that is used to change the MAC address of the computer escpecially for linux based systems.
To this program we are supposed to provide the command line arguments

HOW TO USE:
>cd mac_address_changer_cla
>python3 mac_address_changer_cla.py -i (interface_name) -m (new_mac_address)
                    OR
>python3 mac_address_changer_cla.py --interface (interface_name) --new_mac (new_mac_address)

______________________________________________________________________________________________

# network_scanner
This is a python script that scans the given ip address range specified by the user and returns the IP ADDRESS and MAC ADDRESS using ARP.

The algorithm we used in this network scanner implementation has 4 main steps
1)Create a ARP request packet and broadcast it to the gateway MAC address
2)Send and Recieve the packet response
3)Analyse the response
4)Print the result

HOW TO USE THIS SCRIPT:
>python network_scanner.py -t target_IP_range
              OR
>python network_scanner.py --target target_IP_range

SAMPLE EXAMPLE:
>python network_scanner.py -t 192.169.187.1/24

________________________________________________________________________________________

# arp-spoof-detector
This python script when run in a machine, tells the user whether that machine is under ARP spoofing attack or not.

# Process it follows
1) It gets the MAC address of the owner machine as real_mac.
2) It then checks in the network whether any other machines have same IP address and if yes it gets the MAC address of that machine as response_mac.
3) If real_mac equals to response_mac then it is his own machine so no attack.
  else other machine with different MAC address has spoofed the owners IP.
  
