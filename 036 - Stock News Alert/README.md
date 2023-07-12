# Stock News Alert

The Stock News Alert is a Python script that automatically sends stock updates for a specified stock e.g Tesla. It retrieves the stock data using the Alpha Vantage API and checks for significant changes in the stock price. If the difference exceeds 3%, it fetches relevant news articles using the News API and sends them along with the stock update.

## Usage

1. Sign up for an account and obtain an API key from the [Alpha Vantage API](https://www.alphavantage.co) and the [News API](https://newsapi.org).
2. Replace `"YOUR STOCK API ACCOUNT"` with your actual Alpha Vantage API key in the code.
3. Replace `"YOUR NEWS API KEY"` with your actual News API key in the code.
4. Set up a Telegram bot and obtain the bot token ID and the chat ID of the recipient. Refer to the [Telegram Bot Setup](#telegram-bot-setup) section below for instructions.
5. Install the required dependencies by running the following command:

```bash
pip install requests
```

6. Run the script using Python:

```bash
python stock_news_alert.py
```

The script will automatically fetch the latest stock data for Tesla Inc and compare it with the previous day's closing price. If the difference exceeds 3%, it will fetch relevant news articles about the company and send them, along with the stock update, to the specified Telegram chat.

## Dependencies

The Tesla Stock Update Telegram Bot relies on the `requests` library to make HTTP requests to the Alpha Vantage API and the News API. Install the required dependency by running the following command:

```bash
pip install requests
```

## Telegram Bot Setup

To use the Tesla Stock Update Telegram Bot, you need to set up a Telegram bot and obtain the bot token ID and the chat ID of the recipient. Here are the general steps to set up a Telegram bot:

1. Start a chat with the [BotFather](https://core.telegram.org/bots#6-botfather) on Telegram.
2. Follow the instructions to create a new bot and obtain the bot token ID.
3. To obtain the chat ID of the recipient, you can either use the `get_updates` method in the code (uncomment the relevant line and run the script) or search online for methods to obtain the chat ID programmatically.

