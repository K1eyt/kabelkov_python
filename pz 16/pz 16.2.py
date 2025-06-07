# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
# выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
# свойство "тип кузова"

class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


class Automobile(Transport):
    def __init__(self, brand, model, year, type):
        Transport.__init__(self, brand, model, year)
        self.type = type

    def display_info(self):
        Transport.display_info(self)
        print(f"Тип кузова: {self.type}")

if __name__ == "__main__":
    transport = Transport("Boeing", "747", 2005)
    print("Информация о транспортном средстве:")
    transport.display_info()

    car = Automobile("Toyota", "Camry", 2022, "Седан")
    print("Информация об автомобиле:")
    car.display_info()

    car2 = Automobile("BMW", "X5", 2023, "Внедорожник")
    print("Информация об автомобиле:")
    car2.display_info()