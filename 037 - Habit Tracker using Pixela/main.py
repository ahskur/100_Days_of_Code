import requests
from datetime import datetime

# --- Create an account at pixe.la using the following parameters specified by pixe.la
pixela_endpoint = "https://pixe.la/v1/users"

# Define username and 'password' - You can put whatever you want but check if it's avaliable first
TOKEN = "YOUR TOKEN GOES HERE"
USERNAME = "YOU USERNAME GOES HERE"

# USER_PARAMETERS = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# Running this post() once creates an account using the given TOKEN and USERNAME - You can freely choose what to use
# response = requests.post(url=pixela_endpoint, json=USER_PARAMETERS)
# print(response.text)

# --- Graphic Endpoint --- #
# Create access to a new graph using the specified methods from the API
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# # To effectively create a new graph, it's needed a new post() request
# # SEE SPECIFIC PARAMETERS FOR THE GRAPH CREATION
# GRAPH_PARAMETERS = {
#     "id": "test1",
#     "name": "Coding Graph",
#     "unit": "Days",
#     "type": "int",
#     "color": "momiji"
# }
# # Provide HEADER to authenticate the USERNAME using the TOKEN defined at the beginning
HEADER = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=GRAPH_PARAMETERS, headers=HEADER)
# print(response.text)

# --- Post a Pixel in the Graph --- #
pixelpost_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test1"

today = datetime.now()
formated_today_date = today.strftime("%Y%m%d")
# Use strftime to format the date into a string using parameters specified by the library
# print(today.strftime("%Y%m%d"))

POST_PARAMETERS = {
    "date": formated_today_date,
    "quantity": "1",
}

# response = requests.post(url=pixelpost_endpoint, json=POST_PARAMETERS, headers=HEADER)
# print(response.text)

# --- Update Data from Graph --- #
# Update the Pixel from today using {today}
pixel_update_or_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test1/{formated_today_date}"

UPDATE_PARAMETERS = {
    "quantity": "5",
}

# response = requests.put(url=pixelupdate_or_delete_endpoint, json=UPDATE_PARAMETERS, headers=HEADER)
# print(response.text)

# -- Delete Pixel from Graph --- #
# This deletes a Pixel using TODAY'S DATE - To change date you need to manually change ther formated_today_date var
response = requests.delete(url=pixel_update_or_delete_endpoint, headers=HEADER)
print(response.text)