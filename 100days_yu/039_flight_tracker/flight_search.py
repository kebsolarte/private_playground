import requests
from datetime import datetime   
from flight_data import FlightData


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.base_endpoint = endpoint
        self.api_key = api_key


    def check_roundtrip_flights(self, 
                                origin_code: str, 
                                destination_code: str, 
                                outbound_date: datetime, 
                                return_date: datetime
                                ) -> FlightData:
        """GET request to get google flights search through SerpAPI."""
        query = {
            "engine": "google_flights",
            "departure_id": origin_code,
            "arrival_id": destination_code,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self.api_key,
        }
        response = requests.get(url=self.base_endpoint, params=query)
        print(f"Successfully pulled fresh google flights searches for {destination_code}!")

        # Return the response as a FlightData object
        return FlightData(
            outbound_date=outbound_date,
            return_date=return_date,
            raw_json_response=response.json()
            )



    