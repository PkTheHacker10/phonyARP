import sys
from threading import Thread
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    from phonyARP.modules.banner import banner
    from phonyARP.modules.cli import cli
    from phonyARP.modules.help import help
    from phonyARP.modules.version import version
    from phonyARP.modules.file import file
    from phonyARP.modules.arp.spoofer import ArpSpoofer
    
except ImportError as e:
    print(f"{bright}{blue}INFO:{reset}Could't import :{e}")
    sys.exit()
    
class Phonyhandler():
    
    def __init__(self):
        self.toolbanner=banner.banner()
        self.args=cli.args()
        self.help=help.help()
        self.version=version.get_version()
        self.file_handler=file.FileHandler()
        self.spoofer_handler=ArpSpoofer()
        
    def handler(self):
        # Function will handle the phonyARP.  
        try: 
            interface=self.args.interface
            target_ip=self.args.target
            gateway_ip=self.args.gateway
            is_help=self.args.help
            
            if is_help:
                print(self.help)
                exit()
                
            if (interface is not None) and (target_ip is not None) and (gateway_ip is not None):
                self.toolbanner
                print("spoofing started..")
                target_mac=self.spoofer_handler.get_mac_addr(target_ip)
                gateway_mac=self.spoofer_handler.get_mac_addr(gateway_ip)
                target_spoof_thread=Thread(target=self.spoofer_handler.arp_spoofer,args=(target_ip,target_ip,target_mac,interface)).start()
                #gateway_spoof_thread=Thread(target=self.handler.arp_spoofer,args=(gateway_ip,target_ip,target_mac,self.interface)).start()
                    
                
            else:
                print(self.toolbanner)
                print(f"[{bright}{red}ERROR{reset}]: Missing required argumets.")
                print(f" Usage :{sys.argv[0]} -i <interface> -t <target> -g <gateway>\n Use --help for more information.")
                exit(1)
                
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")  
            
        except Exception as e:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Unexpected Exception in handler :{e}\n")
            
    def start(self):
        try:
            self.handler()
            
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")
        