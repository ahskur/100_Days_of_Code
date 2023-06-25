import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# iss_dict = response.json()["iss_position"]
# iss_longitude = response.json()["iss_position"]["longitude"]
# iss_latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (iss_longitude,iss_latitude)
#
# print(iss_position)

# # Get Quotes from App Brewery's API Kanye Rest - which sucks.
# get_quote = requests.get(url="https://api.kanye.rest")
# get_quote.raise_for_status()
# # After getting 'ok' from the URL, we save the data in json and get the value for the quote
# # and print it as a plain quote
# plain_quote = get_quote.json()["quote"]
# print(plain_quote)

# --- API Exercises --- #

# Put 'London' position for latitude and longitude
parameters_dict = {
    "lat": 51.507351,
    "long": -0.1278758,
    "formatted":0,
}

sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters_dict)
sunrise_sunset.raise_for_status()
API_response = sunrise_sunset.json()

sunrise = API_response["results"]["sunrise"]
sunset = API_response["results"]["sunset"]

print("Sunrise:",sunrise,
      "\n""Sunset:",sunset)

time_sunrise = sunrise.split("T")[1].split(":")[0]
time_sunset = sunset.split("T")[1].split(":")[0]

print("Sunrise hour: ",time_sunrise,
      "\n","Sunset hour:",time_sunset)

current_time = dt.datetime.now()
print(current_time.hour)
