from dotenv import load_dotenv
import requests
from twilio.rest import Client
import os
load_dotenv()
account_sid =  os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

API_KEY=os.environ["OWM_API_KEY"]

LAT=13.082680
LON=80.270721
parameter={
    "appid":API_KEY,
    "lat":LAT,
    "lon":LON,
    "cnt":4}
will_rain=False
response=requests.get(url="http://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
data=response.json()
today_weather=[]

for i in data["list"]:
    condition_code=i['weather'][0]['id']
    if int(condition_code)<700:
        will_rain=True

if will_rain==True:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to rain today, Bring an umbrella",
        from_="+15855413603",
        to="+917075848865",
    )

    print(message.sid)
    print(message.status)
