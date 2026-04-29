#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import datetime

#ISS Notifier, I guess this is supposed to run periodically.
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

iss_response = requests.get("http://api.open-notify.org/iss-now.json")

def send_email(email):
    from_adr = "GMAIL_USER"

    to_adr = email

    subject = "Notificacion ISS en tu casa."
    message = f"Quien pinto a simon bolivar en el techo?"

    mail_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    msg = f"From: {from_adr}\nTo: {to_adr}\nSubject: {subject}\nDate: {mail_date}\n\n{message}"

    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        if os.environ.get('GMAIL_USER') is not None and os.environ.get('GMAIL_PASS') is not None:
            conn.login(os.environ.get('GMAIL_USER'), os.getenv('GMAIL_PASS'))
            conn.sendmail(from_adr, to_adr, msg)
        else:
            print("Variables de entorno no encontradas. revisa el archivo .env.example y crea tu archivo .env")

if iss_response.status_code == 200:
    iss_data = iss_response.json()
    my_latitude = round(float(os.getenv("MY_LATITUDE")),2)
    my_longitude = round(float(os.getenv("MY_LONGITUDE")),2)
    iss_latitude = round(float(iss_data["iss_position"]["latitude"]), 2)
    iss_longitude = round(float(iss_data["iss_position"]["longitude"]), 2)
    if iss_latitude == my_latitude and iss_longitude == my_longitude:
        send_email("cristhianvargas.ingeniero@gmail.com")
    else:
        print(f"ISS not at your position, skipping... ISS at {iss_latitude}, {iss_longitude}")
else:
    print("error obteniendo la posicion de la estacion espacial internacional :C")


