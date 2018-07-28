from utils import *
from faker import Faker
from test_auth import get_token
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def get_homepage_sessions():
  return requests.get(sm.route('sessions/last'), headers=headers)

def first_session_from_homepage():
  return get_homepage_sessions().json()['albums'][0]

def test_homepage_sessions():
  r = get_homepage_sessions()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_photos_of_session():
  first = first_session_from_homepage()
  r = requests.get(sm.route('sessions/{}/photos'.format(first['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_sessions_of_photographer():
  first = first_session_from_homepage()
  r = requests.get(sm.route('sessions/photographer/{}'.format(first['username'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'