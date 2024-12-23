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
    print(f"{bright}{yellow} [+] {reset} :{red}Could't import :{e}{reset}")
    exit(1)
    
def main():
    #Function will call phonyhandler.
    phonyarp_bannner=banner.banner()
    print(phonyarp_bannner)
    try:
        phonyhandler=Phonyhandler()
        phonyhandler.start()
            
    except KeyboardInterrupt:
        print(f"{bright}{yellow} [+] {reset}{blue}: Quiting...\n")
    
if __name__=="__main__":
    main()