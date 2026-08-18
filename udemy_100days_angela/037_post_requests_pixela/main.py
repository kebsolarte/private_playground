import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()


PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
PIXELA_UN = os.getenv('PIXELA_UN')
PIXELA_BASE_ENDPOINT = 'https://pixe.la/v1/users'


# Creating a new pixela user/account
# Pixela token and UN are self-created
NEW_USER_ENDPOINT = PIXELA_BASE_ENDPOINT

NEW_USER_JSON = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_UN,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# # POST request to create a new user, should retun status code 200
# # json param accepts a JSON object to pass together with the POST request
# response = requests.post(url=NEW_USER_ENDPOINT, json=NEW_USER_JSON)
# print(response.text)


# Creating a Pixela graph
GRAPHS_ENDPOINT = f'{PIXELA_BASE_ENDPOINT}/{PIXELA_UN}/graphs'

# Headers are more secured way of passing tokens and keys than
# passing tokens/keys as params and including it in URL
HEADER = {
    'X-USER-TOKEN': PIXELA_TOKEN
}

GRAPH_JSON = {
    'id': 'graph1',
    'name': 'Daily Exercise Tracker',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai',
    'timezone': 'Asia/Manila',
    'description': 'This tracks my daily exercise duration whether it is running, cycling, or other activities.'
}

# # POST request to create a graph
# response = requests.post(url=GRAPHS_ENDPOINT, json=GRAPH_JSON, headers=HEADER)
# print(response.text)
# print(f'{GRAPHS_ENDPOINT}/{GRAPH_JSON['id']}.html')


# Plotting an activity in Pixela
GRAPH_ENDPOINT = f'{GRAPHS_ENDPOINT}/{GRAPH_JSON['id']}'

# Formats date according to API requirements
date = datetime.now().date() - timedelta(days=1)
date = date.strftime('%Y%m%d')

PLOT_JSON = {
    'date': date,
    'quantity': '120'
}

# # POST request to plot an activity
# response = requests.post(url=GRAPH_ENDPOINT, json=PLOT_JSON, headers=HEADER)
# print(response.text)
# print(f'{GRAPH_ENDPOINT}.html')


# Updating a plotted activity
UPDATE_ENDPOINT = f'{GRAPH_ENDPOINT}/{date}'

UPDATE_JSON = {
    'quantity': '110'
}

# # PUT request to update an activity
# response = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_JSON, headers=HEADER)
# print(response.text)
# print(f'{GRAPH_ENDPOINT}.html')


# Deleting a plotted activity
DELETE_ENDPOINT = f'{GRAPH_ENDPOINT}/{date}'

# # DELETE request to delete a plotted activity
# response = requests.delete(url=DELETE_ENDPOINT, headers=HEADER)
# print(response.text)
# print(f'{GRAPH_ENDPOINT}.html')