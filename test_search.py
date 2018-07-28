from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def get_countries():
  return requests.get(sm.route('search/countries'), headers=headers)

def test_search():
  queries = {
    'search': fake.first_name(),
    'limit': 20
  }
  r = requests.get(sm.route('search'), headers=headers, params=queries)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_search_countries():
  r = get_countries()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_search_states():
  countries = get_countries()
  country = countries[0]
  r = requests.post(sm.route('search/{}/states'.format(country['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_search_photographers():
  queries = {
    'search': fake.first_name(),
    'limit': 20
  }
  r = requests.get(sm.route('search/photographers'), headers=headers, params=queries)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_search_spots():
  queries = {
    'search': fake.first_name(),
    'limit': 20
  }
  r = requests.get(sm.route('search/spots'), headers=headers, params=queries)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'