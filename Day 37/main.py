#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import datetime
#habit tracker using pixela

import os
from dotenv import load_dotenv
import requests

load_dotenv()

pixela_password = os.environ.get("PIXELA_TOKEN")
username = "darckronoz"

#create user:
# body = {
#     "token": pixela_password,
#     "username": username,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# user_response = requests.post("https://pixe.la/v1/users", json=body)

#create graph:
headers = {
    "X-USER-TOKEN": pixela_password
}

# body = {
#     "id": "creatine",
#     "name": "Daily Creatine Intake",
#     "unit": "Scooops",
#     "type": "int",
#     "color": "sora",
# }
#
# graph_response = requests.post(f"https://pixe.la/v1/users/{username}/graphs", json=body, headers=headers)

#Create a point in the graph

scoops = input("Cuanta creatina tomaste?? 🥵🥵 \n")
date = datetime.datetime.now().strftime("%Y%m%d")

body = {
    "date": date,
    "quantity": scoops,
}

response = requests.post(f"https://pixe.la/v1/users/{username}/graphs/creatine", headers=headers, json=body)
print(response.json())