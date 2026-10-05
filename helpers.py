import uuid

class DataGenerate:

    @staticmethod
    def get_unique_courier_payload():
        unique_id = uuid.uuid4().hex[:8]

        return {
            "login": f"Igor_{unique_id}",
            "password": "125999",
            "firstName": "Ivanov"
        }

    @staticmethod
    def get_duplicate_courier_payload():
        return {
            "login": "ninja",
            "password": "1234",
            "firstName": "saske"
        }

    @staticmethod
    def get_base_order_payload():
        return {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }