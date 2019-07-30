"""
Адаптер — це структурний патерн, який дозволяє подружити несумісні об’єкти.
Адаптер виступає прошарком між двома об’єктами,
перетворюючи виклики одного у виклики, що зрозумілі іншому.

Переваги:
  Відокремлює та приховує від клієнта подробиці перетворення різних інтерфейсів.
Недоліки:
  Ускладнює код програми внаслідок введення додаткових класів.
"""
from typing import Any


class Guitar:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return "the {} guitar".format(self.name)

    @staticmethod
    def play() -> str:
        return "is playing a Jazz song"


class Ear:

    def __init__(self, is_left: bool):
        self.side = "left" if is_left else "right"

    def __str__(self) -> str:
        return "the {} ear".format(self.side)

    @staticmethod
    def listen() -> str:
        return "is listening"


class Adapter:

    def __init__(self, obj: Any, **adapted_methods):
        self.obj = obj
        self.__dict__.update(**adapted_methods)

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.obj, attr)

    def __str__(self) -> str:
        return str(self.obj)


if __name__ == "__main__":
    guitar = Guitar('Fender')
    guitar_adapted = Adapter(guitar, do_it=guitar.play)

    ear = Ear(is_left=True)
    ear_adapted = Adapter(ear, do_it=ear.listen)

    print("{} {}\n{} {}".format(
        str(guitar_adapted), guitar_adapted.do_it(),
        str(ear_adapted), ear_adapted.do_it()))


# ================ Output ================
# the Fender guitar is playing a Jazz song
# the left ear is listening
