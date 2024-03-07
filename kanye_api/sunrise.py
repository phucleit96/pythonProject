import requests
from datetime import datetime, timezone
MY_LAT = 21.027763
MY_LONG = 105.834160
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]['sunrise'].split("T")[1].split(":")[0]
sunset = data["results"]['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now(timezone.utc)
print(f"Time for sunrise UTC: {sunrise}")
print(F"Time for sunset UTC: {sunset}")
print(f"Time now UTC: {time_now.hour}")


