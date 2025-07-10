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
    print(Fore.YELLOW + "")
    for i in range(1, 21):
        bar = bar[:task.__len__() + 3 + i] + "=" + bar[task.__len__() + 4 + i:]
        sys.stdout.write(Fore.MAGENTA + "\r" + bar)
        sys.stdout.flush()
        time.sleep(0.1)
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

def fake_hack_sequence():
    steps = [
        "Initializing kernel bypass...",
        "Injecting spoofed tokens...",
        "Connecting to WhatsApp Core...",
        "Bypassing 2FA firewall...",
        "Spoof session established!",
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

def main():
    banner()
    animation(Fore.GREEN + "👾 Initializing Hackish Protocols...")
    time.sleep(1)

    animation("🔍 Connecting to WhatsApp servers...")
    time.sleep(1)
    animation("✅ Connection established.")
    time.sleep(0.5)

    loading_bar("Verifying ban status")
    fake_hack_sequence()

    print(Fore.YELLOW + "\nWhat kind of ban are you experiencing?")
    print("1️⃣  Temporary Ban")
    print("2️⃣  Permanent Ban")
    ban_type = input("👉 Enter 1 or 2: ").strip()

    if ban_type not in ["1", "2"]:
        print(Fore.RED + "❌ Invalid selection. Exiting...")
        sys.exit(1)

    phone = input("\n📱 Enter your phone number (e.g., +234xxxxxxxxxx): ").strip()
    if not phone:
        print(Fore.RED + "❌ No phone number entered. Exiting...")
        sys.exit(1)

    print(Fore.MAGENTA + "\n🧠 Generating custom recovery message", end="")
    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")

    subject, body = generate_email(phone, ban_type)

    print(Fore.GREEN + "\n📄 Generated Message:")
    print(Fore.CYAN + "----------------------------------------------")
    print("To: support@whatsapp.com")
    print(f"Subject: {subject}\n")
    print(body)
    print(Fore.CYAN + "----------------------------------------------")

    open_mail = input(Fore.YELLOW + "\n📧 Do you want to simulate opening email app? (y/n): ").strip().lower()
    if open_mail == 'y':
        print(Fore.CYAN + "\n📨 Simulating launch of email app...")
        time.sleep(1)
        print(Fore.YELLOW + "✉️  (Pretending to send this to support@whatsapp.com...)")
    else:
        print(Fore.YELLOW + "\n📋 You can copy the message above manually.")

    print()
    animation("💬 Tool created by Allie’s Tech | Contact: +2348030476809")

if __name__ == "__main__":
    main()
