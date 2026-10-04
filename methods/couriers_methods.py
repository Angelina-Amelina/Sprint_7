import requests
import allure

class CouriersMethods:

    def __init__(self, url=None):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    @allure.step('Создать курьера')
    def create_new_courier(self, params):
        response = requests.post(self.url, json=params, headers=self.headers)
        return response.json(), response.status_code

    @allure.step('Авторизовать курьера')
    def authorize_courier(self, payload):
        response = requests.post(f"{self.url}/login", json=payload, headers=self.headers)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return {"message": "Gateway Timeout (HTML)"}, response.status_code

    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f"{self.url}/{courier_id}", headers=self.headers)
        return response



