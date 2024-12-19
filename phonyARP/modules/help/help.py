from colorama import Fore,Style 
import sys
red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
yellow=Fore.YELLOW
green=Fore.GREEN
cyan=Fore.CYAN
bold=Style.BRIGHT
reset=Style.RESET_ALL

def help():
    # Funtion to create and return the available options and flags.
    help=f"""\n
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{white}]{reset}: {white}{bold}PhonyArp{reset} {white}is a tool which is purely meant for ARPSpoofing by {reset}{bold}{green}PkTheHacker10{reset}.\n
    {bold}{white}[{reset}{bold}{blue}Usage{reset}{white}]{reset}:{sys.argv[0]} -i <interface> -t <target> -g <gateway>\n
            {white}phonyarp {bold}{white}[{reset}{bold}{blue}flags{reset}{bold}{white}]\n
    [{reset}{bold}{blue}flags{reset}{bold}{white}]
                
            [{reset}{bold}{blue}input{reset}{bold}{white}]{reset}
            
                -i,   --interface               :  interface is used to send spoofed arp packets. [mandatory]  
                -t,   --target                  :  target ip to spoof the arp table.              [mandatory]
                -g,   --gateway                 :  gatway ip to imprisonate to the target.        [mandatory]
                    
            {bold}{white}[{reset}{bold}{blue}debug{reset}{bold}{white}]{reset}
                   
                -v,   --version                 :  to check version of this tool. 
                -h,   --help                    :  to see all the available options.
          """
    return help