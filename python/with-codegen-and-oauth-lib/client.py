"""
Very simple Partner API implementation:
- uses requests-oauthlib for OAUTH2 client implementation
- uses swagger-codegen for API proxy classes generation.

Please note that Refresh token is not saved/used here - this implementation is for demonstration purposes only.
In production implementation, you would save the refresh token, and use it to obtain new access token upon expiration.

"""

"""
Using Requests-OAuthlib: OAuth library for Humans
See https://requests-oauthlib.readthedocs.io/en/latest/
"""

from oauthlib.oauth2 import LegacyApplicationClient, BackendApplicationClient
from requests_oauthlib import OAuth2Session

"""
You get the following parameters from Intermedia:
"""
client_id = 'my_client_id'
client_secret = 'my_client_secret'
username = 'contact_id'
password = 'contact_password'

"""
This is standard API endpoint URLs
"""
api_base_url = 'https://cp.serverdata.net/Webservices'
api_service_url = api_base_url + '/RestAPI'
api_token_url = api_base_url + '/Auth/token/v1'

"""
Receiving the token
"""
client = LegacyApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=api_token_url,
                          client_id=client_id, client_secret=client_secret,
                          username=username, password=password, verify=False)

print(token)  # debug

"""
p\Proxy classes generated using swagger-codegen:
# swagger-codegen generate -i https://cp.serverdata.net/Webservices/RestAPI/docs/v1/ -l python
"""

import swagger_client.configuration as config
import swagger_client.apis.accounts_api as accounts_api

config.api_key = {'Authorization': token['access_token']}
config.api_key_prefix = {'Authorization': token['token_type']}
api = accounts_api.AccountsApi()

response = api.accounts_v1_get_accounts()
print(response)
