#!/data/data/com.termux/files/usr/bin/bash

# === Colors ===
GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
CYAN="\033[1;36m"
PURPLE="\033[1;35m"
RESET="\033[0m"

clear
echo -e "${CYAN}"
echo "=============================================="
echo "       ALLIE'S WHATSAPP REVIEW TOOL"
echo "=============================================="
echo -e "${RESET}"

echo -e "${GREEN}👾 Initializing Hackish Protocols...${RESET}"
sleep 0.5

# === Animation effect: fake hacking sequence ===
animation() {
  local message="$1"
  for ((i=0; i<${#message}; i++)); do
    echo -n "${message:$i:1}"
    sleep 0.03
  done
  echo ""
}

animation "🔍 Connecting to WhatsApp servers..."
sleep 1
animation "✅ Connection established."
sleep 0.5
animation "📡 Verifying ban status..."
sleep 1.2
animation "🛑 Ban confirmed. Preparing recovery options..."
sleep 0.5

# === Ban type selection ===
echo ""
echo -e "${YELLOW}What kind of ban are you experiencing?${RESET}"
echo "1️⃣  Temporary Ban"
echo "2️⃣  Permanent Ban"
read -p "👉 Enter 1 or 2: " bantype

if [[ "$bantype" != "1" && "$bantype" != "2" ]]; then
  echo -e "${RED}❌ Invalid selection. Exiting...${RESET}"
  exit 1
fi

# === Phone number input ===
echo ""
read -p "📱 Enter your phone number (e.g., +234xxxxxxxxxx): " phone

if [ -z "$phone" ]; then
  echo -e "${RED}❌ No phone number entered. Exiting...${RESET}"
  exit 1
fi

# === Fancy loading ===
echo -ne "${PURPLE}🧠 Generating custom recovery message"
for i in {1..6}; do echo -n "."; sleep 0.3; done
echo -e "${RESET}"
sleep 0.5

# === Generate message based on ban type ===
if [ "$bantype" == "1" ]; then
  subject="Request to Review My Temporarily Banned WhatsApp Account"
  body = """Dear WhatsApp Team,
I am writing this to request a review...
Thank you for your support.
"""
My number $phone was temporarily banned.
I believe this was a mistake, and I kindly request that my account be reviewed.

I use WhatsApp responsibly and will fully comply with your terms of service.

Thank you,
Allie’s Tech"
else
  subject="Appeal for Permanent WhatsApp Ban"
  body="Dear WhatsApp Team,

My number $phone was permanently banned.
I respectfully appeal this decision and request a review of my account.

I understand the importance of complying with WhatsApp’s policies, and I’m committed to following all guidelines moving forward.

Thank you for considering my appeal,
Allie’s Tech"
fi

# === Display the message ===
echo ""
echo -e "${GREEN}📄 Generated Message:${RESET}"
echo "----------------------------------------------"
echo "To: support@whatsapp.com"
echo "Subject: $subject"
echo ""
echo "$body"
echo "----------------------------------------------"

# === Ask to open email ===
read -p "📧 Do you want to open your email app now? (y/n): " open_email

if [[ "$open_email" == "y" || "$open_email" == "Y" ]]; then
  enc_subject=$(echo "$subject" | sed 's/ /%20/g')
  enc_body=$(echo "$body" | sed 's/ /%20/g' | sed ':a;N;$!ba;s/\n/%0D%0A/g')
  termux-open "mailto:support@whatsapp.com?subject=$enc_subject&body=$enc_body"
  echo ""
  echo -e "${CYAN}📨 Launching your email app...${RESET}"
else
  echo -e "${YELLOW}📋 You can copy the message above manually.${RESET}"
fi

# === Final outro ===
echo ""
animation "💬 Tool created by Allie’s Tech | Contact: +2348030476809"
