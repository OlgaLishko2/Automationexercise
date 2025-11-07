import requests
from  pprint import pprint


# def test_search_list_jeans():
#     url = "https://automationexercise.com/api/searchProduct"
#     search_product = {"search_product" : "jeans"}
#     response = requests.post(
#         url = url,
#         data = search_product
#     )
#     # pprint(response.json())
#
#     body = response.json()
#     list_prod = body['products']
#     assert response.status_code == 200
#
#
#     for product in list_prod:
#         assert 'jeans' in product["name"].lower()
#         # print(product)
#         # print(product["id"])
#         # print(product["name"])


def test_search_list_dress():
    url = "https://automationexercise.com/api/searchProduct"
    search_product = {"search_product" : "dress"}
    response = requests.post(
        url = url,
        data = search_product
    )
     

    body = response.json()
    list_prod = body['products']
    assert response.status_code == 200


    for product in list_prod:
        assert 'dress' in product["category"]["category"].lower()


#
# def test_search_list_top():
#     url = "https://automationexercise.com/api/searchProduct"
#     search_product = {"search_product" : "top"}
#     response = requests.post(
#         url = url,
#         data = search_product
#     )
#     pprint(response.json())
