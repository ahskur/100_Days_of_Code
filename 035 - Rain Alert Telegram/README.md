# Rain Alert Telegram Bot

The Rain Alert Telegram Bot is a Python script that checks the weather forecast using the OpenWeatherMap API for London. If rain is predicted within the next 12 hours, it sends a message through a Telegram bot to notify the specified recipient.

## Usage

1. Set up a Telegram bot by following the instructions provided in the [Telegram Bot documentation](https://core.telegram.org/bots#6-botfather).
2. Obtain the bot token ID and replace `"YOUR BOT TOKEN ID GOES HERE"` with your actual bot token ID in the code.
3. Get the API key for the OpenWeatherMap service by signing up at [https://openweathermap.org](https://openweathermap.org).
4. Replace `"YOUR API KEY GOES HERE"` with your actual OpenWeatherMap API key in the code.
5. Specify the recipient's chat ID by replacing `"THE PERSON YOU WANT TO SEND TO GOES HERE"` with the actual chat ID in the code.
6. Install the required dependencies by running the following command:

```bash
pip install requests asyncio python-telegram-bot
```

7. Run the script using Python:

```bash
python rain_alert_telegram_bot.py
```

The script will check the weather forecast for London and send a message through the specified Telegram bot if rain is predicted within the next 12 hours.

## Dependencies

The Rain Alert Telegram Bot relies on the following dependencies:

- `requests`: Allows making HTTP requests to retrieve weather forecast data from the OpenWeatherMap API.
- `asyncio`: Provides the necessary infrastructure for writing asynchronous code.
- `python-telegram-bot`: A Python wrapper for the Telegram Bot API, enabling interaction with Telegram bots.

Install the required dependencies by running the following command:

```bash
pip install requests asyncio python-telegram-bot
```

## Telegram Bot Setup

To use the Rain Alert Telegram Bot, you need to set up a Telegram bot and obtain the bot token ID and the chat ID of the recipient. Here are the general steps to set up a Telegram bot:

1. Start a chat with the [BotFather](https://core.telegram.org/bots#6-botfather) on Telegram.
2. Follow the instructions to create a new bot and obtain the bot token ID.
3. To obtain the chat ID of the recipient, you can either use the `get_updates` method in the code (uncomment the relevant line and run the script) or search online for methods to obtain the chat ID programmatically.


Stay prepared for rain with the Rain Alert Telegram Bot. Receive timely notifications about upcoming rain in London and make sure to bring an umbrella!