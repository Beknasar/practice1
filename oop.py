"""
    2. ООП (классы, наследование, полиморфизм)
    ✅ Задания:

    1. Создайте класс Car с атрибутами brand, model, year и методом start(), который выводит сообщение "Машина {brand} {model} завелась"
    Создайте класс ElectricCar, который наследуется от Car и добавьте атрибут battery_capacity. Переопределите метод start(), чтобы он выводил "Электромобиль {brand} {model} с батареей {battery_capacity} кВтч завелся".
    2. Создайте класс Animal с методом make_sound(), который выводит "Животное издает звук".
    Создайте подклассы Dog и Cat, переопределите метод make_sound() так, чтобы собака лаяла, а кошка мяукала.
    Напишите функцию play_sound(animal), которая вызывает make_sound() у переданного объекта.
"""
# 1. Создайте класс Car с атрибутами brand, model, year и методом start(),
# который выводит сообщение "Машина {brand} {model} завелась"

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"Машина {self.brand} {self.model} завелась")


c1 = Car("BMW", "X6", "2012")
c1.start()


# Создайте класс ElectricCar, который наследуется от Car и добавьте атрибут battery_capacity.
# Переопределите метод start(),
# чтобы он выводил "Электромобиль {brand} {model} с батареей {battery_capacity} кВтч завелся".
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start(self):
        print(f"Электромобиль {self.brand} {self.model} с батареей {self.battery_capacity} кВтч завелся")


e1 = ElectricCar("Tesla", "M1", "2022", 100)
e1.start()


# 2. Создайте класс Animal с методом make_sound(), который выводит "Животное издает звук".
class Animal:
    def make_sound(self):
        print("Животное издаёт звук")


a1 = Animal()
a1.make_sound()

# Создайте подклассы Dog и Cat, переопределите метод make_sound() так, чтобы собака лаяла, а кошка мяукала.
class Dog(Animal):
    def make_sound(self):
        print("Woof")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


dog1 = Dog()
cat1 = Cat()
dog1.make_sound()
cat1.make_sound()


# Напишите функцию play_sound(animal), которая вызывает make_sound() у переданного объекта.
def play_sound(animal):
    animal.make_sound()


play_sound(dog1)
play_sound(cat1)
play_sound(a1)
