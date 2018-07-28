from utils import *
from faker import Faker
from test_auth import get_token
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
  user_id = "0"
  r = requests.get(sm.route('users/{}'.format(user_id)), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_friends_of():
  user_id = "0"
  r = requests.get(sm.route('friends/{}'.format(user_id)), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_request_friendship():
  user_id = "0"
  r = requests.get(sm.route('friends/{}'.format(user_id)), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_remove_friendship():
  user_id = "0"
  r = requests.delete(sm.route('friends/{}'.format(user_id)), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_my_friends():
  r = requests.get(sm.route('friends'), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'