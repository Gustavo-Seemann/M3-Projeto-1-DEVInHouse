from flask import json

mimetype = 'application/json'
url = "/inventory/"

def test_sucess_get_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/?title=a", headers=headers)
    assert response.status_code == 200
    assert response.json['Status'] == "Sucesso"

def test_not_authorized_get_inventory(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    response = client.get("/inventory/?name=a", headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"

def test_return_data_get_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/?title=a", headers=headers)
    assert "Dados" in response.json

def test_20_per_page_get_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/", headers=headers)
    assert len(response.json["Dados"]) == 20


def test_not_found_get_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/?title=aaaaaaaaaaaaaaaaa", headers=headers)
    assert response.status_code == 204


def test_sucess_get_inventory_by_id(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/2", headers=headers)
    assert response.status_code == 200
    assert "Dados" in response.json

def test_not_exist_get_inventory_by_id(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/inventory/99999999999", headers=headers)
    assert response.status_code == 404
    assert response.json['error'] == "Não foi encontrado nenhum produto."