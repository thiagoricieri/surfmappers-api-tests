from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage, get_photos_of
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def get_cart_history():
  return requests.get(sm.route('carts/history'), headers=headers)

def get_shipping_options():
  return requests.get(sm.route('carts/shipping'), headers=headers, params={ 'cep': "80320050" })

def test_cart():
  r = requests.get(sm.route('carts/active'), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_add_to_cart():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.post(sm.route('carts/photos/{}'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_remove_from_cart():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.delete(sm.route('carts/photos/{}'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_convert_photo_to_frame():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.delete(sm.route('carts/frames/{}'.format(photo['_id'])), headers=headers)
  assert r.status_code == 304, 'Request not modified'

def test_remove_frame_from_cart():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.delete(sm.route('carts/frames/{}'.format(photo['_id'])), headers=headers)
  assert r.status_code == 304, 'Request not modified'

def test_cart_history():
  r = get_cart_history()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_cart_with_id():
  history = get_cart_history()
  assert history.status_code == 200, 'History exist'
  cart_id = history.json()['carts'][0]['_id']
  r = requests.get(sm.route('carts/{}'.format(cart_id)), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_cart_get_shipping():
  r = get_shipping_options()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

# Can't test now
# def test_cart_set_shipping():
#   shipping = get_shipping_options()
#   assert shipping.status_code == 200, 'Shippiong returned ok'
#   s = shipping.json()
#   queries = {
#     "cep": "80320050",
#     "service": s.servico,
#     "address": fake.address(),
#     "city": 0,
#     "state": 0
#   }
#   r = requests.post(sm.route('carts/shipping', params=queries))
#   assert r.status_code == 200, 'Request succeeded'
#   assert r.json() is not None, 'Json result is valid'