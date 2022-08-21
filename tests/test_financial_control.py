from starlette.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_root_status_code():
    response = client.get('/')
    assert response.status_code == 200


def test_root_response_json():
    response = client.get('/')
    assert response.json() == 'Welcome to the financial control app!'


def test_add_transaction_status_code():
    response = client.post(
        url='/',
        data=json.dumps(
            {
                'name': 'comida',
                'month_year': '08-2022',
                'category': 'food',
                'amount': 150.32,
            }
        ),
    )
    assert response.status_code == 201


def test_add_transaction_response_json():
    response = client.post(
        url='/',
        data=json.dumps(
            {
                'name': 'comida',
                'month_year': '08-2022',
                'category': 'food',
                'amount': 150.32,
            }
        ),
    )
    assert response.json() == {
        'name': 'comida',
        'month_year': '08-2022',
        'category': 'food',
        'amount': 150.32,
        'id': 1,
    }


def test_remove_transaction_not_found_id_status_code():
    response = client.delete(url='/?item_id=1')
    assert response.status_code == 404


def test_remove_transaction_found_id_status_code():
    response = client.delete(url='/?item_id=0')
    assert response.status_code == 204


def test_list_transactions_status_code():
    response = client.get('/transactions')
    assert response.status_code == 200


def test_list_transactions_response_json():
    response = client.get('/transactions')
    assert response.json() == [
        {
            'name': 'comida',
            'month_year': '08-2022',
            'category': 'food',
            'amount': 150.32,
            'id': 1,
        }
    ]


def test_show_transaction_status_code():
    response = client.get('/operation/1')
    assert response.status_code == 200


def test_show_transaction_response_json():
    response = client.get('/operation/1')
    assert response.json() == {
        'name': 'comida',
        'month_year': '08-2022',
        'category': 'food',
        'amount': 150.32,
        'id': 1,
    }


def test_show_accounting_status_code():
    response = client.get('balance')
    assert response.status_code == 200


def test_show_accounting_response_json():
    response = client.get('balance')
    assert response.json() == 'R$-150.32'
