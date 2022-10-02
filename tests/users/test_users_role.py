from flask import json

mimetype = 'application/json'
url = "/user/role"


def test_role_already_exists(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "description": "SYSTEM_ADMIN",
        "name": "Administrador do Sistema",
        "permissions": [1, 2, 3, 4]
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "O Cargo já existe."


def test_role_invalid_permissions(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "description": "SYSTEM_MOD",
        "name": "Moderador do Sistema",
        "permissions": [1, 2, 3, 9]
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "Permissões invalidas."


def test_create_role_sucess(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "description": "SYSTEM_MODERATOR",
        "name": "Moderador do Sistema",
        "permissions": [1, 2, 3]
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert response.json['message'] == "O Cargo foi criado com sucesso."


