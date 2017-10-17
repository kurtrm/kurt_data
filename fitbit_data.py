"""Script for pulling data from the Fitbit API."""
from fitbit import Fitbit
import os

CLIENT_ID = os.environ['client_id']
SECRET = os.environ['secret']
ACCESS_TOKEN = os.environ['access_token']
EXPIRES_AT = float(os.environ['expires_at'])
REFRESH_TOKEN = os.environ['refresh_token']
USER_ID = os.environ['user_id']


def refresh_cb(self, token_dict):
    """Function for refreshing access_token, refresh_token, and expires_at."""
    # global ACCESS_TOKEN
    # global EXPIRES_AT
    # global REFRESH_TOKEN
    # ACCESS_TOKEN = token_dict['access_token']
    # EXPIRES_AT = str(token_dict['expires_at'])
    # REFRESH_TOKEN = token_dict['refresh_token']
    import pdb; pdb.set_trace()
    self.access_token = self.token_dict['access_token']
    self.expires_at = self.token_dict['expires_at']
    self.refresh_token = self.token_dict['refresh_token']
    # os.environ['access_token'] = ACCESS_TOKEN
    # os.environ['expires_at'] = str(EXPIRES_AT)
    # os.environ['refresh_token'] = REFRESH_TOKEN

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
