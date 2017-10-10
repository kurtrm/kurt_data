"""Script for pulling data from the Fitbit API."""
from fitbit import Fitbit
import os

CLIENT_ID = os.environ['client_id']
SECRET = os.environ['secret']
ACCESS_TOKEN = os.environ['access_token']
EXPIRES_AT = os.environ['expires_in']
REFRESH_TOKEN = os.environ['refresh_token']
USER_ID = os.environ['user_id']


def refresh_cb(token_dict):
    """Function for refreshing access_token, refresh_token, and expires_at."""
    os.environ['access_token'] = token_dict['access_token']
    os.environ['expires_at'] = str(token_dict['expires_at'])
    os.environ['refresh_token'] = token_dict['refresh_token']

    return token_dict

kurt = Fitbit(
    CLIENT_ID,
    SECRET,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
    expires_at=EXPIRES_AT,
    refresh_cb=refresh_cb
)

#  Activate this project's environment.
#  Run ../python-fitbit/gather_keys_oauth2.py $client_id $secret
#  Set the new environmental variables from the output
