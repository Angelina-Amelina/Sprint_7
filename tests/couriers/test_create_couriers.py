import pytest
import allure
from helpers import DataGenerate
from data import COURIER_DATA_2, COURIER_WITHOUT_LOGIN, COURIER_WITHOUT_PASSWORD

@allure.suite("Тесты API: Создание курьера")
class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier(self, courier_methods, courier_delete):
        payload = DataGenerate.get_unique_courier_payload()
        courier_data, status_code = courier_methods.create_new_courier(payload)

        if status_code == 201:
            courier_delete.append(payload)

        assert (status_code, courier_data) == (201, {"ok": True}), \
        f"status_code:{status_code}, body: {courier_data}"

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, courier_methods, register_duplicate_courier):
        payload = register_duplicate_courier
        courier_data, status_code = courier_methods.create_new_courier(payload)
        assert status_code == 409, f"status_code:{status_code}"

    @pytest.mark.parametrize("missing_field", [COURIER_WITHOUT_LOGIN, COURIER_WITHOUT_PASSWORD])
    @allure.title("Ошибка создания курьера, если отсутствует обязательное поле")
    def test_create_courier_missing_field(self, courier_methods, missing_field):
        courier_data, status_code = courier_methods.create_new_courier(missing_field)
        assert status_code == 400, f"status_code: {status_code}"


