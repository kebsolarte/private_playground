import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    
    def __init__(self, endpoint: str, token: str) -> None:
        self.base_endpoint = endpoint
        self.headers = {
            'Authorization': f'Bearer {token}'
        }


    def get_saved_flights_details(self) -> dict:
        """GET request for retrieving data in sheets DB"""
        response = requests.get(url=self.base_endpoint, headers=self.headers)
        return response.json()['prices']


    def update_saved_flight_lowest_price(self, obj_id: int, new_price: float) -> None:
        """PUT request for updating lowest price of tracked flights"""
        update_endpoint = f'{self.base_endpoint}/{obj_id}'
        update_fields = {
            'price': {
                'lowestPrice': new_price
            }
        }
        response = requests.put(url=update_endpoint, json=update_fields, headers=self.headers)
        print(f"Successfully updated the lowest price for object id #{obj_id} to USD{new_price}.")