from subprocess import run
from platform import system
from netaddr import IPNetwork,AddrFormatError
from concurrent.futures import ThreadPoolExecutor
from scapy.all import ARP, Ether, srp
from colorama import Fore,Style

blue=Fore.BLUE
bright=Style.BRIGHT
yellow=Fore.YELLOW
red=Fore.RED
green=Fore.GREEN
reset=Style.RESET_ALL

def hostbyip():
    ip_obj = run(["hostname", "-I"], capture_output=True, text=True)
    return ip_obj.stdout.strip()

def cidr_calculator(ip):
    # Funtion to default subnetmask.
    first_octet=int(ip.split(".")[0])
    if 1 <= first_octet <= 126:
        return f"{ip}/8"
    elif 128 <= first_octet <= 191:
        return f"{ip}/16"
    elif 192 <= first_octet <= 223:
        return f"{ip}/24"
    else:
        return None
    
def range_calculator(cidr):
    try:
        return [str(ip)for ip in list(IPNetwork(cidr))]
    except AddrFormatError:
        print(f"{bright}{yellow} [+] {reset}{blue}Unexpected exception :Address formate error.")
        exit(1)

def arp(ip):
    try:
        print(f"\r{bright}{yellow} [+] {reset}{green}Scanning ip :{reset}{ip}",end="")
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        result = srp(pkt, timeout=1, verbose=0)[0]
        if result:
            return ip
        else:
            return None
        
    except PermissionError:
        print(f"{bright}{yellow} [+] {reset}{blue}Permission error: Run it as root")
        exit()
        
    except Exception as e:
        print(f"{bright}{yellow} [+] {reset}{blue}Unexpected error on sweeper.ping:{e}")



def sweeper():
    alive_host=[]
    ip=hostbyip()
    cidr=cidr_calculator(ip)
    ip_list=range_calculator(cidr)
    ip_count=len(ip_list)
    if ip_count>1:
        #default_thread_count=default_thread_count//2
        with ThreadPoolExecutor(max_workers=40) as thread:
             results=thread.map(
                 lambda ip:
                     arp(ip),
                     [str(ip) for ip in ip_list])
             for result in results:
                if result is not None and result != ip:
                     alive_host.append(result)
        return alive_host
    else:
        return None


    
    