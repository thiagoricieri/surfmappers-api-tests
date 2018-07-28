from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def test_follow():
  first = first_session_from_homepage()
  user = first['photographer']
  r = requests.post(sm.route('follow/{}'.format(user['_id'])), headers=headers)
  assert r.status_code == 201, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_unfollow():
  first = first_session_from_homepage()
  user = first['photographer']
  r = requests.delete(sm.route('follow/{}'.format(user['_id'])), headers=headers)
  assert r.status_code == 201, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_checkin():
  r = requests.post(sm.route('checkin'),
    headers=headers,
    params={ 'lat': fake.latitude(), 'long': fake.longitude() })
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'