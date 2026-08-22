import os
from dotenv import load_dotenv
from pprint import pprint
from data_manager import DataManager



load_dotenv()

SHEETY_ENDPOINT = 'https://api.sheety.co/f56d43c1df9771a798912f40b5cac00e/flightDeals/prices'
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

sheety = DataManager(endpoint=SHEETY_ENDPOINT, token=SHEETY_TOKEN)
sheety_data = sheety.get_saved_flights_details()
pprint(sheety_data)

sheety.update_saved_flight_lowest_price(obj_id=2, new_price=165)
sheety_data = sheety.get_saved_flights_details()
print()
pprint(sheety_data)