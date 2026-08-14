import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()


COMPANY_NAME = 'Tesla Inc'


STOCK = 'TSLA'
LATEST_CLOSE_DATE = datetime.now().date() - timedelta(days=1)
PREVIOUS_CLOSE_DATE = LATEST_CLOSE_DATE - timedelta(days=1)
STOCK_API = 'https://www.alphavantage.co/query'
STOCK_API_KEY = os.getenv('AV_KEY')
STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY
}


def get_latest_stock_close_volumes(url: str, params: dict) -> tuple:
    """Gets the closing stock price for yesterday and the day before, 
    and return the values as a tuple."""
    stock_response = requests.get(url=url, params=params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    latest_closing_data = (
        float(stock_data[str(LATEST_CLOSE_DATE)]['4. close']), 
        float(stock_data[str(PREVIOUS_CLOSE_DATE)]['4. close'])
    )
    return latest_closing_data


def get_closing_difference(data: tuple) -> tuple:
    """Gets the difference between yesterday and day before closing stock prices, 
     and return the direction and value as tuple."""
    difference = round(data[0]-data[1], 2)
    if difference > 0:
        direction = 'up'
    else: direction = 'down'
    return (direction, abs(difference))


data = get_latest_stock_close_volumes(url=STOCK_API, params=STOCK_PARAMS)
print(data)
print(get_closing_difference(data=data))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

