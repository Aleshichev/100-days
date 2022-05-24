import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "95aa49ec4e86d6b1b1149a73458cdafa"
account_sid = "AC80549d7af691ed52c46420ba5ba55778"
auth_token = "a33a4b8de04cd9a7b26b0fad5b629999"

params = {
    "lat": 47.809490,
    "lon": 13.055010,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code =(hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              from_='+19362377794',
                              body='Hello',
                              to='+380989750736'
                          )

    print(message.status)
# print(weather_data["hourly"][0]["weather"][0]['id'])

