#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import os
import time
from datetime import date, timedelta
import requests
from dotenv import load_dotenv
from twilio.rest import Client

#stock news notificator.

#https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1

load_dotenv()

tickers = ["MXL","GE","AVGO"]

yesterday = date.today() - timedelta(days=1)
pre_yesterday = date.today() - timedelta(days=2)
tiingo_token = os.environ.get("TIINGO_TOKEN")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_TOKEN")
marketaux_token = os.environ.get("MARKETAUX_TOKEN")

def send_message(news):
    client = Client(twilio_sid, twilio_token)
    message = client.messages.create(from_=os.environ.get("TWILIO_FROM_NUMBER"),
                                     body='Stocks update for today! ' + news[:171],##arbitrary value I set to not get errors with twillio free account and msg length
                                     to=os.environ.get("MY_NUMBER"))
    if message.error_message:
        print(message.error_message)
    else:
        print(f"Message sent!, status: {message.status}, id: {message.sid}")

def get_news(ticker):
    time.sleep(1)
    response = requests.get(f"https://api.marketaux.com/v1/news/all?symbols={ticker}&filter_entities=true&language=en&api_token={marketaux_token}")
    return f"News: {response.json()["data"][0]["title"]}: {response.json()["data"][0]["description"]}"

def evaluate_stock(pre_yesterday_close, yesterday_close, ticker):
    news = get_news(ticker)
    if pre_yesterday_close > yesterday_close:
        send_message(f"{ticker}: Opening at: {yesterday_close}. Value went down, {news}")
    elif yesterday_close > pre_yesterday_close:
        send_message(f"{ticker}: Opening at: {yesterday_close}. Value went up, {news}")
    elif yesterday_close == pre_yesterday_close:
        send_message(f"{ticker}: Opening at: {yesterday_close}. Price stayed the same, {news}")

for ticker in tickers:
    time.sleep(3)
    response = requests.get(
        f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={pre_yesterday}&endDate={yesterday}&token={tiingo_token}")
    time.sleep(1)
    evaluate_stock(response.json()[0]["close"], response.json()[1]["close"], ticker)

