import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 178
AGE = 20

APP_ID = "1805b3ba"
API_KEY ="3b2c3ee45892199364c4c9de26fa4b78"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result["exercises"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post("https://api.sheety.co/a17b64cd7979705e6f55de1edeec7121/myWorkouts/workouts", json=sheet_inputs)

    print(sheet_response.text)