class Smartphone:

# Объявите в классе конструктор, принимающий на вход следующие параметры:марка телефона,
# модель телефона, абонентский номер («+79…»).
    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number
