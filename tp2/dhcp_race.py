from scapy.all import dhcpd

ip_pool = [f"10.1.10.{i}" for i in range(250, 253)]

dhcp_server = dhcpd(iface='eth0', pool=ip_pool, network='10.1.10.0/24', gw='10.1.10.254', lease_time=3600)

dhcp_server()
