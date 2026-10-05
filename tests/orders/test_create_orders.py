import pytest
import allure
from data import ORDER_PAYLOAD

@allure.suite("Тесты API: Создание заказа")
class TestCreateOrder:
    @allure.title("Успешное создание заказа с выбором разных цветов")
    @pytest.mark.parametrize("color_value", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, order_methods, color_value):
        complete_payload = {**ORDER_PAYLOAD, "color": color_value}
        response_data, status_code = order_methods.create_order(complete_payload)

        assert (status_code, "track" in response_data) == (201, True), \
            f"status_cod: {status_code}, body: {response_data}"

    @allure.title("Успешное получение списка заказов")
    def test_get_orders_list_success(self, order_methods):
        response_data, status_code = order_methods.get_orders()

        assert (status_code, "orders" in response_data, type(response_data.get("orders"))) == (200, True, list), \
            f"status_code: {status_code}, body: {response_data}"