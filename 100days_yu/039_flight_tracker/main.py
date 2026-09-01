import os
from dotenv import load_dotenv
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData



load_dotenv()

SHEETY_ENDPOINT = 'https://api.sheety.co/f56d43c1df9771a798912f40b5cac00e/flightDeals/prices'
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

SERPAPI_BASE_ENDPOINT = 'https://serpapi.com/search'
SERPAPI_KEY = os.getenv('SERP_KEY')
ORIGIN_CODE = 'MNL'
OUTBOUND_DATE = datetime.now().date()
RETURN_DATE = OUTBOUND_DATE + timedelta(weeks=24)

# sheety = DataManager(endpoint=SHEETY_ENDPOINT, token=SHEETY_TOKEN)
# sheety_data = sheety.get_saved_flights_details()
# pprint(sheety_data)

google_flights = FlightSearch(endpoint=SERPAPI_BASE_ENDPOINT, api_key=SERPAPI_KEY)
raw_flights_data = google_flights.check_roundtrip_flights(origin_code=ORIGIN_CODE, destination_code='SIN', outbound_date=OUTBOUND_DATE, return_date=RETURN_DATE)
flights = FlightData(outbound_date=OUTBOUND_DATE, return_date=RETURN_DATE, raw_json_response=raw_flights_data)

