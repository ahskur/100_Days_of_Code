# Fitness Tracker

The Fitness Tracker is a Python script that integrates with the Nutritionix API and the Sheety API to track and log exercise data in a Google Sheets spreadsheet. It allows users to input their exercise details, such as the exercise performed, duration, and calories burned, and stores the data in a structured format for easy tracking and analysis.


## Setup

1. Sign up for an account and obtain the necessary API credentials:
   - [Nutritionix](https://www.nutritionix.com/business/api) API App ID and API Key.
   - [Sheety](https://sheety.co/) API Access Token.

2. Clone the repository and navigate to the project directory.

3. Install the required dependencies by running the following command:

```bash
pip install requests
```

4. Rename the `.env.example` file to `.env` and replace the placeholder values with your actual API credentials.

## Usage

1. Run the script using Python:

```bash
python fitness_tracker.py
```

2. Follow the prompt to enter the exercise details for the day, including the exercise performed and the duration.

3. The script will send the exercise data to the Nutritionix API's Natural Language endpoint and retrieve the calculated calories burned.

4. The exercise data, including the date, time, exercise, duration, and calories burned, will be logged in a Google Sheets spreadsheet using the Sheety API.

5. Check the console output for the response status of the API requests and any error messages.

## Dependencies

The Fitness Tracker script relies on the `requests` library to make HTTP requests to the Nutritionix API and the Sheety API. Install the required dependency by running the following command:

```bash
pip install requests
```

## Disclaimer

Please note that the Fitness Tracker script is provided as-is, without any warranty or guarantee of its functionality or suitability for any purpose. Use it responsibly and in compliance with the terms and conditions of the Nutritionix API and the Sheety API.
