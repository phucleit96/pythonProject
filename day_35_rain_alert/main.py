import requests
import os
from twilio.rest import Client


# def telegram_bot_send_text(bot_message):
#     bot_token = os.environ.get("BOT_TOKEN")
#     bot_chatID = os.environ.get("BOT_CHATID")
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
#                 + '&parse_mode=Markdown&text=' + bot_message
#
#     bot_response = requests.get(send_text)
#     return bot_response.json()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 21.027763, # 25.281940
    "lon": 105.834160, # 110.278084
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=parameters)
# response = requests.get(WEATHER_API, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:48]
will_rain = False
#list / dict slicing to get the weather id, in the doc code id < 700 = likely to rain and snow
for hour_data in weather_slice:
    condition_data = hour_data["weather"][0]['id']
    if int(condition_data) < 700:
        will_rain = True

if will_rain:
    # message = "🌧 It's going to rain today, bring an umbrella with you."
    # telegram_bot_send_text(message)
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Sắp mưa đâấy, ra ngoài nhớ mang ô nhé! =))",
        from_='+14406933851',
        to='+84329608767'
    )
    print(message.status)

