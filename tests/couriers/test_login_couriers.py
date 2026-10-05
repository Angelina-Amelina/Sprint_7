import pytest
import allure
from data import COURIER_WRONG_PASSWORD, COURIER_NOT_EXIST, LOGIN_WITHOUT_USERNAME, LOGIN_WITHOUT_PASSWORD


@allure.suite("Тесты API: Авторизация курьера")
class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_methods, courier):
        _, courier_payload = courier
        response_data, status_code = courier_methods.authorize_courier(courier_payload)
        assert (status_code, "id" in response_data) == (200, True), \
            f"status_code: {status_code}, body: {response_data}"

    @allure.title("Ошибка авторизации, если неправильно указать пароль или логин")
    @pytest.mark.parametrize("invalid_payload", [COURIER_WRONG_PASSWORD, COURIER_NOT_EXIST])
    def test_login_courier_invalid(self, courier_methods, invalid_payload):
        response_data, status_code = courier_methods.authorize_courier(invalid_payload)

        assert (status_code, response_data.get("message")) == (404, "Учетная запись не найдена"), \
            f"status_code: {status_code}, body: {response_data}"

    @allure.title("Ошибка авторизации, если не передано одно из обязательных полей")
    @pytest.mark.parametrize("missing_field_payload", [LOGIN_WITHOUT_USERNAME, LOGIN_WITHOUT_PASSWORD])
    def test_login_courier_missing_fields(self, courier_methods, missing_field_payload):
        response_data, status_code = courier_methods.authorize_courier(missing_field_payload)
        assert (status_code, response_data.get("message")) == (400, "Недостаточно данных для входа"), \
            f"status_code: {status_code}, body: {response_data}"