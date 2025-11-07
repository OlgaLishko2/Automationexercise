import requests
from config.links import Links

def test_post_products_not_allowed():
    url = f"{Links.HOST}/api/productsList"

    resp = requests.post(url, data={})

    print("Status code:", resp.status_code)
    print("Response:", resp.text)


    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    assert "not supported" in resp.text.lower(), "Expected 'not supported' message"
