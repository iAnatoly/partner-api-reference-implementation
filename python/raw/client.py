"""
Extremely simple Partner API implementation:
- uses raw HTTP request to get the token
- uses raw HTTP request to call the API

This implementation is for demonstration purposes only.
"""

import requests
import json

"""
You get the folllowing parameters from Intermedia:
"""
client_id='my_client_id'
client_secret='my_client_secret'
username='intermedia_contact_id'
password='contact_password'
api_base_url='https://cp.serverdata.net/Webservices'

api_service_url = api_base_url + '/RestAPI/api/v1'
api_token_url = api_base_url + '/Auth/token/v1'

"""
Creating the OAUTH2 form data by hand.
You can (and should) pass client_id and client_secret as Basic Auth headers.
We are omitting this code for simplicity purposes only.
"""

data = 'grant_type=password&client_id={}&client_secret={}&username={}&password={}'\
    .format(client_id, client_secret, username, password)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(api_token_url, data=data, headers=headers)
assert response.status_code == 200

decoded_response = json.loads(response.content.decode('UTF-8'))
bearer_token = decoded_response['access_token']

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {}".format(bearer_token)
}

response = requests.get(api_service_url+"/accounts", headers=headers)
assert response.status_code == 200

decoded_response = json.loads(response.content.decode('UTF-8'))
print(decoded_response)
