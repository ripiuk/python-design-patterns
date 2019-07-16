"""
Будівельник — це породжуючий патерн проектування,
який дозволяє створювати об’єкти покроково.
На відміну від інших породжуючих патернів,
Будівельник дозволяє виготовляти різні продукти,
використовуючи один і той же процес будівництва.

Будівельник можна застосувати, якщо створення кількох відображень
об’єкта складається з однакових етапів, які відрізняються деталями.
Переваги:
    Дозволяє створювати продукти покроково.
    Дозволяє використовувати один і той самий код для створення різноманітних продуктів.
    Ізолює складний код конструювання продукту від його головної бізнес-логіки.
Недоліки:
    Ускладнює код програми за рахунок додаткових класів.
    Клієнт буде прив’язаний до конкретних класів будівельників,
        тому що в інтерфейсі будівельника може не бути методу отримання результату.
"""
from abc import ABC, abstractmethod


class Car:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def get_parts(self):
        print("Car parts: {}".format(self.parts))


class Manual:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def get_parts(self):
        print("Manual parts: {}".format(self.parts))


class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def set_engine(self, name: str):
        pass

    @abstractmethod
    def set_seats(self, number: int):
        pass


class CarBuilder(Builder):

    def __init__(self):
        self._car = Car()

    @property
    def product(self) -> Car:
        car = self._car
        self._car = Car()
        return car

    def set_engine(self, name):
        self._car.add("Set {} Engine".format(name))

    def set_seats(self, number: int):
        self._car.add("Set {} Seats".format(number))


class CarManualBuilder(Builder):

    def __init__(self):
        self._manual = Manual()

    @property
    def product(self) -> Manual:
        manual = self._manual
        self._manual = Manual()
        return manual

    def set_engine(self, name):
        if name.lower() == 'sport':
            self._manual.add("The car have a good engine for sport competitions")
        elif name.lower() == 'big one':
            self._manual.add("The car have a very insatiable engine. You should by more fuel")
        else:
            self._manual.add("The car have some engine, I think")

    def set_seats(self, number: int):
        if number == 2:
            self._manual.add("There are 3 doors in the car")
        elif number == 4:
            self._manual.add("There are 5 doors in the car")
        elif number > 4:
            self._manual.add("There are many doors in the car")
        else:
            self._manual.add("There should be some doors in the car, I think")


class Director:

    @staticmethod
    def build_car_with_sport_engine(builder: Builder):
        builder.set_engine("Sport")
        builder.set_seats(2)

    @staticmethod
    def build_car_with_10_seats(builder: Builder):
        builder.set_engine("Big one")
        builder.set_seats(10)

    @staticmethod
    def build_car_only_with_seats(builder: Builder):
        builder.set_seats(4)


if __name__ == '__main__':
    director = Director()
    car_builder = CarBuilder()
    manual_builder = CarManualBuilder()

    director.build_car_with_10_seats(car_builder)
    car_builder.product.get_parts()
    director.build_car_with_10_seats(manual_builder)
    manual_builder.product.get_parts()

    director.build_car_with_sport_engine(car_builder)
    car_builder.product.get_parts()
    director.build_car_with_sport_engine(manual_builder)
    manual_builder.product.get_parts()

    director.build_car_only_with_seats(car_builder)
    car_builder.product.get_parts()
    director.build_car_only_with_seats(manual_builder)
    manual_builder.product.get_parts()

    car_builder.set_seats(1)
    car_builder.set_engine("minimal one")
    car_builder.product.get_parts()

    manual_builder.set_seats(1)
    manual_builder.set_engine("minimal one")
    manual_builder.product.get_parts()
