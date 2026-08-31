import requests

class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, raw_json_response: dict) -> None:
        self.price = 0
        self.departure_country = ''
        self.arrival_country = ''
        self.outbound_date = ''
        self.return_date = ''


def find_cheapest_flight():
    pass

