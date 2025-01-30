import json

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")

    def eat(self):
        print(f"{self.name} is eating.")

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} says: Chirp chirp!")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} says: Roar!")

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} says: Hiss!")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename):
        zoo_data = {
            "animals": [{"type": type(animal).__name__, "name": animal.name, "age": animal.age} for animal in self.animals],
            "staff": [{"type": type(staff).__name__, "name": staff.name} for staff in self.staff]
        }
        with open(filename, 'w') as file:
            json.dump(zoo_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            zoo_data = json.load(file)
            for animal_data in zoo_data["animals"]:
                if animal_data["type"] == "Bird":
                    animal = Bird(animal_data["name"], animal_data["age"], wingspan=0)
                elif animal_data["type"] == "Mammal":
                    animal = Mammal(animal_data["name"], animal_data["age"], fur_color="")
                elif animal_data["type"] == "Reptile":
                    animal = Reptile(animal_data["name"], animal_data["age"], scale_type="")
                self.animals.append(animal)
            for staff_data in zoo_data["staff"]:
                if staff_data["type"] == "ZooKeeper":
                    staff = ZooKeeper(staff_data["name"])
                elif staff_data["type"] == "Veterinarian":
                    staff = Veterinarian(staff_data["name"])
                self.staff.append(staff)

# Пример использования
zoo = Zoo()

# Добавляем животных
zoo.add_animal(Bird("Parrot", 5, 30))
zoo.add_animal(Mammal("Lion", 10, "Golden"))
zoo.add_animal(Reptile("Snake", 3, "Smooth"))

# Добавляем сотрудников
zoo.add_staff(ZooKeeper("John"))
zoo.add_staff(Veterinarian("Alice"))

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Сохраняем состояние зоопарка в файл
zoo.save_to_file("zoo_state.json")

# Загружаем состояние зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file("zoo_state.json")

# Проверяем загруженное состояние
animal_sound(new_zoo.animals)