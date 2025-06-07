class Animal:
    def __init__(self, name, species):  # Исправлено на __init__
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Имя: {self.name}, Вид: {self.species}")


if __name__ == "__main__":
    my_animal = Animal("Денчик", "Кот")
    my_animal.display_info()

    another_animal = Animal("Вазген", "Собака")
    another_animal.display_info()

    wild_animal = Animal("Африканский Вазген", "Лев")
    wild_animal.display_info()