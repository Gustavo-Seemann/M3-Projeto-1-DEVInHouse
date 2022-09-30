import random
from flask import json

mimetype = 'application/json'
url = "/inventory/"


def test_sucess_create_item(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 938123,
	    "value":3980.99,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201

def test_missing_field_create_item(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    keys = ['product_category_id', 'title', 'product_code', 'value', 'brand', 'template', 'description']
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 938123,
	    "value":3980.99,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    del data[keys_not_have_in_request]
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_expected = {'error': {f'{keys_not_have_in_request}': [f'{keys_not_have_in_request} é obrigatório.']}}
    assert response.status_code == 400
    assert response.json['error'] == f"{response_expected['error']}"


def test_invalid_product_value_equals_zero(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 938123,
	    "value":0,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'value': ['Valor inválido']}"


def test_invalid_product_value_less_than_zero(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 938123,
	    "value":-1932.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'value': ['Valor inválido']}"


def test_exist_product_code(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 1,
	    "value":3932.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'product_code': ['Código já registrado']}"


def test_not_authorized_post_inventory(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
        "product_code": 938123,
	    "value":3980.99,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"