import time

import requests
from datetime import datetime
import smtplib

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

MY_LAT = 9.081999
MY_LONG = 8.675277

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT >= iss_latitude - 5 and MY_LAT <= iss_latitude + 5) and (MY_LONG >= iss_longitude - 5 and MY_LONG <= iss_longitude + 5):
        return True

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

    time_now = datetime.now()

    if time_now.hour < sunrise and time_now.hour > sunset:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.office365.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                        from_addr=my_email,
                        to_addrs="RECEIVER EMAIL",
                        msg=f"Subject: Look Up\n\n Look up nigga"
            )

1111

