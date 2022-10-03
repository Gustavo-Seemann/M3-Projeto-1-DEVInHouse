from flask import json

mimetype = 'application/json'
url = "/user/"

def test_not_authorized_patch_user(client):
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
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"


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
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
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

def test_invalid_password_patch(client, logged_in_client):
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
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "T!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Senha fraca, utilize letras maiúsculas, minúsculas, números e caracteres especiais'

def test_invalid_phone_patch(client, logged_in_client):
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
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "4899999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Telefone inválido'


def test_existent_email_patch(client, logged_in_client):
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
        "age" : "12/05/1998",
        "email" : "ana@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Esse email já está em uso.'

def test_name_with_less_than_3_char_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 2,
        "role_id" : 2,
        "name" : "An",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Por favor insira um nome com mais de 3 caracteres.'


def test_invalid_city_id_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 10941281,
        "gender_id" : 2,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Cidade não encontrada.'


def test_invalid_gender_id_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 12,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Gênero não encontrado.'

def test_invalid_role_id_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 1,
        "role_id" : 369,
        "name" : "Ana Luiza",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Função não encontrada.'

def test_invalid_age_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 1,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "19",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Data de nascimento inválida'


def test_invalid_cep_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 1,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!",
        "cep": "98890"
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'CEP inválido'

def test_invalid_number_street_patch(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {logged_in_client}"
    data = {
        "city_id": 1566,
        "gender_id" : 1,
        "role_id" : 2,
        "name" : "Ana Luiza",
        "age" : "12/05/1998",
        "email" : "ana12@email.com",
        "phone" : "48999999999",
        "password" : "Teste12345!",
        "number_street": -12
    }
    response = client.patch("/user/2", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == 'Número da rua inválido'