import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token= os.environ.get("TWILIO_AUTH_TOKEN")

OWM_ENDPOINT = os.environ.get("OWM_ENDPOINT")
api_key = os.environ.get("api_key")

parameters = {
    "lat": 9.605624,
    "lon": 77.171297,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]

will_rain = False

for hour_data in weather_data:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    
    client.api.account.messages.create(
    to="+919382036996",
    from_="+13863462899",
    body="Carry an Umbrella. It will rain today!☔")
