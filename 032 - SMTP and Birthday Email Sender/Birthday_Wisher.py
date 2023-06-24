import smtplib
import random
import datetime as dt
import pandas

# You can use https://ethereal.email to create a SMTP-capable inbox to test this code and more Remember that if
# sending messages through SMTP then no message is actually delivered, all messages are caught, and you can see these
# in the Messages page.

# --- Email Settings --- #
my_email = "michel.carter29@ethereal.email"
my_password = "MrmhqWCzUZjGWSWpzv"

# --- Time to check for birthday --- #
what_time_is_it = dt.datetime.now()
todays_day = what_time_is_it.day
todays_month = what_time_is_it.month
# Create a tuple for today's date
today = (todays_month, todays_day)

# Debug print for day and month
# print(todays_day, todays_month)

# Now open the csv with the birthdays and compare if today's date has a match with someone's birthday
birthday_data = pandas.read_csv("birthdays.csv")
# Debug print
# print(birthday_data["month"])
# print(birthday_data["day"])
# Save birthdays as dictionary
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

# Check if today's date tuple is in the birthday dictionary
for today in birthdays_dict:
    # Save the name of the person that had a match inside a new variable
    birthday_person = birthdays_dict[today]
    # If tuple is in the dictionary, pick a random letter from the folder
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # Read the letter to change name inside
    with open(file_path) as letter_file:
        # Save letter contents to a var
        letter_contents = letter_file.read()
        # Update this variable with new information
        letter_contents = letter_contents.replace("[NAME]", birthday_person["name"])

    # Now send the new letter using smtplib
    with smtplib.SMTP("smtp.ethereal.email", 587, 'tls') as connection:
        # Secure connection
        connection.starttls()
        # Login using credentials
        connection.login(user=my_email, password=my_password)
        # Set from and to addresses and also msg subject and body
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!!!\n\n"
                                                                                       f"{letter_contents}")
