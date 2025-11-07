from config.links import Links
import requests
import random
import string
from pprint import pprint


def test_create_user_random():

    random_number = random.randint(1000, 9999)
    email = f"usertest{random_number}@example.com"

    user_data = {
        "name": "New_user",
        "email": email,
        "password": "Test1234!",
        "title": "Mrs",
        "birth_date": "01",
        "birth_month": "8",
        "birth_year": "1990",
        "newsletter": "true",
        "optin": "true",
        "firstname": "New",
        "lastname": "User",
        "company": "NewCompany",
        "address1": "111 New St",
        "address2": "",
        "country": "Canada",
        "zipcode": "12345",
        "state": "Alberta",
        "city": "Calgary",
        "mobile_number": "1234567890"
    }
    resp = requests.post(
        url = f"{Links.HOST}/api/createAccount",
        data = user_data
    )
    resp.raise_for_status()
    pprint(resp.json())
    assert resp.status_code == 200
    assert "User created" in resp.text or "already exists" in resp.text

