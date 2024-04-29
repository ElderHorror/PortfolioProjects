import requests
from datetime import datetime

MY_LAT =  9.081999
MY_LONG = 8.675277

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()


print(sunrise, sunset)










