from flask import json

mimetype = 'application/json'
url = "/user/"

def test_sucess_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 2,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998" ,
        "email" : "ana@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 204

def test_not_found_id_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    data = {
        "city_id": 1566,
        "gender_id" : 2,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998" ,
        "email" : "ana@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    response = client.patch("/user/99999999999999", data=json.dumps(data), headers=headers)
    assert response.status_code == 404
    assert response.json['message'] == "Usuario nao encontrado."
