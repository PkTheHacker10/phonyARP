import sys
import argparse
import requests
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
green=Fore.GREEN
bold=Style.BRIGHT
reset=Style.RESET_ALL

def args():
    #function to get arguments.
    parser=argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False)
    try:
        parser.add_argument("-i","--interface",type=str)
        parser.add_argument("-t","--target",type=str)
        parser.add_argument("-g","--gateway",type=str)
        parser.add_argument("-v","--version",action="store_true")
        parser.add_argument("-h","--help",action="store_true")
        args=parser.parse_args()
        return args
    
    except argparse.ArgumentError:
        print(f"{bold}{blue}INFO:{reset}Please use -h to get more information.")
        
    except argparse.ArgumentTypeError:
        print(f"{bold}{blue}INFO:{reset}Please use -h to get more information.")
        
    except Exception as e:
        print(f"{bold}{blue}INFO:{reset}Unexpected Argument Error:{e}")
        
def help():
    # Funtion to create and return the available options and flags.
    return f"""\n
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
def get_version():
    #funtion which is used to get the version (tag) from github through api
    #TODO chang the url after relese it .
    try:
        url="https://api.github.com/repos/PkTheHacker10/phonyARP"
        response=requests.get(url,timeout=3,verify=True)
        if response.status_code==200:
            json_data=response.json()
            latest=json_data.get('tag_name')
            return latest
        else:
            return "v0.0.1"
        
    except (requests.ConnectTimeout,requests.ReadTimeout,requests.Timeout):
        print(f"{bold}{white}[{reset}{blue}INFO{reset}{bold}{white}]{reset} : {white}Connection TimeOut while getting version{reset}.")
        
    except requests.JSONDecodeError:
        print(f"{bold}{white}[{reset}{blue}INFO{reset}{bold}{white}]{reset} : {white}Couldn't decode data{reset}.")