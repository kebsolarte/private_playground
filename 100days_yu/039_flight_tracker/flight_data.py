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
            self.best_flights = {item['flights'][0]['airline']: float(item['price']) for item in raw_json_response['best_flights'] if item.get('price', None) != None}
        except KeyError:
            self.best_flights = {}
            print("No best flights from API response.")

        try:
            self.other_flights ={item['flights'][0]['airline']: float(item['price']) for item in raw_json_response['other_flights'] if item.get('price', None) != None}
        except KeyError:
            self.other_flights = {}
            print("No other flights from API response.")

        # Uses the find_cheapest_flight method to find the cheapest flight pair
        self.cheapest_flight = self.find_cheapest_flight()


    def find_cheapest_flight(self) -> tuple:
        """Finds the cheapest flights from the pulled data, combining best flights and other flights."""
        # Combine flight details, if keys overlap, the item in best flights will overwrite the older data
        combined_flights = {**self.other_flights, **self.best_flights}

        # Finds the cheapest pair in combined_flights and return the flight pair
        cheapest_flight = min(combined_flights, key=combined_flights.get)
        return (cheapest_flight, combined_flights[cheapest_flight])


    def compare_and_update_cheapest_flight_price(self, stored_price: float ) -> bool:
        """Compares the pulled cheapest flight data to the sheets DB data.
            A bool is returned to trigger downstream activities if a cheaper price is found."""

        # Comparing prices
        if self.cheapest_flight[1] < stored_price:
            print(f"Found a cheaper flight price for {self.arrival_country} from {self.cheapest_flight[0]}!")
            return True
        else:
            print(f"No cheaper flight found for {self.arrival_country}.")
            return False


