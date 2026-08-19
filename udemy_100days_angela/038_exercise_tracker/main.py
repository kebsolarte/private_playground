import requests
import os
from dotenv import load_dotenv


load_dotenv()


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
  "weight_kg": 72,                  
  "height_cm": 163,                 
  "age": 32,                        
  "gender": "male"                 
}

response = requests.post(url=QUERY_URL, json=request_body, headers=NE_KEYS)
response.raise_for_status()
data = response.json()
print(data)


# Sheety API tokens and calls
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_BASE_URL = 'https://api.sheety.co/f56d43c1df9771a798912f40b5cac00e/workoutTracker/workouts'

SHEETY_HEADER = {
    'Authorization': Bearer DAtwerk2025!
}

