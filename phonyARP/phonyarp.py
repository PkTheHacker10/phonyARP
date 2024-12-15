from phonyARP.modules.banner import banner
from phonyARP.modules.cli import cli

class handler():
    def __init__(self):
        self.toolbanner=banner.banner()
        self.args=cli.args()
    def start(self):
        print(self.toolbanner)
        print(self.args)