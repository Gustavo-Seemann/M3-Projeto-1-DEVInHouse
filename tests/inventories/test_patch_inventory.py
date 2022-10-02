from flask import json

mimetype = 'application/json'
url = "/inventory/"

def test_not_authorized_patch_inventory(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    data = {
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":3932.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"



def test_sucess_patch_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":3932.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 204


def test_fields_not_allowed_product_category_id(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "product_category_id": 1,
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":3932.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "Campo 'product_category_id' não permite alteração"


def test_fields_not_allowed_product_code(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":3932.98,
        "product_code": 1,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "Campo 'product_code' não permite alteração"


def test_invalid_value_patch_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":0,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'value': ['Valor inválido']}"


def test_invalid_value_less_than_zero_patch_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
	    "title":"Notebook i5-10400F, GTX1650, 16GB",
	    "value":-10.98,
	    "brand":"Alienware",
	    "template":"https://m.media-amazon.com/images/I/51WqIqjSOxL._AC_SL1000_.jpg",
	    "description":"Notebook Gamer Intel i5-10400F, Placa de video GTX1650 4GB, RAM 16 GB"
    }
    response = client.patch("/inventory/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'value': ['Valor inválido']}"


