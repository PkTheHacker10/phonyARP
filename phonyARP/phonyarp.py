import sys
from colorama import Fore,Style 

blue=Fore.BLUE
bright=Style.BRIGHT
reset=Style.RESET_ALL

try:
    from phonyARP.modules.banner import banner
    from phonyARP.modules.cli import cli
    from phonyARP.modules.help import help
    
except ImportError as e:
    print(f"{bright}{blue}INFO:{reset}Could't import :{e}")
    sys.exit()
    
class handler():
    
    def __init__(self):
        self.toolbanner=banner.banner()
        self.args=cli.args()
        self.help=help.help()
        
    def start(self):
        print(self.toolbanner)
        print(self.args)
        print(self.help)