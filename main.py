import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

parameters = {
    "lat": os.getenv('MY_LAT'),
    "lon": os.getenv('MY_LON'),
    "appid": os.getenv('API_KEY'),
    "cnt": 4
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()

data = response.json()

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    print('Bring an Umbrella')
    client = Client(account_sid, auth_token)
    # for sms- if this not works use whatsapp method
    message = client.messages.create(
        body='Its going to rain today, Remember to bring an UMBRELLA.',
        from_='+19303004324',
        to='+919778311669'
    )
    # try this
    # message = client.messages.create(
    #     body='Its going to rain today, Remember to bring an UMBRELLA.',
    #     from_='whatsapp:+14155238886',
    #     to='whatsapp:+919778311669'
    # )
    print(message.status)

        
