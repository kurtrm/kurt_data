"""Script for pulling data from the Fitbit API."""
from fitbit import Fitbit
import os
import yaml

CLIENT_ID = os.environ['client_id']
SECRET = os.environ['secret']


def refresh_cb(self, token_dict):
    """Function for refreshing access_token, refresh_token, and expires_at."""
    # with shelve.open('tokens.db', writeback=True) as tokens:
    #     tokens['access_token'] = token_dict['access_token']
    #     tokens['expires_at'] = token_dict['expires_at']
    #     tokens['refresh_token'] = token_dict['refresh_token']

    import pdb; pdb.set_trace()
    self.access_token = self.token_dict['access_token']
    self.expires_at = self.token_dict['expires_at']
    self.refresh_token = self.token_dict['refresh_token']

    return token_dict

kurt = Fitbit(
    CLIENT_ID,
    SECRET
)

#  Activate this project's environment.
#  Run ../python-fitbit/gather_keys_oauth2.py $client_id $secret
#  Set the new environmental variables from the output
