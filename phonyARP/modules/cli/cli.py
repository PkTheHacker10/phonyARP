import sys
import argparse
import requests
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
bright=Style.BRIGHT
green=Fore.GREEN
red=Fore.RED
bold=Style.BRIGHT
reset=Style.RESET_ALL

def args():
    #function to get arguments.
    parser=argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False)
    try:
        parser.add_argument("-i","--interface",type=str)
        parser.add_argument("-t","--target",type=str)
        parser.add_argument("-g","--gateway",type=str)
        parser.add_argument("-sN","--scan-network",action="store_true")
        parser.add_argument("-v","--version",action="store_true")
        parser.add_argument("-h","--help",action="store_true")
        args=parser.parse_args()
        return args
    
    except argparse.ArgumentError:
        print(f"{bright}{red}\n [+] {reset}{blue}Please use -h to get more information.")
        
    except argparse.ArgumentTypeError:
        print(f"{bright}{blue}\n [+] {reset}{blue}Please use -h to get more information.")
        
    except Exception as e:
        print(f"{bright}{red}\n [+] {reset}{blue}Unexpected Argument Error:{e}")
        
def help():
    # Funtion to create and return the available options and flags.
    return f"""\n
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{white}]{reset}: {white}{bold}PhonyArp{reset} {white}is a tool which is purely meant for ARPSpoofing by {reset}{bold}{green}PkTheHacker10{reset}.\n
    {bold}{white}[{reset}{bold}{blue}Usage{reset}{white}]{reset}:{sys.argv[0]} -i <interface> -t <target> -g <gateway>\n
            {white}phonyARP {bold}{white}[{reset}{bold}{blue}flags{reset}{bold}{white}]\n
    [{reset}{bold}{blue}flags{reset}{bold}{white}]
                
            [{reset}{bold}{blue}input{reset}{bold}{white}]{reset}
            
                -i,   --interface               :  Interface is used to send spoofed arp packets. [mandatory]  
                -t,   --target                  :  Target ip to spoof the arp table.              [mandatory]
                -g,   --gateway                 :  Gatway ip to imprisonate to the target.        [mandatory]
                    
            {bold}{white}[{reset}{bold}{blue}debug{reset}{bold}{white}]{reset}
                   
                -v,   --version                 :  To check version of this tool. 
                -sN,  --scan-network            :  To scan network to find alive hosts.
                -h,   --help                    :  To see all the available options.
          """
def get_version():
    #funtion which is used to get the version (tag) from github through api.
    try:
        url="https://api.github.com/repos/PkTheHacker10/phonyARP/releases/latest"
        response=requests.get(url,timeout=3,verify=True)
        if response.status_code==200:
            json_data=response.json()
            latest=json_data.get('tag_name')
            return latest
        
    except (requests.ConnectTimeout,requests.ReadTimeout,requests.Timeout):
        print(f"{bright}{blue}\n [+] {reset} : Connection TimeOut while getting version.")
        
    except requests.JSONDecodeError:
        print(f"{bright}{red}\n [+] {reset} : Couldn't decode data.")
        