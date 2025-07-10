import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.GREEN + Style.BRIGHT + """
  █████╗ ██╗     ██╗     ██╗███████╗██╗  ██╗
 ██╔══██╗██║     ██║     ██║██╔════╝██║ ██╔╝
 ███████║██║     ██║     ██║█████╗  █████╔╝ 
 ██╔══██║██║     ██║     ██║██╔══╝  ██╔═██╗ 
 ██║  ██║███████╗███████╗██║███████╗██║  ██╗
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝
     WHATSAPP BAN SIMULATOR - BY ALLIE

""")

def animation(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ban_type():
    print(Fore.YELLOW + "\nChoose a ban type:")
    print(Fore.CYAN + "[1] Temporary Ban")
    print(Fore.RED + "[2] Permanent Ban")
    choice = input(Fore.GREEN + "\nEnter your choice (1 or 2): ")
    return choice

def temp_ban():
    animation(Fore.YELLOW + "\n[+] Connecting to WhatsApp servers...")
    time.sleep(2)
    animation(Fore.CYAN + "[+] Sending temporary ban request...")
    time.sleep(2)
    animation(Fore.RED + "\n[✓] User temporarily banned for 72 hours.")
    animation(Fore.GREEN + "Simulation complete.\n")

def perm_ban():
    animation(Fore.YELLOW + "\n[+] Connecting to WhatsApp servers...")
    time.sleep(2)
    animation(Fore.CYAN + "[+] Sending permanent ban request...")
    time.sleep(2)
    animation(Fore.RED + "\n[✓] User permanently banned from WhatsApp.")
    animation(Fore.GREEN + "Simulation complete.\n")

    # Fake email message
    message = """\n
Dear WhatsApp Team,

I am writing to request a review of my account, which appears to be banned.
If this action was a mistake, please assist me in restoring access.

Best regards,  
Allie
"""
    print(Fore.LIGHTBLUE_EX + message)

# Main flow
banner()
choice = ban_type()

if choice == '1':
    temp_ban()
elif choice == '2':
    perm_ban()
else:
    print(Fore.RED + "\nInvalid choice. Exiting...\n")
