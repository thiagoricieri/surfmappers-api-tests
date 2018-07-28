from utils import *
from faker import Faker
from test_auth import get_token
import requests

sm = Surfmappers()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def get_spots():
  return requests.get(sm.route('spots'), headers=headers)

def test_get_spots():
  r = get_spots()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'