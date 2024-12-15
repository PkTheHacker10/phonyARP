from phonyARP.modules.banner import banner

class handler():
    def banner(self):
        phony_banner=banner.banner()
        print(phony_banner)
    def start(self):
        self.banner()