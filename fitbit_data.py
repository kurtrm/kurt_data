"""Script for pulling data from the Fitbit API."""
from fitbit import Fitbit
import os

CLIENT_ID = os.environ['client_id']
SECRET = os.environ['secret']
ACCESS_TOKEN = os.environ['access_token']
EXPIRES_AT = os.environ['expires_in']
REFRESH_TOKEN = os.environ['refresh_token']
USER_ID = os.environ['user_id']


kurt = Fitbit(
    CLIENT_ID,
    SECRET,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
    expires_at=EXPIRES_AT,
)