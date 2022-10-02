from flask import json

mimetype = 'application/json'
url = "/user/"


def test_not_authorized_get_user(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    response = client.get("/user/?name=a", headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"


def test_return_data_get_users(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/user/?name=a", headers=headers)
    assert "Dados" in response.json

    
def test_sucess_get_user(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/user/?name=a", headers=headers)
    assert response.status_code == 200
    assert response.json['Status'] == "Sucesso"

def test_not_found_get_user(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/user/?name=aaaaaaaa", headers=headers)
    assert response.status_code == 204

def test_return_data_get_users(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get("/user/", headers=headers)
    assert "Dados" in response.json