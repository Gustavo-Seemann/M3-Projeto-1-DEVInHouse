from urllib import response
from flask import json
from src.app.models.inventory import Inventory
from src.app.models.user import User
from src.app.utils import format_currency

mimetype = 'application/json'
url = "/inventory/results"


def test_not_authorized_results_inventory(client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    response = client.get(url, headers=headers)
    assert response.status_code == 403
    assert response.json['error'] == "Você não tem permissão"


def test_sucess_results_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    response = client.get(url, headers=headers)
    assert response.status_code == 200
    assert "itens emprestados" in response.json
    assert "numero de usuários" in response.json
    assert "quantidade de produtos" in response.json
    assert "valor total de itens" in response.json

def test_number_of_users_results_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    users = User.query.all()
    response = client.get(url, headers=headers)
    assert response.json["numero de usuários"] == len(users)

def test_number_of_itens_results_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    itens = Inventory.query.all()
    response = client.get(url, headers=headers)
    assert response.json["quantidade de produtos"] == len(itens)

def test_total_value_of_itens_results_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    itens = Inventory.query.all()
    itens_total_value = format_currency(sum([item.value for item in itens]))
    response = client.get(url, headers=headers)
    assert response.json["valor total de itens"] == itens_total_value

def test_loaned_itens_results_inventory(client, logged_in_client):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"
    itens = Inventory.query.all()
    itens_loaned = len(
            [
                item.user_id
                for item in itens
                if item.user_id is not None or item.user_id == 0
            ]
        )
    response = client.get(url, headers=headers)
    assert response.json["itens emprestados"] == itens_loaned