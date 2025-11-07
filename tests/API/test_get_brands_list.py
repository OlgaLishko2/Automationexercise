import requests
from config.links import Links

def test_get_brands_list():


    resp = requests.get(f"{Links.HOST}/api/brandsList")

    print("Status code:", resp.status_code)
    print("Response:", resp.text)

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"


    data = resp.json()
    assert "brands" in data, "Response JSON does not contain 'brands'"
    assert isinstance(data["brands"], list), "'brands' is not a list"


    assert len(data["brands"]) > 0, "Brands list is empty"