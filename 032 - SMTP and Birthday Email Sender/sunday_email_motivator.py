# This program aims to check if the day is Sunday, and if it is, sends a motivational email
import datetime as dt
import smtplib
import random

my_email = "michel.carter29@ethereal.email"
my_password = "MrmhqWCzUZjGWSWpzv"

# Get a hold of time at current/present moment
time_now = dt.datetime.now()
# Save the weekday to a new var
what_day_is = time_now.weekday()

# Debug print
print(what_day_is)
# Why Sunday is the fifth day of the week tho? Anyways...
# If the day == 5, then is motivational email time!!!!!!!!!
if what_day_is == 5:
    print("Damn, time for Sunday quotes already!?")
    with open("quotes.txt") as quotes:
        # Save quotes from txt to a list
        all_quotes = quotes.readlines()
        # Get a random one
        random_quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.ethereal.email", 587, 'tls') as connection:
        # Secure connection
        connection.starttls()
        # Login using credentials
        connection.login(user=my_email, password=my_password)
        # Set from and to addresses and also msg subject and body
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Sunday Motivational Quote, Michael!\n\n"
                                                                       f" {random_quote}")

