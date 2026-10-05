import requests
import allure

class OrderMethods:

    def __init__(self, url, headers=None):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    @allure.step('Создание заказа')
    def create_order(self, params):
        response = requests.post(self.url, json=params, headers=self.headers)
        return response.json(), response.status_code

    @allure.step('Получение конкретного заказа')
    def get_one_order(self, order_id):
        response = requests.get(f"{self.url}/{order_id}", headers=self.headers)
        return response.json(), response.status_code

    @allure.step('Получение списка всех заказов')
    def get_orders(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json(), response.status_code

    @allure.step('Проверка статуса ответа')
    def check_response(self, expected_value, response_status_code):
        return response_status_code == expected_value