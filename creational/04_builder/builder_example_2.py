"""
Builder Pattern is a unique design pattern which helps in building
complex object using simple objects and uses an algorithmic approach.
This design pattern comes under the category of creational pattern.
In this design pattern, a builder class builds the final object in step-by-step procedure.
This builder is independent of other objects.
"""
from collections import namedtuple
from abc import ABC, abstractmethod


Wheel = namedtuple('Wheel', ('size', ))
Engine = namedtuple('Engine', ('horsepower', ))
Body = namedtuple('Body', ('shape', ))


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body: Body):
        self.__body = body

    def attach_wheel(self, wheel: Wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine: Engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)


class Builder(ABC):
    @abstractmethod
    def get_wheel(self) -> Wheel: pass

    @abstractmethod
    def get_engine(self) -> Engine: pass

    @abstractmethod
    def get_body(self) -> Body: pass


class JeepBuilder(Builder):

    def get_wheel(self) -> Wheel:
        return Wheel(size=22)

    def get_engine(self) -> Engine:
        return Engine(horsepower=400)

    def get_body(self) -> Body:
        return Body(shape="SUV")


class PassengerBuilder(Builder):

    def get_wheel(self) -> Wheel:
        return Wheel(size=18)

    def get_engine(self) -> Engine:
        return Engine(horsepower=200)

    def get_body(self) -> Body:
        return Body(shape="simple one")


class Director:
    __builder = None

    def set_builder(self, builder: Builder) -> None:
        self.__builder = builder

    def get_car(self) -> Car:
        car = Car()
        car.set_body(self.__builder.get_body())
        car.set_engine(self.__builder.get_engine())
        for _ in range(4):
            car.attach_wheel(self.__builder.get_wheel())

        return car


if __name__ == "__main__":
    director = Director()

    print("Jeep")
    jeep_builder = JeepBuilder()
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()

    print("\nPassenger")
    passenger_builder = PassengerBuilder()
    director.set_builder(passenger_builder)
    passenger = director.get_car()
    passenger.specification()


# ================ Output ================
# Jeep
# body: SUV
# engine horsepower: 400
# tire size: 22'
#
# Passenger
# body: simple one
# engine horsepower: 200
# tire size: 18'
