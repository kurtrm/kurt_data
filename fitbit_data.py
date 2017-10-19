"""Script for pulling data from the Fitbit API."""
from fitbit import Fitbit
# import os
# import yaml

# CLIENT_ID = os.environ['client_id']
# SECRET = os.environ['secret']


def refresh_cb(self, token_dict):
    """Function for refreshing access_token, refresh_token, and expires_at."""
    self.access_token = self.token_dict['access_token']
    self.refresh_token = self.token_dict['refresh_token']
    self.expires_at = self.token_dict['expires_at']

    return token_dict

# with open('config.yml') as config:
#     tokens = yaml.load(config)


def instantiate_fitbit_kurt():
    """Uses gather_keys_oauth2 class to gather tokens and instantiate a

    'Kurt' Fitbit class.
    """
    import gather_keys_oauth2
    import os

    CLIENT_ID = os.environ['client_id']
    SECRET = os.environ['secret']
    server = gather_keys_oauth2.OAuth2Server(
        CLIENT_ID,
        SECRET
    )
    server.browser_authorize()
    import pdb; pdb.set_trace()
    access_token = server.oauth.token['access_token']
    refresh_token = server.oauth.token['refresh_token']
    expires_at = server.oauth.token['expires_at']
    kurt = Fitbit(
        CLIENT_ID,
        SECRET,
        access_token=access_token,
        refresh_token=refresh_token,
        expires_at=expires_at,
        refresh_cb=refresh_cb
    )
    return kurt

#  Activate this project's environment.
#  Run ../python-fitbit/gather_keys_oauth2.py $client_id $secret
#  Set the new environmental variables from the output
