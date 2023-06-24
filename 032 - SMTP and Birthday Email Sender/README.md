# Birthday Email Sender

The Birthday Email Sender is a Python script that automatically sends birthday emails to individuals based on the information provided in a CSV file. It utilizes the SMTP protocol to send the emails through a configured email account.

## Usage

1. Prepare a CSV file named `birthdays.csv` with the following columns: `name`, `email`, `month`, `day`. This file should contain the names, email addresses, and birthdays (month and day) of the recipients.
2. Create letter templates in the `letter_templates/` directory. The templates should be text files containing the content of the email to be sent. Use the placeholder `[NAME]` in the template to dynamically replace it with the recipient's name.
3. Update the email settings in the script by replacing `my_email` and `my_password` with your SMTP email credentials.
4. Make sure you have the required dependencies installed. You can install them by running the following command:

```bash
pip install pandas
```

5. Run the script using Python:

```bash
python birthday_email_sender.py
```

The script will check if any birthdays match the current date and send personalized birthday emails using the letter templates.

## Email Settings

Before running the script, make sure to update the following email settings:

- `my_email`: Your SMTP email address.
- `my_password`: Your SMTP email password.

Please note that it is recommended to use a test email account, such as [Ethereal](https://ethereal.email), to avoid sending actual emails during development and testing. Ethereal provides a SMTP-capable inbox where you can view the caught messages.

## Letter Templates

Create personalized letter templates in the `letter_templates/` directory. These templates will serve as the content of the birthday emails. 
Use plain text files and include the desired message. To personalize the emails, use the placeholder `[NAME]` in the template. This placeholder will be replaced with the recipient's name when sending the email.

## Dependencies

The Birthday Email Sender script relies on the following dependencies:

- `smtplib`: Allows sending emails using the SMTP protocol.
- `random`: Enables selecting a random letter template.
- `datetime`: Provides the functionality to determine the current date and compare it with birthdays.
- `pandas`: Simplifies reading and manipulating data from CSV files.

Install the required dependencies by running the following command:

```bash
pip install pandas
```

