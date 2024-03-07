import requests
from datetime import datetime, timezone
import smtplib
import time

my_email = "moonknight196@gmail.com"
password = "qrqmazreuirftjlo"
MY_LAT = float(21.004263) # Your latitude
MY_LONG = float(105.831442) # Your longitude

def check_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#Function to test if it is night time or day time:


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour
    if time_now >= sunset or time_now <= sunrise:
        return True
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    # Wait for 60 seconds, slow it down!
    time.sleep(60)
    if check_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="phuc.le.it96@gmail.com",
                msg=f"Subject: ISS OverHead Notifier\n\nPlease look up, the ISS "
                    f"is up on the sky and it is near the location!"
            )



