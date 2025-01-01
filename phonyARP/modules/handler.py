import os
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
    
    from phonyARP.modules.cli import cli
    from phonyARP.modules.spoofer.arp.spoofer import *
    from phonyARP.modules.spoofer.ping_sweep.sweeper import sweeper
    
except ImportError as e:
    print(f"{bright}{yellow} [+] {reset}{blue}Could't import :{e}")
    exit(1)
    
except KeyboardInterrupt:
    print(f"{bright}{white}\n[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting before start :(")
    
class Phonyhandler():
    # Class which handle the phonyARP spoofing.
    def handler(self):
        # Handler funtion for phony ARP.  
        try:
            arguments=cli.args()
            interface=arguments.interface
            target_ip=arguments.target
            gateway_ip=arguments.gateway

            if cli.args().help:
                print(cli.help())
                exit()
                
            if cli.args().version:
                version=cli.get_version()
                print(f"""
    phonyARP is a arp spoofing tool which is created by {bright}{green}PkTheHacker10{reset}. \nWhich is currently runing on the version ( {green}{version}{reset} ) .
                      """)
                exit()    
                
            if arguments.scan_network:
                print(f"{bright}{yellow}\n [+] {reset}{blue}Network scanning started.{reset}")
                ip_list=sweeper()
                print(f"\n{bright}{yellow} [+] {reset}{blue}Active hosts:{reset}")
                for active_ip in ip_list:
                    print(f"{green}{bright}  =>{reset}   {active_ip}")
                exit()
                              
            if os.getuid() !=0:
                print(f"{bright}{yellow} [+] {reset}{bright}{red}Permission error Operation not permitted.{reset}\n{blue}     Run it from superuser privilege.{reset}")
                exit(1)          
                  
            if (interface is not None) and (target_ip is not None) and (gateway_ip is not None):
                try:
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Spoofing started{reset} {blue}({reset} {bright}{red}Target{reset} :[{target_ip}] {bright}{red}Gateway{reset} :[{gateway_ip}] {bright}{red}Interface{reset} :[{interface}] {blue}){reset}")
                    print(f"{bright}{yellow} [+] {reset}{blue}MAC resolution {green}{bright}started{reset}")
                    
                    # MAC resolution from ip.
                    target_mac=get_mac_addr(target_ip)              
                    gateway_mac=get_mac_addr(gateway_ip)
                    
                    if target_ip is None and gateway_mac is None:
                        # Check the given IP is reachable or not.
                        print(f"{bright}{yellow} [+] {reset}{blue}MAC resolution {bright}{red}Failed{reset} \n{bright}{yellow} [+]{reset} {blue}Check the ip is correct or not.\n{reset}")
                        exit(1)
                    else:
                        # Spoofing threads initalization.                  
                        print(f"{bright}{yellow} [+] {reset}{blue}Target spoof {bright}status:{green}running{reset}")
                        target_spoof_thread=Thread(target=arp_spoofer,args=(target_ip,target_mac,gateway_ip,interface))
                    
                        print(f"{bright}{yellow} [+] {reset}{blue}Gateway spoof {bright}status:{green}running{reset}")
                        gateway_spoof_thread=Thread(target=arp_spoofer,args=(gateway_ip,gateway_mac,target_ip,interface))
                        
                        # Spoofing threads started.
                        target_spoof_thread.start()
                        gateway_spoof_thread.start()
                        
                        # waiting for the tspoofing thread to end.
                        target_spoof_thread.join()
                        gateway_spoof_thread.join()
                        
                except KeyboardInterrupt:
                    # To signal threads to stop.
                    stop_event.set()  
                    target_spoof_thread.join()
                    gateway_spoof_thread.join()
                    
                    # Restore from Arp poisoning.
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Quiting....")
                    print(f"{bright}{yellow}\n [+] {reset}{blue}Arp Spoof Restoring {reset}{bright}{green}Started")
                    spoof_restorer(target_ip,target_mac,gateway_ip,gateway_mac,interface)

            else:
                print(f"{bright}{red} [ ERROR ]{reset}: Missing required argumets.")
                print(f" {bright}{blue} Usage :{sys.argv[0]} {reset}-i {red}<interface>{reset} -t {red}<target>{reset} -g {red}<gateway>{reset}\n {blue}Use --help for more information.{reset}\n")
                exit(1)
                
        except KeyboardInterrupt:
            print(f"{bright}{yellow} [+] {reset}{red}: Quiting...\n") 
            
        except NameError:
            # To prevent from quick exit.
            pass    
        
        except Exception as e:
            print(f"{bright}{yellow} [+] {reset}{red}: Unexpected Handler Error :{e}\n")

            
    def start(self):
        # Starter funtion
        try:
            self.handler()
            
        except NameError:
            # To prevent from quick exit.
            pass
        
        except KeyboardInterrupt:
            print(f"{bright}{yellow} [+] {reset}{blue}: Quiting...\n")
        
if __name__ =="__main__":
    test=Phonyhandler()
    test.start()