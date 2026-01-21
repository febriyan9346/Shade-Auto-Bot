# 🚀 Shade Network Auto Bot

Automated bot for Shade Network points farming, daily claims, quest verification, and faucet claiming with captcha solving support.

## 📋 Features

- ✅ **Automated Daily Claims** - Claim daily rewards and track streaks
- 🎯 **Quest Verification** - Auto-verify Twitter and Discord quests
- 💧 **Faucet Claiming** - Automated faucet claims with captcha solving
- 🏆 **Leaderboard Tracking** - Monitor your rank and points
- 🔐 **Multi-Account Support** - Manage multiple wallets simultaneously
- 🌐 **Proxy Support** - Optional proxy rotation for each account
- 🤖 **Dual Captcha Solver** - Supports 2Captcha and SCTG with auto-fallback
- 📊 **Detailed Logging** - Color-coded console output with timestamps

## 🔗 Registration

Register on Shade Network using this referral link:
👉 **[https://v1.shadenetwork.io/ref/6pvefkoy](https://v1.shadenetwork.io/ref/6pvefkoy)**

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/febriyan9346/Shade-Auto-Bot.git
cd Shade-Auto-Bot
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure your accounts**
   - Create `accounts.txt` and add your private keys (one per line)
   - ⚠️ **Never share your private keys!**

4. **Configure captcha solver** (choose one or both)
   - For 2Captcha: Create `2captcha.txt` and add your API key
   - For SCTG: Create `sctg.txt` and add your API key

5. **Configure proxies** (optional)
   - Create `proxy.txt` and add your proxies (one per line)
   - Supported formats:
     - `ip:port`
     - `ip:port:username:password`
     - `http://ip:port`
     - `http://username:password@ip:port`

## 🎮 Usage

Run the bot:
```bash
python bot.py
```

### Menu Options

1. **Proxy Mode**
   - Option 1: Run with proxy (uses proxies from `proxy.txt`)
   - Option 2: Run without proxy

2. **Captcha Solver**
   - Option 1: Auto (tries 2Captcha first, then SCTG as fallback)
   - Option 2: 2Captcha only
   - Option 3: SCTG only

## 📁 File Structure

```
Shade-Auto-Bot/
├── bot.py              # Main bot script
├── accounts.txt        # Your wallet private keys (create this)
├── proxy.txt           # Proxy list (optional, create if needed)
├── 2captcha.txt        # 2Captcha API key (optional, create if needed)
├── sctg.txt           # SCTG API key (optional, create if needed)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 📋 Configuration Files

### accounts.txt
```
0x1234567890abcdef...
0xabcdef1234567890...
```

### proxy.txt
```
ip:port:username:password
http://username:password@ip:port
ip:port
```

### 2captcha.txt
```
your_2captcha_api_key_here
```

### sctg.txt
```
your_sctg_api_key_here
```

## 🔧 Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

Dependencies include:
- `requests` - HTTP requests
- `web3` - Ethereum interactions
- `colorama` - Colored terminal output
- `pytz` - Timezone handling
- `eth-account` - Ethereum account management
- `eth-utils` - Ethereum utilities

## ⚠️ Important Notes

- **Security**: Never share your `accounts.txt` file or private keys
- **Captcha Costs**: Both 2Captcha and SCTG are paid services
- **Rate Limits**: The bot includes built-in delays to respect rate limits
- **24h Cycle**: Bot runs in 24-hour cycles for optimal claiming
- **Backup**: Always backup your private keys securely

## 🐛 Troubleshooting

### Common Issues

1. **"accounts.txt not found"**
   - Create the file in the same directory as `bot.py`
   - Add your private keys (one per line)

2. **"Captcha solving failed"**
   - Check your API key in `2captcha.txt` or `sctg.txt`
   - Ensure you have sufficient balance in your captcha service account

3. **"Login failed"**
   - Verify your private key is correct
   - Check proxy connection if using proxies

4. **"Already claimed"**
   - This is normal - the bot will wait for the next cycle

## 📈 Features Breakdown

### Daily Claims
- Automatically claims daily rewards
- Tracks login streaks
- Displays total points

### Quest Verification
- Twitter quests (Follow, Like, Retweet)
- Discord quests (Join, Send Message)
- Automatic verification attempts

### Faucet Claiming
- Solves Turnstile captcha automatically
- Claims SHD tokens from faucet
- Displays transaction hash and status

### Leaderboard
- Shows your current rank
- Displays total points and level
- Updates after each cycle

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📜 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This bot is for educational purposes only. Use at your own risk. The author is not responsible for any losses or damages. Always ensure you comply with Shade Network's terms of service.

## 💖 Support Us with Cryptocurrency

You can make a contribution using any of the following blockchain networks:

| Network | Wallet Address |
|---------|---------------|
| **EVM** | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** | `9XgbPg8fndBquuYXkGpNYXKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

---

## 📞 Contact

- **GitHub**: [@febriyan9346](https://github.com/febriyan9346)
- **Repository**: [Shade-Auto-Bot](https://github.com/febriyan9346/Shade-Auto-Bot)

---

**⭐ If you find this bot helpful, please give it a star!**

**Made with ❤️ by FEBRIYAN**