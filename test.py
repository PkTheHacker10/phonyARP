from scapy.all import ARP, Ether, srp

def arp_discovery(ip):
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(pkt, timeout=1, verbose=0)[0]
    if result:
        print(f"{ip} is alive")
    else:
        print(f"{ip} is not responding")

arp_discovery("192.168.1.10")
