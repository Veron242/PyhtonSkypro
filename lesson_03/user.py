class User:

# Объявите в классе конструктор с двумя параметрами
        def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#Создаем в классе три метода, которые печатают: имя,фамилию,имя и фамилию.
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_User_info(self):
        return f"User: {self.first_name}, {self.last_name}"

