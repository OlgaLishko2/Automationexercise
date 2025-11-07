import requests
from config.links import Links


def test_get_all_products():
    url = f"{Links.HOST}/api/productsList"

    resp = requests.get(url)

    print("Status code:", resp.status_code)
    print("Response:", resp.text)

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"

    data = resp.json()
    assert "products" in data, "Response JSON does not contain 'products'"
    assert isinstance(data["products"], list), "'products' is not a list"

    assert len(data["products"]) > 0, "Products list is empty"

