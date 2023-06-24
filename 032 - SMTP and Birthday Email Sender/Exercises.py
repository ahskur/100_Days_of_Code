# import smtplib
#
# # Using Ethereal SMTP service to test this code
# # Save generated email and password to variables
# my_email = "michel.carter29@ethereal.email"
# my_password = "MrmhqWCzUZjGWSWpzv"
#
# # Set connection smtp server, port and protocol?
# with smtplib.SMTP("smtp.ethereal.email", 587, 'tls') as connection:
#     # Secure connection
#     connection.starttls()
#     # Login using credentials
#     connection.login(user=my_email, password=my_password)
#     # Set from and to addresses and also msg subject and body
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello, Michael!\n\n"
#                                                                                            "This is the body of my "
#                                                                                            "email, can you read it?")
#     # You can avoid using close() if you open the connection just like a file
#     # connection.close()

import datetime as dt
# Tap into to module, then to the class with the same name]
time_now = dt.datetime.now()
# And we can then tap into specific attributes
year = time_now.year
if year == 2023:
    print("Ohayo!")
# There are a lot of attributes you can get hold of using datetime
day_of_week = time_now.weekday()
print(day_of_week)

# It also let us set a variable using datetime, like a birthday
# And we can specify a lot of things inside datetime too
birthday_Josh = dt.datetime(year=1995,month=12,day=15) # If time not specified, then it's the default value of 00:00:00
print(birthday_Josh)