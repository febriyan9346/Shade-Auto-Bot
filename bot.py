import os
import time
import random
import requests
import json
from datetime import datetime
import pytz
from colorama import Fore, Style, init
from web3 import Web3
from eth_account.messages import encode_defunct
from eth_utils import to_checksum_address

os.system('clear' if os.name == 'posix' else 'cls')
import warnings
warnings.filterwarnings('ignore')
import sys
if not sys.warnoptions:
    os.environ["PYTHONWARNINGS"] = "ignore"

init(autoreset=True)

class ShadeBot:
    def __init__(self):
        self.base_headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        }

    def get_headers(self, subdomain="points", auth_token=None):
        headers = self.base_headers.copy()
        headers["authority"] = f"{subdomain}.shadenetwork.io"
        headers["origin"] = f"https://{subdomain}.shadenetwork.io"
        headers["referer"] = f"https://{subdomain}.shadenetwork.io/"
        
        if auth_token and subdomain == "points":
            headers["authorization"] = f"Bearer {auth_token}"
            
        return headers

    def get_wib_time(self):
        wib = pytz.timezone('Asia/Jakarta')
        return datetime.now(wib).strftime('%H:%M:%S')
    
    def print_banner(self):
        banner = f"""
{Fore.CYAN}SHADE NETWORK AUTO BOT{Style.RESET_ALL}
{Fore.WHITE}By: FEBRIYAN{Style.RESET_ALL}
{Fore.CYAN}============================================================{Style.RESET_ALL}
"""
        print(banner)
    
    def log(self, message, level="INFO"):
        time_str = self.get_wib_time()
        
        if level == "INFO":
            color = Fore.CYAN
            symbol = "[INFO]"
        elif level == "SUCCESS":
            color = Fore.GREEN
            symbol = "[SUCCESS]"
        elif level == "ERROR":
            color = Fore.RED
            symbol = "[ERROR]"
        elif level == "WARNING":
            color = Fore.YELLOW
            symbol = "[WARNING]"
        elif level == "CYCLE":
            color = Fore.MAGENTA
            symbol = "[CYCLE]"
        else:
            color = Fore.WHITE
            symbol = "[LOG]"
        
        print(f"[{time_str}] {color}{symbol} {message}{Style.RESET_ALL}")
    
    def random_delay(self):
        delay = random.randint(3, 7)
        self.log(f"Delay {delay} seconds...", "INFO")
        time.sleep(delay)
    
    def show_menu(self):
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Select Mode:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Run with proxy")
        print(f"2. Run without proxy{Style.RESET_ALL}")
        print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}")
        
        while True:
            try:
                choice = input(f"{Fore.GREEN}Enter your choice (1/2): {Style.RESET_ALL}").strip()
                if choice in ['1', '2']:
                    return choice
                else:
                    print(f"{Fore.RED}Invalid choice! Please enter 1 or 2.{Style.RESET_ALL}")
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}Program terminated by user.{Style.RESET_ALL}")
                exit(0)
    
    def countdown(self, seconds):
        for i in range(seconds, 0, -1):
            hours = i // 3600
            minutes = (i % 3600) // 60
            secs = i % 60
            print(f"\r[COUNTDOWN] Next cycle in: {hours:02d}:{minutes:02d}:{secs:02d} ", end="", flush=True)
            time.sleep(1)
        print("\r" + " " * 60 + "\r", end="", flush=True)

    def load_file(self, filename):
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return []
    
    def format_proxy(self, proxy_str):
        if not proxy_str:
            return None
        if "://" not in proxy_str:
            parts = proxy_str.split(':')
            if len(parts) == 4:
                proxy_str = f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
            elif len(parts) == 2:
                proxy_str = f"http://{proxy_str}"
            else:
                if "@" not in proxy_str:
                     proxy_str = f"http://{proxy_str}"
        return {"http": proxy_str, "https": proxy_str}

    def get_signature_data(self, private_key):
        try:
            w3 = Web3()
            
            pk = private_key.strip()
            if pk.startswith('0x'):
                pk = pk[2:]
            
            if len(pk) != 64:
                raise ValueError(f"Invalid private key length: {len(pk)}, expected 64 hex chars")
            
            pk_with_prefix = '0x' + pk
            account = w3.eth.account.from_key(pk_with_prefix)
            address = to_checksum_address(account.address)
            timestamp = int(time.time() * 1000)
            message = f"Shade Points: Create account for {address.lower()} at {timestamp}"
            encoded_message = encode_defunct(text=message)
            signed_message = w3.eth.account.sign_message(encoded_message, private_key=pk_with_prefix)
            signature = signed_message.signature.hex()
            
            if not signature.startswith('0x'):
                signature = '0x' + signature
            
            return address, timestamp, signature, message
            
        except Exception as e:
            self.log(f"Error in get_signature_data: {str(e)}", "ERROR")
            raise

    def do_login(self, private_key, proxies):
        try:
            address, timestamp, signature, message = self.get_signature_data(private_key)
            
            payload = {
                "address": address,
                "timestamp": timestamp,
                "signature": signature
            }
            
            self.log(f"{address[:6]}...{address[-4:]}", "INFO")
            
            headers = self.get_headers("points")
            
            response = requests.post(
                "https://points.shadenetwork.io/api/auth/session",
                headers=headers,
                json=payload,
                proxies=proxies,
                timeout=30
            )
            
            if response.status_code in [200, 201]:
                data = response.json()
                if "token" in data:
                    time_str = self.get_wib_time()
                    print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Login successful!{Style.RESET_ALL}")
                    return data['token'], address
                else:
                    self.log(f"Token not in response", "WARNING")
            else:
                self.log(f"Login failed [{response.status_code}]", "ERROR")
                    
        except Exception as e:
            self.log(f"Login error: {str(e)}", "ERROR")
        
        return None, None

    def do_claim(self, token, proxies):
        headers = self.get_headers("points", auth_token=token)
        try:
            self.log(f"Processing Daily Claim:", "INFO")
            
            self.random_delay()
            
            response = requests.post(
                "https://points.shadenetwork.io/api/claim", 
                headers=headers, 
                json={}, 
                proxies=proxies, 
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    reward = data.get('reward', 0)
                    streak = data.get('streak', 0)
                    new_points = data.get('newPoints', 0)
                    
                    time_str = self.get_wib_time()
                    print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Claim Success! Reward: +{reward} Points | Streak: {streak} days{Style.RESET_ALL}")
                    
                    self.random_delay()
                    
                    time_str = self.get_wib_time()
                    print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Total Points: {new_points:,}{Style.RESET_ALL}")
                else:
                    self.log(f"Not claimed yet", "WARNING")
            elif response.status_code == 400:
                self.log("Already claimed", "WARNING")
            elif response.status_code == 429:
                self.log("Already claimed", "WARNING")
            else:
                self.log(f"Not claimed yet", "WARNING")
                
        except Exception as e:
            self.log(f"Claim error", "ERROR")

    def verify_twitter(self, token, proxies):
        headers = self.get_headers("points", auth_token=token)
        headers["referer"] = "https://points.shadenetwork.io/quests"
        
        twitter_quests = [
            {"questId": "social_001", "title": "Follow Twitter"},
            {"questId": "social_002", "title": "Like Tweet"},
            {"questId": "social_003", "title": "Retweet"},
        ]
        
        try:
            self.log("Processing Twitter Verifications:", "INFO")
            
            for quest in twitter_quests:
                self.random_delay()
                
                response = requests.post(
                    "https://points.shadenetwork.io/api/quests/verify-twitter",
                    headers=headers,
                    json={"questId": quest["questId"]},
                    proxies=proxies,
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("verified"):
                        time_str = self.get_wib_time()
                        print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Twitter Quest '{quest['title']}' Verified!{Style.RESET_ALL}")
                elif response.status_code == 400:
                    pass
                else:
                    pass
                    
        except Exception as e:
            pass

    def verify_discord(self, token, proxies):
        headers = self.get_headers("points", auth_token=token)
        headers["referer"] = "https://points.shadenetwork.io/quests"
        
        discord_quests = [
            {"questId": "social_006", "title": "Join Discord"},
            {"questId": "social_007", "title": "Send Message"},
        ]
        
        try:
            self.log("Processing Discord Verifications:", "INFO")
            
            for quest in discord_quests:
                self.random_delay()
                
                response = requests.post(
                    "https://points.shadenetwork.io/api/quests/verify-discord",
                    headers=headers,
                    json={"questId": quest["questId"]},
                    proxies=proxies,
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("verified"):
                        time_str = self.get_wib_time()
                        print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Discord Quest '{quest['title']}' Verified!{Style.RESET_ALL}")
                elif response.status_code == 400:
                    pass
                else:
                    pass
                    
        except Exception as e:
            pass

    def do_faucet(self, address, proxies):
        url = "https://wallet.shadenetwork.io/api/faucet"
        headers = self.get_headers("wallet")
        payload = {"address": address}
        
        try:
            self.log("Processing Faucet Claim:", "INFO")
            
            self.random_delay()
            
            response = requests.post(
                url, 
                headers=headers, 
                json=payload, 
                proxies=proxies, 
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    amount = data.get("amount", "0")
                    tx_hash = data.get("txHash", "")
                    
                    time_str = self.get_wib_time()
                    print(f"[{time_str}] {Fore.GREEN}[SUCCESS] Faucet Claimed! Amount: {amount} SHD{Style.RESET_ALL}")
                    
                    self.random_delay()
                    
                    time_str = self.get_wib_time()
                    print(f"[{time_str}] {Fore.GREEN}[SUCCESS] TxHash: {tx_hash[:10]}...{tx_hash[-8:]}{Style.RESET_ALL}")
                else:
                    self.log("Not claimed yet", "WARNING")
            elif response.status_code == 429:
                error_data = response.json() if response.text else {}
                error_msg = error_data.get('error', '')
                if error_msg:
                    self.log(f"Faucet: {error_msg}", "WARNING")
                else:
                    self.log("Already claimed", "WARNING")
            elif response.status_code == 404:
                self.log("Already claimed", "WARNING")
            else:
                self.log(f"Not claimed yet", "WARNING")
        
        except requests.exceptions.Timeout:
            self.log("Faucet timeout", "WARNING")
        except Exception as e:
            self.log(f"Faucet error: {str(e)}", "WARNING")

    def run(self):
        self.print_banner()
        
        mode = self.show_menu()
        use_proxy = True if mode == '1' else False
        
        private_keys = self.load_file("accounts.txt")
        proxies_list = self.load_file("proxy.txt")
        
        if not private_keys:
            self.log("File accounts.txt not found or empty!", "ERROR")
            return

        if use_proxy:
            self.log("Running with Proxy Mode", "INFO")
            if not proxies_list:
                self.log("WARNING: Proxy mode selected but proxy.txt is empty!", "WARNING")
        else:
            self.log("Running without Proxy Mode", "INFO")
            
        self.log(f"Loaded {len(private_keys)} accounts successfully", "INFO")
        
        print(f"\n{Fore.CYAN}============================================================{Style.RESET_ALL}\n")
        
        cycle = 1
        while True:
            self.log(f"Cycle #{cycle} Started", "CYCLE")
            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            
            success_count = 0
            
            for i, pk in enumerate(private_keys):
                current_proxy = None
                proxy_log_str = "No Proxy"
                
                if use_proxy and proxies_list:
                    raw_proxy = proxies_list[i % len(proxies_list)]
                    current_proxy = self.format_proxy(raw_proxy)
                    if "@" in raw_proxy:
                        proxy_log_str = raw_proxy.split("@")[1]
                    else:
                        proxy_log_str = raw_proxy

                self.log(f"Account #{i+1}/{len(private_keys)}", "INFO")
                self.log(f"Proxy: {proxy_log_str}", "INFO")
                
                token, address = self.do_login(pk, current_proxy)
                
                if token and address:
                    success_count += 1
                    
                    self.do_claim(token, current_proxy)
                    
                    self.verify_twitter(token, current_proxy)
                    
                    self.verify_discord(token, current_proxy)

                    self.do_faucet(address, current_proxy)
                else:
                    self.log(f"Skipping account #{i+1} due to login failure", "WARNING")

                if i < len(private_keys) - 1:
                    print(f"{Fore.WHITE}............................................................{Style.RESET_ALL}")
                    time.sleep(2)
            
            print(f"{Fore.CYAN}------------------------------------------------------------{Style.RESET_ALL}")
            self.log(f"Cycle #{cycle} Complete | Success: {success_count}/{len(private_keys)}", "CYCLE")
            print(f"{Fore.CYAN}============================================================{Style.RESET_ALL}\n")
            
            cycle += 1
            wait_time = 86400
            self.countdown(wait_time)

if __name__ == "__main__":
    bot = ShadeBot()
    bot.run()
