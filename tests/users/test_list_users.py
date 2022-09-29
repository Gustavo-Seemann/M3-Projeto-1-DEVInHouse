from flask import json

mimetype = 'application/json'
url = "/user/"


def test_not_authorized_get_user(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    response = client.get(url, headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"

    