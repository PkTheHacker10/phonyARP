from colorama import Fore,Style
from phonyARP.modules.handler import Phonyhandler

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

def main():
    #Function will call phonyhandler.
    try:
        phonyhandler=Phonyhandler()
        phonyhandler.start()
        
    except KeyboardInterrupt:
        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Quiting...\n")
    
if __name__=="__main__":
    main()