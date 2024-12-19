from colorama import Fore,Style 
import argparse

red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
bright=Style.BRIGHT
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
        print(f"{bright}{blue}INFO:{reset}Please use -h to get more information.")
        
    except argparse.ArgumentTypeError:
        print(f"{bright}{blue}INFO:{reset}Please use -h to get more information.")
        
    except Exception as e:
        print(f"{bright}{blue}INFO:{reset}Unexpected Error:{e}")
