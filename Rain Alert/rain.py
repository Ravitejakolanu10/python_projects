import requests
from twilio.rest import Client

api_key = "your openweather api key"

latitude = "your latitude"
longitude = "your longitude"

url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" :latitude,
    "lon" : longitude,
    "appid" : api_key,
    "cnt" :4
}

response = requests.get(url, params=parameters)
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"] :
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain =True
    

if will_rain :
    account_sid = "your twilio account_id"
    auth_token = "your twilio account auth_token"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="http://d emo.twilio.com/docs/voice.xml",
        to="+15558675310",
        from_="+15017122661",
    )

    print(call.sid)
