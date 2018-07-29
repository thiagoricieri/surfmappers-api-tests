from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage
from test_spots import get_spots
import datetime as dt
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def get_agenda():
  params = {
    "limit": 20,
    "page": 1
  }
  return requests.get(sm.route('agenda'), headers=headers, params=params)

def test_agenda():
  r = get_agenda()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'
  assert r.json()['entries'] is not None, 'Agenda has entries'

def test_add_to_agenda():
  spots = get_spots()
  assert spots.status_code == 200, 'Spots exist'
  now = dt.datetime.now()
  date = "%d/%d/%d %d:%d" % (now.day, now.month, now.year, now.hour, now.minute)
  queries = {
    "spot_id": spots[0]['_id'],
    "date": date
  }
  r = requests.post(sm.route('agenda'), headers=headers, params=queries)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_users_agenda():
  first = first_session_from_homepage()
  user = first['photographer']
  assert user["_id"] is not None, "User must have an id"
  r = requests.get(sm.route('{}/agenda'.format(user['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_remove_from_agenda():
  agenda = get_agenda()
  assert agenda.status_code == 200, 'Agenda returned correctly'
  agenda = agenda.json()["entries"]
  r = requests.delete(sm.route('agenda/{}'.format(agenda[0]['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

print(first_session_from_homepage())