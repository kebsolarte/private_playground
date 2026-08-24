import requests
from datetime import datetime   


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.base_endpoint = endpoint
        self.api_key = api_key


    def check_roundtrip_flights(self, origin_code: str, destination_code: str, outbound_date: datetime, return_date: datetime) -> dict:
        """GET request to get google flights search through SerpAPI."""
        parameters = {
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
        response = requests.get(url=self.base_endpoint, params=parameters)
        return response.json()



    