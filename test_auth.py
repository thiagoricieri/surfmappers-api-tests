from utils import *
from faker import Faker
import requests

sm = Surfmappers()
fake = Faker()

def perform_login():
  params = {
    "username": sm.login,
    "password": sm.password
  }
  r = requests.post(sm.route('login'), json=params)
  return r

def get_token():
  return perform_login().json()['token']

def test_login():
  r = perform_login()
  assert r.status_code == 200, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'
  assert r.json()['token'] is not None, 'Token exists'

def test_signup():
  password = fake.password()
  params = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "ddd": "84",
    "phone": "999999999",
    "password": password,
    "confirm_password": password,
    "user_type": "surfer"
  }
  r = requests.post(sm.route('signup'), json=params)
  assert r.status_code == 201, 'Request succeeded'
  assert r.json() is not None, 'Json result is valid'
