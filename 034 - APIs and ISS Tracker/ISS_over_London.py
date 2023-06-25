import requests
from datetime import datetime
import smtplib
import time

# --- Email Settings --- #
my_email = "michel.carter29@ethereal.email"
my_password = "MrmhqWCzUZjGWSWpzv"

# --- Starting Position - London --- #
# Set London's latitude and longitude as floating numbers
LONDON_LAT = 51.507351
LONDON_LONG = -0.127758


def check_iss_pos():
    # Use ISS API-URL to get the json and save it as data
    # Also raise status if not 200
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # From the ISS API, get from inside the json and save latitude and longitude to single variables as floats
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Compare if current position is within +5 or -5 degrees of the ISS actual position
    if LONDON_LAT - 5 <= iss_latitude <= LONDON_LAT + 5 and LONDON_LONG - 5 <= iss_longitude <= LONDON_LONG + 5:
        return True


def check_night():
    # Set Parameters to ask the Sunrise-API for
    parameters = {
        "lat": LONDON_LAT,
        "lng": LONDON_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Now save strip the important data from the json file using split() method
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get actual hour and save it to a variable
    time_now = datetime.now().hour

    # Sunrise/Sunset must be integers for this to work
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Check every 5 minutes the position of the ISS and see if it's night already
    time.sleep(300)
    # If both checks are true, then proceed sending an email
    if check_iss_pos() and check_night():
        with smtplib.SMTP("smtp.ethereal.email", 587, 'tls') as connection:
            # Secure connection
            connection.starttls()
            # Login using credentials
            connection.login(user=my_email, password=my_password)
            # Set from and to addresses and also msg subject and body
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject:ISS is over London now!\n\n"
                                    "Look up in the sky and see if you can spot the ISS over London right now! :)")
