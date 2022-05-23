import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.456542
MY_LONG = 30.530037
MY_EMAIL = "Aleshichevigor@outlook.com"
PASSWORD = "45rhfy7853rt"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    # iss_position = (longitude, latitude)
    # print(iss_position)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5<= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])     #достаём конкретный час
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])      #достаём конкретный час
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()  # защита письма
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look up\n\nThe ISS is above you in the sky")


