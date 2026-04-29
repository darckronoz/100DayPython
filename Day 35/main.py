#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import os

#rain alert app with notifications using twilio.
#Este codigo se ejecutaria todas las mananas a cierta hora.
#Pero como estoy haciendo esto rapido pues aqui queda jaja.

from twilio.rest import Client

import requests
from dotenv import load_dotenv
load_dotenv()

latitude = os.environ.get("MY_LATITUDE")
longitude = os.environ.get("MY_LONGITUDE")
api_key = os.environ.get("WEATER_KEY")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_TOKEN")

def send_message(description):
    client = Client(twilio_sid, twilio_token)
    message = client.messages.create(from_=os.environ.get("TWILIO_FROM_NUMBER"),
                                     body='Va a llover muchacho, lleva sombrilla: ' + description,
                                     to=os.environ.get("MY_NUMBER"))
    if message.error_message:
        print(message.error_message)
    else:
        print(f"Message sent!, status: {message.status}, id: {message.sid}")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]
    if weather["main"] == "Rain":
        send_message(weather["description"])
    else:
        print("Not raining, skipping message...")

