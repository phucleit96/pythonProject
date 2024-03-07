import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
GENDER = "male"
WEIGHT_KG = 91.0
HEIGHT_CM = 186.00
AGE = 27
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What exercise did you do: ")
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
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
print(result)

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
# sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
bearer_headers = {
    "Authorization": os.environ["BEARER_TOKEN"]
}
sheet_response = requests.post(
    sheety_endpoint,
    json=sheet_inputs,
    # auth=(
    #     os.environ['USER_NAME'],
    #     os.environ['PASS'],
    headers=bearer_headers
    )

print(sheet_response.text)
# sheet_put_endpoint = "https://api.sheety.co/e9748e03f6c21cfa6ea571685ed76cb7/phuc'sWorkout/workouts/10"
# sheet_put_json = {
#     "workout": {
#         "exercise": "Swimming",
#         "duration": 99.99,
#         "calories": 999.99
#     }
# }
# sheet_put_response = requests.put(sheet_put_endpoint, json=sheet_put_json, headers=bearer_headers)
# print(sheet_put_response.text)
# sheet_del_endpoint = "https://api.sheety.co/e9748e03f6c21cfa6ea571685ed76cb7/phuc'sWorkout/workouts/10"
# sheet_del_response = requests.delete(sheet_del_endpoint, headers=bearer_headers)
# print(sheet_del_response.text)