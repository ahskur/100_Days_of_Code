import requests
from datetime import datetime as dt
import os

N_APP_ID = os.environ.get("N_APP_ID", "API AppId not found")
N_APP_KEY = os.environ.get("N_APP_KEY", "API AppKey not found")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH", "Sheety API Access not found")

# --- Nutritionix API Access and Natural Language API Access --- #
HTTP_HEADERS = {
    "x-app-id": N_APP_ID,
    "x-app-key": N_APP_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_exercise = input("What exercise did you do today and for how long?\n")
query = {
    'query': user_exercise,
}

user_query = requests.post(url=exercise_endpoint, json=query, headers=HTTP_HEADERS)
# As soon as the user data is sent, save what comes back from the Natural Language model as .json to access it later
user_data = user_query.json()
print(user_data)

# --- Sheety for Google Sheets API Use --- #
current_day = dt.today()
time = current_day.strftime("%H:%M")
day = current_day.strftime("%d/%m/%Y")
print(day, "\n", time)

SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH,
}
# Set Sheet-Specific Endpoint
sheety_endpoint = "https://api.sheety.co/f1b981216bb94377308e85ae4ded476a/day38WorkoutSheet/workouts"

# Loop trough user data to fetch exercise, duration, and calories inside a dict for each exercise given
for each_exercise in user_data['exercises']:
    # Parameters to be add to the sheet
    NEW_ROW = {
        "workout": {
            "date": day,
            "time": time,
            "exercise": each_exercise["user_input"].title(),
            "duration": each_exercise["duration_min"],
            "calories": each_exercise["nf_calories"],
        }
    }
    insert_new_row = requests.post(url=sheety_endpoint, json=NEW_ROW, headers=SHEETY_HEADER)
    print(insert_new_row.text)