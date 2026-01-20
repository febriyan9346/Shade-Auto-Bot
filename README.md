# Shade Network Auto Bot

Automated bot for Shade Network that handles daily claims, quest completion, activities check, and faucet claims.

## Register

Register here: [https://points.shadenetwork.io/ref/6pvefkoy](https://points.shadenetwork.io/ref/6pvefkoy)

## Features

- ✅ Auto Login with private key
- ✅ Auto Daily Claim
- ✅ Auto Complete Quests (Twitter, Discord, Telegram)
- ✅ Auto Check Activities
- ✅ Auto Faucet Claim
- ✅ Proxy Support
- ✅ Multi-account Support
- ✅ Automatic 24-hour cycle

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/febriyan9346/Shade-Auto-Bot.git
cd Shade-Auto-Bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create `accounts.txt` file and add your private keys (one per line):
```
0xYOUR_PRIVATE_KEY_1
0xYOUR_PRIVATE_KEY_2
0xYOUR_PRIVATE_KEY_3
```

2. (Optional) Create `proxy.txt` file for proxy support:
```
ip:port:username:password
ip:port:username:password
```

Or in standard format:
```
http://username:password@ip:port
http://username:password@ip:port
```

## Usage

Run the bot:
```bash
python bot.py
```

Select mode:
- **Option 1**: Run with proxy (requires proxy.txt)
- **Option 2**: Run without proxy

The bot will:
1. Login to all accounts
2. Claim daily rewards
3. Complete available quests
4. Check activities
5. Claim faucet
6. Wait 24 hours and repeat

## File Structure

```
Shade-Auto-Bot/
├── bot.py              # Main bot script
├── accounts.txt        # Your private keys (create this)
├── proxy.txt          # Your proxies (optional)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Security Warning

⚠️ **IMPORTANT**: 
- Never share your `accounts.txt` file
- Keep your private keys secure
- Use at your own risk
- This bot is for educational purposes

## Requirements.txt

Create a `requirements.txt` file with:
```
web3>=6.0.0
requests>=2.31.0
colorama>=0.4.6
pytz>=2023.3
eth-account>=0.9.0
eth-utils>=2.2.0
```

## Troubleshooting

**Login Failed**
- Check if your private key is correct
- Verify internet connection
- Try without proxy first

**Proxy Issues**
- Ensure proxy format is correct
- Test proxy connectivity
- Use mode 2 (without proxy) if issues persist

**Quest Not Completing**
- Some quests require manual verification
- Blockchain quests are skipped automatically
- Wait for next cycle

## Disclaimer

This bot is for educational purposes only. Use at your own risk. The developer is not responsible for any losses or damages.

## Support Us with Cryptocurrency

You can make a contribution using any of the following blockchain networks:

| Network | Wallet Address |
|---------|---------------|
| **EVM** | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** | `9XgbPg8fndBquuYXkGpNYKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

## Credits

Created by: **FEBRIYAN**

## License

MIT License - feel free to use and modify

---

⭐ If this bot helps you, please star this repository!
