import os
from dotenv import load_dotenv
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta


load_dotenv()

SHEETY_ENDPOINT = 'https://api.sheety.co/f56d43c1df9771a798912f40b5cac00e/flightDeals/prices'
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

SERPAPI_BASE_ENDPOINT = 'https://serpapi.com/search'
SERPAPI_KEY = os.getenv('SERP_KEY')
ORIGIN_CODE = 'MNL'
OUTBOUND_DATE = datetime.now().date() + timedelta(days=90)
RETURN_DATE = OUTBOUND_DATE + timedelta(weeks=1)


# Creating the sheety DataManager object and pulling the data in sheets DB
sheety = DataManager(endpoint=SHEETY_ENDPOINT, token=SHEETY_TOKEN)
sheety_data = sheety.get_saved_flights_details()


# Creating the google flight search engine object
google_flights = FlightSearch(endpoint=SERPAPI_BASE_ENDPOINT, api_key=SERPAPI_KEY)


# Main program
# Iterate over each row in sheety_data. itertuples is faster than iterrows.
for row in sheety_data.itertuples(index=False):
    print(f"Checking if there is a cheaper flight for {row.city} from {OUTBOUND_DATE} to {RETURN_DATE}...")

    # Get available flights(FlightData object)
    flights = google_flights.check_roundtrip_flights(
        origin_code=ORIGIN_CODE, 
        destination_code=row.iataCode, 
        outbound_date=OUTBOUND_DATE, 
        return_date=RETURN_DATE
        )

    # Compare and update price if a cheaper flight is found
    print(f"Checking if the new flight prices for {row.city} are cheaper than the stored flight prices ...")
    if flights.compare_and_update_cheapest_flight_price(stored_price=row.lowestPrice):
        print(f"Updating stored cheapest flight price for {row.city} ...")
        sheety.update_saved_flight_lowest_price(obj_id=row.id, new_price=flights.cheapest_flight[1])
        print("SEND NOTIF")

    print("---------- Moving on to the next item on the list ----------")
print("Done looking for cheaper flights! Book your flight now or check back tomorrow for fresh data!")

