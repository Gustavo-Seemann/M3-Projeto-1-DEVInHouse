from flask import json

mimetype = 'application/json'
url = "/user/create"

def test_sucess_create_user(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566, 
        "gender_id" : 1, 
        "role_id" : 1 , 
        "name" : "Usuario de Teste", 
        "age" : "04/04/1994",
        "email" : "testando@email.com",
        "phone" : "48999999999",
        "password" : "Senha12345!"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert response.json['message'] == "Usuário foi criado com sucesso."