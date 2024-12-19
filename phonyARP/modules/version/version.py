import requests
from colorama import Fore,Style 

blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

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
        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset} : {white}Connection TimeOut while getting version{reset}.")
        
    except requests.JSONDecodeError:
        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset} : {white}Couldn't decode data{reset}.")