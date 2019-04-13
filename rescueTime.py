# load api key
# key this api key private!
from datetime import datetime
import numpy as np
import pandas as pd
import requests
with open('api_key.txt', 'r') as f:  # equivalent to opening, reading and closing app
    api_key = f.read().replace('\n', '')

# Headers to be passed in the request
# headers = {
    # "authorization": 'Bearer %s' % api_key,  # for the Traider API
    # "accept": 'application/json',
# }

params = {
    "key": '%s' % api_key,
    "format": 'json',

}

endpoint = 'https://www.rescuetime.com/anapi/data'

response = requests.get(endpoint, params=params)
print(response.json())
