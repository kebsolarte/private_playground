import requests
from datetime import datetime

class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, outbound_date: datetime, return_date: datetime, raw_json_response: dict) -> None:
        self.departure_country = raw_json_response['airports'][0]['departure'][0]['airport']['id']
        self.arrival_country = raw_json_response['airports'][0]['arrival'][0]['airport']['id']
        self.outbound_date = outbound_date
        self.return_date = return_date

        # Handling missing best or other flights
        try:
            self.best_flights = {item['flights'][0]['airline']: item['price'] for item in raw_json_response['best_flights'] if item.get('price', None) != None}
        except KeyError:
            self.best_flights = {}

        try:
            self.other_flights ={item['flights'][0]['airline']: item['price'] for item in raw_json_response['other_flights'] if item.get('price', None) != None}
        except KeyError:
            self.other_flights = {}

        # Uses the find_cheapest_flight method to find the cheapest flight pair
        self.cheapest_flight = self.find_cheapest_flight()


    def find_cheapest_flight(self) -> tuple:
        """Finds the cheapest flights from the pulled data, combining best flights and other flights."""
        # Combine flight details, if keys overlap, the item in best flights will overwrite the older data
        combined_flights = {**self.other_flights, **self.best_flights}

        # Finds the cheapest pair in combined_flights
        cheapest = min(combined_flights, key=combined_flights.get)
        return (cheapest, combined_flights[cheapest])


