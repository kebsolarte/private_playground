import os
from dotenv import load_dotenv
import requests


# Load .env variables
load_dotenv()


# Get variable values and keys
OW_KEY = os.getenv('OPENWEATHER_KEY')
MY_LAT = os.getenv('MY_LAT')
MY_LONG = os.getenv('MY_LONG')


# Get hourly OpenWeather data
OW_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': OW_KEY,
    'cnt': 4
}

ow_response = requests.get(url=OW_ENDPOINT, params=parameters)
ow_response.raise_for_status()
ow_data = ow_response.json()['list']
ow_data_weather_ids = [item['weather'][0]['id'] for item in ow_data]


def will_it_rain(weather_ids: list) -> bool:
    # Original code:
    #  for _ in weather_ids:
    #     if _ < 700:
    #         return True
    # return False
    
    # Better code: use the lazy built-in func any() which returns true as soon as it finds something truthy
    return any(id < 700 for id in weather_ids)

# There's a part about using Twilio API to send a notif via message, but I opted to do it some other time
# For now, confirming the API call via a print statement
print(will_it_rain(ow_data_weather_ids))

