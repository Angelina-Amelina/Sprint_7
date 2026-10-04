# Полные данные
COURIER_DATA_1 = {
    "login": "Igor",
    "password": "125999",
    "firstName": "Ivanov"
}
# Данные для проверки дублирующихся курьеров при их создании
COURIER_DATA_2 = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

# Не указан логин при создании курьера
COURIER_WITHOUT_LOGIN = {
    "password": "1234",
    "firstName": "saske"
}

# Не указан пароль при создании курьера
COURIER_WITHOUT_PASSWORD = {
    "login": "ninja_error_test",
    "firstName": "saske"
}

# Данные для проверки авторизации с неправильным паролем
COURIER_WRONG_PASSWORD = {
    "login": "ninja",
    "password": "PASSWORD_123"
}

# Данные для проверки авторизации с несуществующим логином
COURIER_NOT_EXIST = {
    "login": "12345_user_2026",
    "password": "1234"
}

# Авторизация без логина
LOGIN_WITHOUT_USERNAME = {
    "password": "1234"
}

# Авторизация без пароля
LOGIN_WITHOUT_PASSWORD = {
    "login": "ninja"
}

# Заполнение заказа
ORDER_PAYLOAD = {
    "firstName": "Anton",
    "lastName": "Petrov",
    "address": "Lenina street, 221B",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2026-12-12",
    "comment": "Как можно скорее",
}
