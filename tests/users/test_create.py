import random
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
        "role_id" : 1, 
        "name" : "Anderson van Hallen", 
        "email" : "anderson-teste@email.com",
        "age" : "04/04/1993",
        "password" : "Teste12345!"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert response.json['message'] == "Usuário foi criado com sucesso."


def test_missing_field_create(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    keys = ['city_id', 'gender_id', 'role_id', 'name', 'email', 'age', 'password']
    keys_not_have_in_request = keys.pop(random.randrange(len(keys)))
    data = {
        'city_id': 1566, 
        'gender_id' : 2, 
        'role_id' : 2,
        'name' : 'Luisa Savano', 
        'email' : 'savanoluisa2@email.com',
        'age' : '04/04/1993',
        'password' : 'Teste12345!'
    }
    del data[keys_not_have_in_request]
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_expected = {'error': {f'{keys_not_have_in_request}': [f'{keys_not_have_in_request} é obrigatório.']}}
    assert response.status_code == 400
    assert response.json['error'] == f"{response_expected['error']}"


def test_exist_email_db(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data =  {
        "city_id": 1566,
        "gender_id" : 1,
        "role_id" : 1 ,
        "name" : "João Victor",
        "age" : "04/04/1993" ,
        "email" : 'joao@email.com',
        "phone" : '48999999999',
        "password" : "Teste12345!"
     }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'email': ['Email já registrado']}"

def test_invalid_phone_lenght(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566, 
        "gender_id" : 1, 
        "role_id" : 1, 
        "name" : "Anderson van Hallen", 
        "email" : "anderson-teste@email.com",
        "age" : "04/04/1993",
        "phone" : "4899999",
        "password" : "Teste12345!"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'phone': ['Telefone inválido']}"


def test_invalid_phone_characters(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566, 
        "gender_id" : 1, 
        "role_id" : 1, 
        "name" : "Anderson van Hallen", 
        "email" : "anderson-teste@email.com",
        "age" : "04/04/1993",
        "phone" : "4999834224#",
        "password" : "Teste12345!"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "{'phone': ['Telefone inválido']}"
