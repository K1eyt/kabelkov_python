# Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
# выводит информацию о животном в формате "Имя: имя, Вид: вид".

class Animal:
    def __init__(self, name, antype):
        self.name = name
        self.antype = antype

    def display_info(self):
        print(f"Имя: {self.name}, Вид: {self.antype}")

if __name__ == "__main__":
    my_animal = Animal("Барсик", "Кот")
    my_animal.display_info()

    dog_animal = Animal("Бобик", "Собака")
    dog_animal.display_info()

    lien_animal = Animal("Африканский лев", "Лев")
    lien_animal.display_info()