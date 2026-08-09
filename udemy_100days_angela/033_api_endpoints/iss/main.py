import os
import requests
from dotenv import load_dotenv
from datetime import datetime


# Load .env variables
load_dotenv()


# Get my location details
MY_LAT = float(os.getenv('MY_LAT'))
MY_LONG = float(os.getenv('MY_LONG'))


def get_iss_details() -> dict:
    """Get ISS location"""
    iss_response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()['iss_position']
    iss_lat = float(iss_data['latitude'])
    iss_long = float(iss_data['longitude'])
    return({'lat': iss_lat, 'lng': iss_long})


def get_sunrise_sunset(lat: float, lng: float) -> dict:
    """Get sunset/sunrise time"""
    params = {
        'lat': lat,
        'lng': lng,
        }
    ss_response = requests.get('https://api.sunrise-sunset.org/v2', params=params)
    ss_response.raise_for_status()
    ss_data = ss_response.json()
    sunrise = int(ss_data['sunrise'].split('T')[1].split(':')[0])
    sunset = int(ss_data['sunset'].split('T')[1].split(':')[0])
    return({'sunrise': sunrise, 'sunset': sunset})


def is_iss_overhead(lat: float, lng: float) -> bool:
    """Checks if iSS is within +/- 5 degrees latitude"""
    return (
        MY_LAT - 5 <= lat <= MY_LAT + 5
        and MY_LONG - 5 <= lng <= MY_LONG + 5
    )


# Main program
# Opted for simple print statements rather than sending emails for simplicity
current_hour = datetime.now().hour

iss_location = get_iss_details()
ss_hours = get_sunrise_sunset(lat=MY_LAT, lng=MY_LONG)

if is_iss_overhead(**iss_location) and ss_hours['sunset'] < current_hour:
    print("The ISS is over you! Look at the sky!")
else:
    print(f"The ISS will be visible in {ss_hours['sunset']-current_hour} hour(s).")
