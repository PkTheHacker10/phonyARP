from colorama import Back,Fore,Style
from random import choice
from art import text2art 

red=Fore.RED
green=Fore.GREEN
blue=Fore.BLUE
white=Fore.WHITE
yellow=Fore.YELLOW
cyan=Fore.CYAN
magenta=Fore.LIGHTMAGENTA_EX
mixed=Fore.BLUE+Fore.GREEN+Fore.RED
bright=Style.BRIGHT
reset=Style.RESET_ALL

def banner():
    # Function to create and return the banner of the tool.
    name="  PhonyARP"
    all_fonts=["graffiti","slant","speed","ogre","Poison","Star Wars","Ghost","Lean","Doom","Varsity","Alligator","Rectangles"]
    all_colour=[red,blue,yellow,cyan,mixed,magenta]
    selected_colour=choice(all_colour)
    selected_font=choice(all_fonts)
    Ascii_text=text2art(f"{name}",font=selected_font)
    return f"\n{bright}{selected_colour}{Ascii_text}{reset}"