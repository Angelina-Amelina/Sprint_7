import pytest
from urls import BASE_URL, ORDERS_URL, COURIERS_URL
from methods.order_methods import OrderMethods
from methods.couriers_methods import CouriersMethods
from helpers import DataGenerate


@pytest.fixture()
def order_methods():
    return OrderMethods(url=f'{BASE_URL}{ORDERS_URL}')

@pytest.fixture()
def courier_methods():
    return CouriersMethods(url=f'{BASE_URL}{COURIERS_URL}')

@pytest.fixture()
def courier():
    courier_methods = CouriersMethods(url=f'{BASE_URL}{COURIERS_URL}')
    payload = DataGenerate.get_unique_courier_payload()
    response_data, status_code = courier_methods .create_new_courier(payload)
    yield response_data, payload

    login_json, _ = courier_methods.authorize_courier(payload)

    if 'id' in login_json:
        courier_methods.delete_courier(login_json['id'])

@pytest.fixture()
def authorize_courier(courier, courier_methods):
    response_data, _ = courier_methods.authorize_courier(courier[1])
    return response_data['id']
