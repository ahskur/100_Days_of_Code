# ISS Over London Notifier

The ISS Over London Notifier is a Python script that checks the position of the International Space Station (ISS) and the current time to determine if the ISS is over London during the nighttime. If both conditions are met, it sends an email notification using the configured SMTP email account.

## Usage

1. Update the email settings in the script by replacing `my_email` and `my_password` with your SMTP email credentials.
2. Make sure you have the required dependencies installed. You can install them by running the following command:

```bash
pip install requests
```

3. Run the script using Python:

```bash
python iss_over_london_notifier.py
```

The script will continuously check the position of the ISS and the current time every 5 minutes. If the ISS is within 5 degrees latitude and longitude of London and it is nighttime, an email notification will be sent.

## Email Settings

Before running the script, make sure to update the following email settings:

- `my_email`: Your SMTP email address.
- `my_password`: Your SMTP email password.

Please note that it is recommended to use a test email account, such as [Ethereal](https://ethereal.email), to avoid sending actual emails during development and testing. Ethereal provides a SMTP-capable inbox where you can view the sent messages.

## Dependencies

The ISS Over London Notifier script relies on the following dependencies:

- `requests`: Allows making HTTP requests to retrieve data from APIs.
- `datetime`: Provides the functionality to work with dates and times.
- `smtplib`: Enables sending emails using the SMTP protocol.
- `time`: Provides functions for time-related operations.

Install the required dependencies by running the following command:

```bash
pip install requests
```

Stay informed about the International Space Station's position over London with the ISS Over London Notifier. Enjoy the awe-inspiring sight of the ISS passing by and share the excitement with your friends and family. Happy coding!