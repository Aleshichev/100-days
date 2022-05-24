import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "95aa49ec4e86d6b1b1149a73458cdafa"
params = {
    "lat": 50.4333,
    "lon": 30.5167,
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
        will_raiin = True


if will_rain:
    print("Bring an umbrella")
# print(weather_data["hourly"][0]["weather"][0]['id'])

