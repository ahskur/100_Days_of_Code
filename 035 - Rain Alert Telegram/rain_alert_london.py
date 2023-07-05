import requests
import asyncio
import telegram


# --- TELEGRAM BOT --- #
BOT = "YOUR BOT TOKEN ID GOES HERE"


async def send_message():
    bot = telegram.Bot(BOT)
    async with bot:
        # Print to manually get user_id
        # print((await bot.get_updates())[0])
        await bot.send_message(text="It's going to rain, take an umbrella with you!", chat_id="THE PERSON YOU WANT TO SEND TO GOES HERE")

# --- API Calls --- #
api_forecast: str
api_forecast = "YOUR OPEN WEATHER API KEY GOES HERE"
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
REQUEST_PARAMETERS = {
    # Latitude and Longitude for London
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_forecast,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "lang": "en_us",
}

# Using the endpoint, ask for a 'response' using the given parameters
response = requests.get(url=api_endpoint, params=REQUEST_PARAMETERS)
# Raise a flag if there is any status different then 2xx
response.raise_for_status()
# Save to a variable
weather_data = response.json()

# Set bool flag to be flipped if weather forecast shows rain
gonna_rain = False

# Now get a hold of the specific ID of each hourly weather prediction
# by tapping into a dictionary, and lists multiple times
# print(weather_data["hourly"][0]["weather"][0]["id"])
# This was made by using a JSON viewer to help visualise where is the value we want
# Now we get a 'slice', by tapping into index 0 to index 12 of the initial weather data list
weather_slice = weather_data["hourly"][:12]
# Loop trough each index (0 to 12) and get weather condition (ID) for each one of the hours/indexes
# then save to a var
for hourly_data in weather_slice:
    condition_code = (hourly_data["weather"][0]["id"])
    if int(condition_code) < 700:
        # Flip flag
        gonna_rain = True
        print("Going to rain, let's send messages!")

# If true, print and send message through a Telegram Bot
if gonna_rain:
    print("Going to rain, bring an Umbrella ella ella eeeh eeh eeh eh")
    asyncio.run(send_message())

# Debug print for json data
# print(weather_data["hourly"][0]["weather"][0]["id"])
# print(weather_data)
