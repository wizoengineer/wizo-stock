# Wizo Stock

**Wizo Stock** is a Discord bot that fetches and displays real-time stock market charts.

### **Get Started:**
After you run the bot - use the command below for setup:

> /chart 15min #channel

- "ticker": Use yahoo finance for tickers. `NQ=F` is Nasdaq.
- "interval": The update frequency (e.g., 30min, 1h, 2h, etc.).

Example: Start the bot with `python bot.py` and run the server with `python server.py`. Once started, use /chart.

### **Features:**
- **📈 Customizable Channels:** Choose a specific Discord channel for the bot to send stock market charts.
- **⏱️ Automated Updates:** Set intervals to receive charts automatically, ensuring you never miss a market update.

### **Important Notes**:
- **🛠️ Single Guild Support:** Currently, the bot supports only one guild (server) at a time. Support for multiple guilds may be added in the future.
- **💻 Self-Hosting Required:** You’ll need to set up your own host to run the bot.
- **🚨 DISCORD_TOKEN:** You'll need to create a .env file in the root directory and define variable DISCORD_TOKEN with your bot’s token.
- **🧪 Unit Testing:** Run unit tests with `python -m unittest`.

### **Current Simple Architecture**:

![Wizo-Stock-Architecture](architecture.png)
