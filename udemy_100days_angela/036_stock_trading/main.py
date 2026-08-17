import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import smtplib as smtp
from email.message import EmailMessage


load_dotenv()


STOCK = 'TSLA'
STOCK_API = 'https://www.alphavantage.co/query'
STOCK_API_KEY = os.getenv('AV_KEY')
STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY
}


COMPANY_NAME = 'Tesla Inc'
NEWS_API = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = os.getenv('NEWS_KEY')
NEWS_PARAMS = {
    'apiKey': NEWS_API_KEY,
    'q': f'{COMPANY_NAME} OR {STOCK}', 
    'from': datetime.now().date() - timedelta(days=2),
    'to': datetime.now().date(),
    'sortBy': 'popularity',
    'pageSize': 3
}


SENDER_EMAIL = os.getenv('WORK_GMAIL_UN')
SENDER_EMAIL_PW = os.getenv('WORK_GMAIL_APP_PW')
RECIPIENT_EMAIL = os.getenv('PERSONAL_GMAIL_UN')


# Created a function that will get the latest business close date since stock market only trades on weekdays
def get_latest_close_date() -> datetime:
    """Gets the latest business close date. If it is the weekend, it will return Friday."""
    today = datetime.now().date()
    if today.weekday() < 5:
        latest_close_date = today
    else:
        days_back = (today.weekday() - 4) % 7
        latest_close_date = today - timedelta(days=days_back)
    return latest_close_date


# Setting the stock close dates
LATEST_CLOSE_DATE = get_latest_close_date()
PREVIOUS_CLOSE_DATE = LATEST_CLOSE_DATE - timedelta(days=1)


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
     and return the direction and percent change as tuple."""
    difference = round(data[0]-data[1], 2)
    percent_change = round(difference / data[1], 2)
    if difference > 0:
        direction = '🔺'
    else: direction = '🔻'
    return (direction, abs(percent_change))


def get_top_headlines(url: str, params: dict) -> list:
    """Gets the top 3 headlines for the company holding the specific tracked stock 
    and returns it in a list of dicts."""
    news_response = requests.get(url=url, params=params)
    news_response.raise_for_status()
    news_data = [{
        'title': article['title'], 
        'description': article['description'], 
        'url': article['url']
        } for article in news_response.json()['articles']
        ]
    return news_data


# Twilio don't offer free trials in PH 🤡, so I'll be sending the news in email instead
def construct_news_email(stock: str, closing_difference: tuple, news: dict) -> EmailMessage:
    """Construct the news email alert for the tracked stock and return it as an EmailMessage object."""
    email_msg = EmailMessage()
    email_msg['From'] = SENDER_EMAIL
    email_msg['To'] = RECIPIENT_EMAIL
    email_msg['Subject'] = f'{stock} {closing_difference[0]} by {closing_difference[1]}'
    email_msg.set_content(f'Headline: {news['title']}\n{news['description']}\n{news['url']}')
    return email_msg


def send_news_email(msg: EmailMessage) -> None:
    """Sends the news articles about the tracked stock/company to email."""
    with smtp.SMTP(host='smtp.gmail.com', port=587, timeout=10) as conn:
        conn.starttls()
        conn.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PW)
        conn.send_message(msg=msg)


# Main program
print(f'Getting {STOCK} stock prices ...')
stock_data = get_latest_stock_close_volumes(url=STOCK_API, params=STOCK_PARAMS)
closing_difference = get_closing_difference(data=stock_data)

print(f'Gathering top news articles about {STOCK} and {COMPANY_NAME} ...')
news = get_top_headlines(url=NEWS_API, params=NEWS_PARAMS)

print(f'Sending news articles to {RECIPIENT_EMAIL} ...')
for article in news:
    email_msg = construct_news_email(stock=STOCK, closing_difference=closing_difference, news=article)
    send_news_email(msg=email_msg)

print(f"DONE! Top headlines regarding {STOCK} were sent to {RECIPIENT_EMAIL}.")

