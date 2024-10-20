import requests
from datetime import datetime
import smtplib
import time
my_longitude = 76.955833
my_latitude = 11.016844
my_email = "hackersiva847@gmail.com"
password = "ccnffohqpwivwijz"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()


def is_iss_overhead():
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if my_latitude-5 <= latitude <= my_latitude+5 and my_longitude-5 <= longitude <= my_longitude+5:
        return True

def is_night():
    parameter = {
        "lat" : my_latitude,
        "lng" : my_longitude,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data= response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_DT = sunrise.split("T")[1]
    sunrise_HR = int(sunrise_DT.split(":")[0])
    sunset_DT = sunset.split("T")[1]
    sunset_HR = int(sunset_DT.split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset_HR or time_now <= sunrise_HR:
        return True
while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="sivam4266@gmail.com",
                msg="subject:Look up ☝️\n\nThe ISS is above you in the sky."
            )