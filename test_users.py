from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def test_users_me():
  r = requests.get(sm.route('users/me'), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_users_id():
  first = first_session_from_homepage()
  user = first['photographer']
  assert 'username' in user, 'User has username property'
  r = requests.get(sm.route('users/{}'.format(user['username'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_friends_of():
  first = first_session_from_homepage()
  user = first['photographer']
  assert 'username' in user, 'User has username property'
  r = requests.get(sm.route('friends/{}'.format(user['username'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_request_friendship():
  first = first_session_from_homepage()
  user = first['photographer']
  assert 'username' in user, 'User has username property'
  r = requests.get(sm.route('friends/{}'.format(user['username'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_remove_friendship():
  first = first_session_from_homepage()
  user = first['photographer']
  assert 'username' in user, 'User has username property'
  r = requests.delete(sm.route('friends/{}'.format(user['username'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_my_friends():
  r = requests.get(sm.route('friends'), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'