# https://thepacketgeek.com/scapy/building-network-tools/part-06/
from scapy.all import *

flag = 'UAH{it5_imp0ssibl3_T0_g3t_A_repLy!}'
pcap = "dist/ping.pcap"

def do_stego(url):
    print(f"there should be {len(flag)+1} packets")
    waits = [ord(x) for x in list(flag)]
    print(waits)
    pkts = []
    p = IP(dst=url)/ICMP()
    p.time = 0
    pkts.append(p)
    for t in waits:
        p = IP(dst=url)/ICMP()
        p.time = t
        pkts.append(p)
    wrpcap(pcap,pkts)

do_stego("www.uah.edu")