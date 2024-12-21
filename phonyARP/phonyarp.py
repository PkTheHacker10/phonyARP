import sys
from threading import Thread,Event
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
yellow=Fore.YELLOW
green=Fore.GREEN
reset=Style.RESET_ALL

stop_event=Event()

try:
    from phonyARP.modules.banner import banner
    from phonyARP.modules.cli import cli
    from phonyARP.modules.arp.spoofer import *
    
except ImportError as e:
    print(f"{bright}{blue}INFO:{reset}Could't import :{e}")
    sys.exit()
    
except KeyboardInterrupt:
    print(f"{bright}{white}\n[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting before start :(")
    
class Phonyhandler():
    # Class which handle the phonyARP spoofing.
    def handler(self):
        # Handler funtion for phony ARP.  
        try:
            interface=cli.args().interface
            target_ip=cli.args().target
            gateway_ip=cli.args().gateway
            
            if cli.args().help:
                print(cli.help())
                exit()
                
            if (interface is not None) and (target_ip is not None) and (gateway_ip is not None):
                try:
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Spoofing started{reset} {blue}({reset} {bright}{red}Target{reset} :[{target_ip}] {bright}{red}Gateway{reset} :[{gateway_ip}] {bright}{red}Interface{reset} :[{interface}] {blue}){reset}")
                    print(f"{bright}{yellow} [+] {reset}{blue}MAC resolution {green}{bright}started{reset}")
                    target_mac=get_mac_addr(target_ip)
                    gateway_mac=get_mac_addr(gateway_ip)
                    
                    if target_ip==1 and gateway_mac==1 :
                        # Check the given ip is reachable or not.
                        print(f"{bright}{yellow} [+] {reset}{blue}MAC resolution {bright}{red}Failed{reset} \n{bright}{yellow} [+]{reset} {blue}Check the ip is correct or not.\n{reset}")
                        exit(1)
                    else:                      
                        print(f"{bright}{yellow} [+] {reset}{blue}Target spoof {bright}status:{green}running{reset}")
                        target_spoof_thread=Thread(target=arp_spoofer,args=(target_ip,target_mac,gateway_ip,interface))
                    
                        print(f"{bright}{yellow} [+] {reset}{blue}Gateway spoof {bright}status:{green}running{reset}")
                        gateway_spoof_thread=Thread(target=arp_spoofer,args=(gateway_ip,gateway_mac,target_ip,interface))
                        
                        target_spoof_thread.start()
                        gateway_spoof_thread.start()
                        
                        target_spoof_thread.join()
                        gateway_spoof_thread.join()

                        
                except KeyboardInterrupt:
                    # Ro signal threads to stop.
                    stop_event.set()  
                    target_spoof_thread.join()
                    gateway_spoof_thread.join()
                    
                    # Restore from Arp poisoning.
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Quiting....")
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Arp Spoof Restoring {reset}{bright}{green}Started")
                    spoof_restorer(target_ip,target_mac,gateway_ip,gateway_mac,interface)
                
            else:
                print(f"[{bright}{red}ERROR{reset}]: Missing required argumets.")
                print(f" Usage :{sys.argv[0]} -i <interface> -t <target> -g <gateway>\n Use --help for more information.\n")
                exit(1)
                
        except KeyboardInterrupt:
            print(f"{bright}{white}\n[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n") 
            
        except NameError:
            # To prevent from quick exit.
            pass    
        
        except Exception as e:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Unexpected Handler Error :{e}\n")

            
    def start(self):
        try:
            phonyarp_bannner=banner.banner()
            print(phonyarp_bannner)
            self.handler()
            
        except NameError:
            # To prevent from quick exit.
            pass
        
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")
        