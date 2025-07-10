import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('clear')

def animation(message, delay=0.03):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("")

def loading_bar(task="Processing"):
    bar = f"{task}: [                    ]"
    print(Fore.YELLOW)
    for i in range(1, 21):
        bar = bar[:task.__len__() + 3 + i] + "=" + bar[task.__len__() + 4 + i:]
        sys.stdout.write(Fore.MAGENTA + "\r" + bar)
        sys.stdout.flush()
        time.sleep(0.07)
    print("")

def banner():
    clear()
    print(Fore.CYAN + Style.BRIGHT + """
  █████╗ ██╗     ██╗     ██╗███████╗
 ██╔══██╗██║     ██║     ██║██╔════╝
 ███████║██║     ██║     ██║█████╗   
 ██╔══██║██║     ██║     ██║██╔══╝   
 ██║  ██║███████╗███████╗██║███████╗
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝
      WHATSAPP BAN REVIEW TOOL - BY ALLIE
""")

def fake_trace():
    animation("🛰️ Tracing WhatsApp server...")
    time.sleep(1)
    print(Fore.GREEN + "IP Found: 157.240.22.35")
    print("Location: Menlo Park, California, USA")

def fake_ping():
    print(Fore.GREEN + "\n📶 Pinging whatsapp.com [157.240.22.35] with 32 bytes of data:")
    for _ in range(4):
        print("Reply from 157.240.22.35: bytes=32 time=22ms TTL=56")
        time.sleep(0.5)
    print("Ping stats: Sent = 4, Received = 4, Lost = 0 (0% loss)")

def fake_hack_sequence():
    steps = [
        "Injecting spoofed session tokens...",
        "Bypassing TLS encryption...",
        "Connecting to WhatsApp internal APIs...",
        "Brute-forcing verification checksum...",
        "Spoof session established."
    ]
    for step in steps:
        animation("🔐 " + step)
        time.sleep(0.8)

def generate_email(phone, ban_type):
    if ban_type == "1":
        subject = "Request to Review My Temporarily Banned WhatsApp Account"
        body = f"""Dear WhatsApp Team,

My number {phone} was temporarily banned.
I believe this was a mistake, and I kindly request that my account be reviewed.

I use WhatsApp responsibly and will fully comply with your terms of service.

Thank you,
Allie’s Tech"""
    else:
        subject = "Appeal for Permanent WhatsApp Ban"
        body = f"""Dear WhatsApp Team,

My number {phone} was permanently banned.
I respectfully appeal this decision and request a review of my account.

I understand the importance of complying with WhatsApp’s policies, and I’m committed to following all guidelines moving forward.

Thank you for considering my appeal,
Allie’s Tech"""
    return subject, body

def show_smart_replies():
    print(Fore.YELLOW + "\n💬 WhatsApp Support May Reply:")
    print("- 'Your number was banned for violating our Terms of Service.'")
    print("- 'We’ve received your appeal and will get back within 48 hours.'")

def log_action(phone, ban_type):
    with open("logs.txt", "a") as f:
        f.write(f"{time.ctime()} | {phone} | {'Temporary' if ban_type == '1' else 'Permanent'}\n")

def bypass_options():
    print("\n🛡️ Choose Unban Bypass Mode:")
    print("1. Soft Review (recommended)")
    print("2. Hard Force Unban (⚠️ risky)")
    mode = input("👉 Enter option: ")
    if mode == "2":
        animation("⚠️ Attempting deep override...")
        animation("💥 Exploit failed! WhatsApp detected intrusion.")
    else:
        animation("✅ Soft review bypass mode selected. Message generated successfully.")

def easter_egg():
    secret = input("\n🔐 Enter secret override code (press Enter to skip): ")
    if secret == "1337":
        print(Fore.MAGENTA + "🎉 Secret Hack Mode Activated: You found Allie’s Easter Egg!")
        print("🧠 Fun fact: This tool is 100% simulation and just for entertainment 😅")

def main():
    banner()
    animation(Fore.GREEN + "👾 Booting Allies Hack Tool...")
    time.sleep(1)

    fake_trace()
    fake_ping()
    loading_bar("Checking ban status")
    fake_hack_sequence()

    print(Fore.YELLOW + "\nWhat kind of ban are you experiencing?")
    print("1️⃣  Temporary Ban")
    print("2️⃣  Permanent Ban")
    ban_type = input("👉 Enter 1 or 2: ").strip()

    if ban_type not in ["1", "2"]:
        print(Fore.RED + "❌ Invalid selection. Exiting.")
        sys.exit(1)

    phone = input("\n📱 Enter your phone number (e.g., +2348012345678): ").strip()
    if not phone:
        print(Fore.RED + "❌ No phone number entered. Exiting.")
        sys.exit(1)

    print(Fore.MAGENTA + "\n🧠 Generating custom email message", end="")
    for _ in range(6):
        print(".", end='', flush=True)
        time.sleep(0.3)
    print("\n")

    subject, body = generate_email(phone, ban_type)

    print(Fore.GREEN + "\n📄 Generated Email Message:")
    print(Fore.CYAN + "----------------------------------------------")
    print("To: support@whatsapp.com")
    print(f"Subject: {subject}\n")
    print(body)
    print(Fore.CYAN + "----------------------------------------------")

    show_smart_replies()
    bypass_options()
    log_action(phone, ban_type)
    easter_egg()

    print()
    animation("💬 Tool created by Allie’s Tech | Contact: +2348030476809")
    print(Fore.GREEN + "\n✅ DONE. You can now copy the message above and email WhatsApp Support.")

if __name__ == "__main__":
    main()
