import sys
from threading import Thread
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
yellow=Fore.YELLOW
reset=Style.RESET_ALL

try:
    from phonyARP.modules.banner import banner
    from phonyARP.modules.cli import cli
    from phonyARP.modules.arp.spoofer import *
    
except ImportError as e:
    print(f"{bright}{blue}INFO:{reset}Could't import :{e}")
    sys.exit()
    
class Phonyhandler():

    def handler(self):
        # Function will handle the phonyARP.  
        try:
            interface=cli.args().interface
            target_ip=cli.args().target
            gateway_ip=cli.args().gateway
            
            if cli.args().help:
                print(help.help())
                exit(0)
                
            if (interface is not None) and (target_ip is not None) and (gateway_ip is not None):
                print(f"{bright}{yellow}[+] {reset}{blue}Spoofing started{reset} :{bright}{red}Target{reset} :[{target_ip}] {bright}{red}Gateway{reset} :[{gateway_ip}] {bright}{red}Interface{reset} :[{interface}]")
                target_mac=get_mac_addr(target_ip)
                gateway_mac=get_mac_addr(gateway_ip)
                if target_ip != 1 and gateway_mac != 1:
                    print(f"Target  [Ip:Mac] :{target_ip} : {target_mac}")
                    print(f"Gateway [Ip:Mac] :{gateway_ip} : {gateway_mac}")
                else:
                    exit(1)
                target_spoof_thread=Thread(target=arp_spoofer,args=(target_ip,target_mac,gateway_ip,gateway_mac,interface)).start()
                #gateway_spoof_thread=Thread(target=self.handler.arp_spoofer,args=(gateway_ip,target_ip,target_mac,self.interface)).start()
                    
                
            else:
                print(f"[{bright}{red}ERROR{reset}]: Missing required argumets.")
                print(f" Usage :{sys.argv[0]} -i <interface> -t <target> -g <gateway>\n Use --help for more information.\n")
                exit(1)
                
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")  
            
        except Exception as e:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Unexpected Exception in handler :{e}\n")
            
    def start(self):
        try:
            phonyarp_bannner=banner.banner()
            print(phonyarp_bannner)
            self.handler()
            
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")
        