import os
from colorama import Fore,Style
from phonyARP.modules.handler import Phonyhandler

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
yellow=Fore.YELLOW
reset=Style.RESET_ALL

try:
    from phonyARP.modules.banner import banner
    
except ImportError as e:
    print(f"{bright}{blue}INFO:{reset}Could't import :{e}")
    exit(1)
    
def main():
    #Function will call phonyhandler.
    phonyarp_bannner=banner.banner()
    print(phonyarp_bannner)
    
    if os.getuid() !=0:
       print(f"{bright}{yellow}\n [+] {reset}{bright}{red}Permission error Operation not permitted.{reset}\n{blue}     Run it from superuser privilege.{reset}")
       exit(1)
       
    else: 
        try:
            phonyhandler=Phonyhandler()
            phonyhandler.start()
            
        except KeyboardInterrupt:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")
    
if __name__=="__main__":
    main()