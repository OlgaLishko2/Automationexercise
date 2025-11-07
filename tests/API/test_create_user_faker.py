
from config.links import Links
import requests
from faker import Faker
from pprint import pprint


fake = Faker()



def test_create_user_faker():

    user_data = {
        "name": fake.name(),
        "email": fake.email(),
        "password": "Test1234!",
        "title": "Mr",
        "birth_date": "2",
        "birth_month": "9",
        "birth_year": "1980",
        "newsletter": "true",
        "optin": "true",
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number()
    }

    resp = requests.post(
        url = f"{Links.HOST}/api/createAccount",
        data = user_data
    )
    resp.raise_for_status()
    pprint(resp.json())
    assert resp.status_code == 200
    assert "User created" in resp.text or "already exists" in resp.text




