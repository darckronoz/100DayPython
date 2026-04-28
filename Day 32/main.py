#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import datetime
#auto happy birthday mail app
#mi version es para escribir correos cobrando el spotify familiar B)
import smtplib
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

from_adr = "GMAIL_USER"

emails_df = pd.read_csv("mails.csv")

emails_dict = dict(zip(emails_df["email"], emails_df["value"]))

for email in emails_dict.keys():
    to_adr = email

    subject = "Recordatorio pago spotify"
    message = f"Buenos dias mi estimado(a). \n la presente es para recordarle el pago del spotify,\n tu deuda actual es de ${emails_dict[email]}\n\n\n\n\n paga pls :D"

    mail_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    msg = f"From: {from_adr}\nTo: {to_adr}\nSubject: {subject}\nDate: {mail_date}\n\n{message}"

    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        if os.environ.get('GMAIL_USER') is not None and os.environ.get('GMAIL_PASS') is not None:
            conn.login(os.environ.get('GMAIL_USER'), os.getenv('GMAIL_PASS'))
            conn.sendmail(from_adr, to_adr, msg)
        else:
            print("Variables de entorno no encontradas. revisa el archivo .env.example y crea tu archivo .env")
