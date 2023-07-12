import requests

## TODO
# Automate Telegram Bot to automatically send stock updates for Tesla Inc

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# --- Stock API Calls --- #
# Define var type
stock_api_key: str
# Set API key as var
stock_api_key = "YOUR STOCK API ACCOUNT"
# Set API Endpoint as var
stock_api_endpoint = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

# Now using the Endpoint, ask for a response using the given parameters
response_stock = requests.get(url=stock_api_endpoint, params=STOCK_PARAMETERS)
# Raise flag if status != 2xx:
response_stock.raise_for_status()
# Save data to var # -> using a JSON Viewer to get to the dictionary key we want
tsla_data = response_stock.json()["Time Series (Daily)"]
# print(tsla_data)

# Transform to list using list comprehension
tsla_data_list = [value for (key, value) in tsla_data.items()]
# Save the first item of the list which is data of yesterday to a var
yesterday_data = tsla_data_list[0]
# Save the closing price by tapping into the dictionary with '4. close'
yesterday_data_closing_price = yesterday_data['4. close']
print(yesterday_data_closing_price)

# Get day before yesterday data to compare both
day_before_yesterday_data = tsla_data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_data_closing_price)

# Find difference between the 2 days - and also transform them to floats bc they're strings
# And using abs() to help getting the absolute value, without signal
difference = abs(float(yesterday_data_closing_price) - float(day_before_yesterday_data_closing_price))
print(difference)

# Calculate percentage using difference/closing_price times 100
diff_percent = (difference / float(yesterday_data_closing_price)) * 100
print(diff_percent)

# Set flag for getting news about the stock if difference bigger than 3% in comparison to last day
if diff_percent > 3:
    print("Get news!")
    # If flag passes, then get news about the Stock from another API
    # --- NEWS API CALLS --- #
    # Define var type
    news_api_key: str
    # Set API key as var
    news_api_key = "YOUR NEWS API KEY"
    # Set API Endpoint as var
    news_api_endpoint = "https://newsapi.org/v2/everything"
    NEWS_PARAMETERS = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apiKey": news_api_key,
    }
    response_news = requests.get(url=news_api_endpoint, params=NEWS_PARAMETERS)
    response_news.raise_for_status()
    news_data = response_news.json()["articles"]
    # Get hold of only the first 3 articles with the company name
    newest_three = news_data[:3]
    print(newest_three)
    # Organize and format message to be sent
    # Using list comprehension
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          newest_three]
    print(formatted_articles)
