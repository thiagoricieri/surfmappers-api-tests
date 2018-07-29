from utils import *
from faker import Faker
from test_auth import get_token
from test_sessions import get_homepage_sessions, first_session_from_homepage, get_photos_of
import requests

sm = Surfmappers()
fake = Faker()
token = get_token()
headers = {'Authorization': 'Bearer {}'.format(token)}

def test_get_photo():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.get(sm.route('photos/{}'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_unlike_photo():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.post(sm.route('photos/{}/like'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_like_photo():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.post(sm.route('photos/{}/unlike'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_comment_photo():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  comment = { "comment_text": fake.text() }
  r = requests.post(sm.route('photos/{}/comments'.format(photo['_id'])), 
    headers=headers,
    json=comment)
  assert r.status_code == 201, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'

def test_get_comments_photo():
  first = first_session_from_homepage()
  photo = get_photos_of(first)
  assert photo.status_code == 200, 'Photos exist'
  photo = photo.json()["photos"][0]
  r = requests.get(sm.route('photos/{}/comments'.format(photo['_id'])), headers=headers)
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'