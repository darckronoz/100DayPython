#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import json
from datetime import date
from typing import Optional
import os
from dotenv import load_dotenv
from attr import dataclass
import requests

load_dotenv()

#Workout tracker with google sheets.
exercise = input("What did you do today. \n")

#process the exercise to extrac and map into
@dataclass
class WorkoutLog:
    #not all are required, some can be missing for 1 log, if I say I run 10km today, it would be just name, quantity, units and date (date is always the day of the log)
    name: str #Running, pullups, dips, the exercise name.
    quantity: float #a number can be 30 km, 10 pullups and the number will be 30 or 10 km and pullups would be the unit.
    units: str #km if was runing or cycling, lb or kg if it was weigths, reps if it was reps.
    series: Optional[str] = "-"#how many times the exercise was performed.
    effort: Optional[int] = 0 #from 1 to 10 how challenging
    workout_date: Optional[str] = date.today().strftime("%Y/%m/%d") #always the date of the log

#here goes the logic that converts the user input into WorkoutLog structure

llm_headers = {
    "Authorization": f"Bearer {os.environ.get('OPEN_ROUTER_AI')}",
    "Content-Type": "application/json"
}
#aqui uso openrouter/free para que me seleccione un modelo gratis ya que la tarea es sencilla.
#despues de usar openrouter/free vi que el modelo que mejor respondia era el de nvidia entonces solo lo puse y ya
llm_body = {
    "model": "nvidia/nemotron-3-super-120b-a12b-20230311:free",
    "messages": [
    #este prompt puede ser mejorado mucho para obtener una mejor respuesta y mas consistente.
      {"role": "user", "content": f"Extract name, quantity, units series and effort from this user input '{exercise}' using the json schema given"},
    ],
    "provider": {
        "require_parameters": True
      },
    "structured_outputs": True,
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "workout_log",
        "strict": True,
        "schema": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the exercise, like cycling, running, pullups, press bank etc...",
            },
            "quantity": {
              "type": "number",
              "description": "A number representing the quantity of the exercise performed, if the user says ran 30 km quantity would be 30",
            },
            "units": {
              "type": "string",
              "description": "string that represents the units of the quantity, km, reps, etc...",
            },
            "series": {
              "type": "string",
              "description": "just how many times the exercise was performed. infer as 1 if the use does not specify",
            },
            "effort": {
              "type": "number",
              "description": "only 1 to 10. 1 being super easy 10 super hard",#aqui me da negativos por alguna razon jaja
            },
          },
          "required": ["name", "quantity", "units", "series", "effort"],
          "additionalProperties": False,
        },
      },
    },
  }

llm_response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=llm_headers, json=llm_body)
data = llm_response.json()
try:
    print(data['choices'][0]['message']['content'])

    bearer = os.environ.get("SHEETY_BEARER")
    workout_log = json.loads(data['choices'][0]['message']['content'])
    sheet_headers = {"Authorization": f"{bearer}"}
    sheet_body = {
        "workout": {
            "name": workout_log["name"],
            "quantity": workout_log["quantity"],
            "units": workout_log["units"],
            "series": workout_log["series"],
            "effort": workout_log["effort"],
            "workoutDate": date.today().strftime("%Y/%m/%d")
        }
    }

    response = requests.post("https://api.sheety.co/f6c04f152153d8edd0213d6fb9e62629/workoutlogPy/workouts",
                             headers=sheet_headers, json=sheet_body)

    if response.status_code == 200:
        print(f"Workout saved! :{response.json()}")
    else:
        print(f"Error saving workout :{response.json()}")
# este catch se come muchas excepciones utiles. toca cambiarlo
except AttributeError as e:
    print("error parseando el input del usuario: ", e)
    print(llm_response.json())

    #esta un poco maluco pero logre hacer que el flujo completo funcione :D

