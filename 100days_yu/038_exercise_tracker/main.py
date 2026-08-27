import requests
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

# Personal constants
WEIGHT = 72
HEIGHT = 163
AGE = 32
GENDER = 'male'

# Nutrition and exercise API keys and calls
NE_KEYS = {
    'x-app-id': os.getenv('NE_APP_ID'),
    'x-app-key': os.getenv('NE_KEY')
}
BASE_URL = 'https://app.100daysofpython.dev'


# Check if the server status and DB connectivity
response = requests.get(url=f'{BASE_URL}/healthz', headers=NE_KEYS)
print(response.text)


# Calculate calories burned from a natural language exercise description
QUERY_URL = f'{BASE_URL}/v1/nutrition/natural/exercise'

exercise_input = input('What exercise did you do today and for how long? ')

request_body = {
  "query": exercise_input,
  "weight_kg": WEIGHT,                  
  "height_cm": HEIGHT,                 
  "age": AGE,                        
  "gender": GENDER                 
}

response = requests.post(url=QUERY_URL, json=request_body, headers=NE_KEYS)
response.raise_for_status()
data = response.json()['exercises']
exercise = data[0]['name'].title()
duration = data[0]['duration_min']
calories = data[0]['nf_calories']
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')


# Sheety API tokens and calls
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_BASE_URL = 'https://api.sheety.co/f56d43c1df9771a798912f40b5cac00e/workoutTracker/workouts'

# Set up a auth via bearer token
SHEETY_HEADER = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

# Sheety uses camel case for the propeties
# Properties should be nested in a root following the endpoint (i.e. workout for workouts)
SHEETY_BODY = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}

# POST an activity
response = requests.post(url=SHEETY_BASE_URL, json=SHEETY_BODY, headers=SHEETY_HEADER)
# print(response.text)

# # GET records
# response = requests.get(url=SHEETY_BASE_URL, headers=SHEETY_HEADER)
# print(response.text)


