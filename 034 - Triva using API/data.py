import requests

# Setting parameters to ask the API
parameters = {
    "amount": 10,
    "type": "boolean",
    "category":18,
}

# Using API request to get data from the site using parameters
# First check if the response code is 2xx
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data = (data["results"])
