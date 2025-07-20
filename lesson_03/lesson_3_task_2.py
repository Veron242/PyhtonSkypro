from smartphone import Smartphone

# Создаем каталог смартфонов
catalog = [
    Smartphone("Apple", "iPhone", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79229876543"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79337654321"),
    Smartphone("Google", "Pixel 8", "+79446543210"),
    Smartphone("Realme", "C75", "+79555432109")
]
# Выводим каталог в заданном формате
for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.subscriber_number}")